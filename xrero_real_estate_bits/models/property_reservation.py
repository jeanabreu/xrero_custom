import calendar
import datetime
from datetime import date, datetime, timedelta

from odoo import api, fields, models
from odoo.exceptions import UserError
from odoo.tools.translate import _
from .project_worksite import PROJECT_WORKSITE_TYPE


class PropertyReservation(models.Model):
    _name = "property.reservation"
    _description = "Property Reservation"
    _inherit = ["mail.thread", "mail.activity.mixin"]

    def _contract_count(self):
        property_contract = self.env["property.contract"]
        for rec in self:
            contract_ids = property_contract.search([("reservation_id", "=", rec.id)])
            rec.contract_count_own = len(contract_ids.filtered(lambda x: x.contract_type == "is_ownership"))
            rec.contract_count_rent = len(contract_ids.filtered(lambda x: x.contract_type == "is_rental"))

    def _deposit_count(self):
        payment_obj = self.env["account.payment"]
        for rec in self:
            rec.deposit_count = len(payment_obj.search([("reservation_id", "=", rec.id)]))

    account_income = fields.Many2one("account.account", "Income Account")

    contract_count_own = fields.Integer(compute="_contract_count", string="Sales")
    contract_count_rent = fields.Integer(compute="_contract_count", string="Rentals")

    deposit_count = fields.Integer(compute="_deposit_count", string="Deposits")

    # Reservation Info
    name = fields.Char("Name", size=64, default='New')
    booking_type = fields.Selection([('is_rental', 'Rental'), ('is_ownership', 'Ownership')], default='is_rental')
    date = fields.Datetime("Reservation Date", default=fields.Datetime.now())
    maintenance_deposit = fields.Float(string="Maintenance Deposit", required=False)
    payment_type = fields.Selection(string="Payment Type", selection=[("cash", "Case"),
                                                                      ("debit", "Debit")], required=False)
    date_payment = fields.Date("First Payment Date")

    # Project Info
    project_id = fields.Many2one("project.worksite", "Project")
    project_code = fields.Char("Project Code", related='project_id.default_code', store=True)

    # Property Info
    type = fields.Selection(selection=PROJECT_WORKSITE_TYPE + [('shop', 'Shop')], string="Project Type")
    property_id = fields.Many2one("product.template", "Property", required=True,
                                  domain=[("is_property", "=", True), ("state", "=", "free")])
    property_code = fields.Char("Property Code", related='property_id.default_code', store=True)
    property_price_type = fields.Selection(related='property_id.property_price_type', store=True)
    price_per_m = fields.Float('Price Per m²', related='property_id.price_per_m', store=True)
    property_area = fields.Float("Property Area", related='property_id.property_area', store=True)
    floor = fields.Integer("Floor", related='property_id.floor', store=True)
    address = fields.Char("Address", related='property_id.address', store=True)
    net_price = fields.Float("Selling Price")

    template_id = fields.Many2one("installment.template", "Payment Template")
    contract_id = fields.Many2one("property.contract", "Property Contract")

    property_type_id = fields.Many2one("property.type", "Property Type", related='property_id.property_type_id',
                                       store=True)
    region_id = fields.Many2one("region.region", "Region")
    user_id = fields.Many2one("res.users", "Responsible", default=lambda self: self.env.user)
    partner_id = fields.Many2one("res.partner", "Customer")
    loan_line_ids = fields.One2many("loan.line", "reservation_id")
    state = fields.Selection([("draft", "Draft"), ("confirmed", "Confirmed"), ("contracted", "Contracted"),
                              ("canceled", "Canceled")], "Status", default="draft")
    company_id = fields.Many2one("res.company", string="Company", default=lambda self: self.env.company)
    deposit = fields.Float("Deposit", digits=(16, 2), )
    advance_payment_type = fields.Selection([("percentage", "Percentage"), ("amount", "Amount")],
                                            "Advance Payment Type")

    advance_payment = fields.Float("Advance Payment")

    channel_partner_id = fields.Many2one("res.partner")
    channel_partner_commission = fields.Float("Commission")
    commission_status = fields.Selection([("percentage", "Percentage"), ("amount", "Amount")], default="percentage")
    commission_base_amount_selection = fields.Selection(
        [("sales_price", "Sales Price"), ("tax_base_amount", "Tax Base Amount")],
        default="sales_price", string="Commission Base Amount Selection")
    commission_base_amount = fields.Float("Commission Base Amount", compute="_compute_commission" ,store=True)
    total_commission = fields.Float("Total Commission", compute="_compute_commission", store=True)

    @api.depends('commission_base_amount_selection', 'commission_status', 'commission_base_amount',
                 'channel_partner_commission')
    def _compute_commission(self):
        if self.commission_base_amount_selection == "tax_base_amount":
            self.commission_base_amount = self.property_id.tax_base_amount
        else:
            self.commission_base_amount = self.property_id.net_price

        if self.commission_status == "percentage":
            self.total_commission = (self.channel_partner_commission * self.commission_base_amount) / 100
        else:
            self.total_commission = self.channel_partner_commission

    def unlink(self):
        for rec in self:
            if rec.state != "draft":
                raise UserError(_("You can not delete a reservation not in draft state"))
        super(PropertyReservation, self).unlink()

    @api.onchange("property_id")
    def onchange_property(self):
        self.property_type_id = self.property_id.property_type_id.id
        self.project_id = self.property_id.project_worksite_id.id
        self.region_id = self.property_id.region_id.id
        self.net_price = self.property_id.net_price

    def action_draft(self):
        self.write({"state": "draft"})

    def action_cancel(self):
        self.write({"state": "canceled"})
        self.property_id.write({"state": "free"})

    def action_confirm(self):
        if self.name == 'New' or not self.name:
            self.name = self.env["ir.sequence"].next_by_code("property.booking")
        self.write({"state": "confirmed"})
        self.property_id.write({"state": "reserved"})

    def action_receive_deposit(self):
        if not self.deposit:
            raise UserError(_("Please set the deposit amount!"))

        return {
            "name": _("Payment"),
            "view_type": "form",
            "view_mode": "form",
            "res_model": "account.payment",
            "view_id": self.env.ref("account.view_account_payment_form").id,
            "type": "ir.actions.act_window",
            "context": {
                "form_view_initial_mode": "edit",
                "default_payment_type": "inbound",
                "default_partner_type": "customer",
                "default_amount": self.deposit,
                "default_partner_id": self.partner_id.id,
                "default_reservation_id": self.id,
            },
            "target": "current",
        }

    def view_deposits(self):
        payment_obj = self.env["account.payment"]
        payment_ids = payment_obj.search([("reservation_id", "=", self.id)])

        return {
            "name": _("Deposits"),
            "domain": [("id", "in", payment_ids.ids)],
            "view_type": "form",
            "view_mode": "tree,form",
            "res_model": "account.payment",
            "type": "ir.actions.act_window",
            "nodestroy": True,
            "view_id": False,
            "target": "current",
        }

    def action_contract_ownership(self):
        return {
            "name": _("Ownership Contract"),
            "view_type": "form",
            "view_mode": "form",
            "res_model": "property.contract",
            "view_id": self.env.ref("xrero_real_estate_bits.view_property_contract_form").id,
            "type": "ir.actions.act_window",
            "context": {
                "form_view_initial_mode": "edit",
                "default_contract_type": "is_ownership",
                "default_project_id": self.project_id.id,
                "default_partner_id": self.partner_id.id,
                "default_property_id": self.property_id.id,
                "default_type": self.type,
                "default_pricing": self.net_price,
                "default_price_per_m": self.price_per_m,
                "default_property_price_type": self.property_price_type,
                "default_reservation_id": self.id,
                "default_deposit": self.deposit,
                "default_advance_payment_type": self.advance_payment_type,
            },
            "target": "current",
        }

    def action_contract_rental(self):
        return {
            "name": _("Rental Contract"),
            "view_type": "form",
            "view_mode": "form",
            "res_model": "property.contract",
            "view_id": self.env.ref("xrero_real_estate_bits.view_property_contract_form").id,
            "type": "ir.actions.act_window",
            "context": {
                "form_view_initial_mode": "edit",
                "default_contract_type": "is_rental",
                "default_project_id": self.project_id.id,
                "default_partner_id": self.partner_id.id,
                "default_property_id": self.property_id.id,
                "default_pricing": self.net_price,
                "default_price_per_m": self.price_per_m,
                "default_property_price_type": self.property_price_type,
                "default_type": self.type,
                "default_reservation_id": self.id,
            },
            "target": "current",
        }

    def view_contract_own(self):
        own_ids = self.env["property.contract"].search(
            [("reservation_id", "=", self.id), ('contract_type', '=', 'is_ownership')])
        return {
            "name": _("Ownership Contract"),
            "domain": [("id", "in", own_ids.ids)],
            "view_type": "form",
            "view_mode": "tree,form",
            "res_model": "property.contract",
            "type": "ir.actions.act_window",
            "nodestroy": True,
            "view_id": False,
            "target": "current",
        }

    def view_contract_rent(self):
        rent_ids = self.env["property.contract"].search(
            [("reservation_id", "=", self.id), ('contract_type', '=', "is_rental")])
        return {
            "name": _("Rental Contract"),
            "domain": [("id", "in", rent_ids.ids)],
            "view_type": "form",
            "view_mode": "tree,form",
            "res_model": "property.contract",
            "type": "ir.actions.act_window",
            "nodestroy": True,
            "view_id": False,
            "target": "current",
        }

    def add_months(self, source_date, months):
        month = source_date.month - 1 + months
        year = int(source_date.year + month / 12)
        month = month % 12 + 1
        day = min(source_date.day, calendar.monthrange(year, month)[1])
        return date(year, month, day)

    def _prepare_lines(self, date_payment):
        loan_line_ids = []
        if self.template_id:
            net_price = self.net_price
            mon = self.template_id.duration_month
            yr = self.template_id.duration_year
            repetition = self.template_id.repetition_rate
            advance_percent = self.template_id.adv_payment_rate
            deduct = self.template_id.deduct
            if not date_payment:
                raise UserError(_("Please select first payment date!"))
            adv_payment = net_price * float(advance_percent) / 100
            if mon > 12:
                x = mon / 12
                mon = (x * 12) + mon % 12
            mons = mon + (yr * 12)
            if adv_payment:
                loan_line_ids.append(
                    (
                        0,
                        0,
                        {
                            "amount": adv_payment,
                            "date": date_payment,
                            "name": _("Advance Payment"),
                        },
                    )
                )
                if deduct:
                    net_price -= adv_payment
            loan_amount = (net_price / float(mons)) * repetition
            m = 0
            i = 2
            while m < mons:
                loan_line_ids.append(
                    (
                        0,
                        0,
                        {
                            "amount": loan_amount,
                            "date": date_payment,
                            "name": _("Loan Installment"),
                        },
                    )
                )
                i += 1
                date_payment = self.add_months(date_payment, repetition)
                m += repetition
        return loan_line_ids
