from odoo import models, fields, api, _


class InheritedAccountTaxInheritCustomAccount(models.Model):
    _inherit = "account.tax"

    base_amount = fields.Float()
    rabill_id = fields.Many2one('account.account')
    real_amount = fields.Float()


class InheritedAccountTaxRepartitionInheritCustomAccount(models.Model):
    _inherit = "account.tax.repartition.line"

    refund_tax_id = fields.Many2one('account.tax')
    invoice_tax_id = fields.Many2one('account.tax')

    
class InheritedAccountMoveInheritCustomAccount(models.Model):
    _inherit = "account.move"
    _description = "Account Move Inherit"

    project_id = fields.Many2one('project.project')


class InheritedAccountMoveLineInheritCustomAccount(models.Model):
    _inherit = "account.move.line"
    _description = "Account Move Line Inherit"

    followup_line_id = fields.Many2one('account.account')
    job_cost_id = fields.Many2one('account.account')
    job_cost_line_id = fields.Many2one('account.account')
    picking_id = fields.Many2one('account.account')
    vehicle_id = fields.Many2one('account.account')
    analytic_account_id = fields.Many2one('account.account')
    tax_tag_ids = fields.Many2many('account.account.tag',
        string="Analytics Tags",
        ondelete='restrict',
        tracking=True,
        help="Tags assigned to this line by the tax creating it, if any. It determines its impact on financial reports.",
    )
    purchase_line_id = fields.Many2one('purchase.order.line')
    tax_audit = fields.Char()
    remark = fields.Char()
    expected_pay_date = fields.Date()
    next_action_date = fields.Date()
    last_followup_date = fields.Date()
    discount_percentage = fields.Float()


class InheritedResUsers(models.Model):
    _inherit = "res.users"

    target_sales_invoiced = fields.Float()
    target_sales_done = fields.Float()
    target_sales_won = fields.Float()


class InheritedResPartner(models.Model):
    _inherit = "res.partner"

    @api.depends('parent_id')
    def _compute_display_name(self):
        for category in self:
            names = []
            current = category
            while current:
                names.append(current.name or "")
                current = current.parent_id
            category.display_name = ' / '.join(reversed(names))


class AccountJournalInherit(models.Model):
    _inherit = "account.journal"

    account_online_account_id = fields.Many2one('account.account')
    account_online_link_id = fields.Many2one('account.account')
    message_main_attachment_id = fields.Many2one('account.account')


class AccountAccountInherit(models.Model):
    _inherit = "account.account"
    _description = "Account Account Inherit"

    message_main_attachment_id = fields.Many2one('account.account')

    asset_model = fields.Many2one('account.account')
    create_asset = fields.Char()
    is_off_balance = fields.Boolean()
    multiple_assets_per_line = fields.Boolean()

