# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import datetime
from odoo.exceptions import ValidationError

class HrVisitorProcess(models.Model):
    _name = 'hr.visitor'
    _description = 'Hr Visitor'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _order = 'in_datetime desc, id desc'

    name = fields.Char(string="Number", readonly=True)
    visitor_name = fields.Char(required=True, string="Visitor Name")
    visitor_company_id = fields.Many2one('res.partner', required=False, string="Visitor Company")
    partner_id = fields.Many2one('hr.employee', required=True, string="Employee")
    in_datetime = fields.Datetime(required=True, string="Date Time In")
    out_datetime = fields.Datetime(string="Date Time Out")
    mobile_number = fields.Char(required=True,  string="Phone/Mobile")
    email = fields.Char(string="Email")
    purpose = fields.Text(required=True, string="Reason")
    department_id = fields.Many2one('hr.department', required=True, string="Department")
    user_id = fields.Many2one('res.users', required=True, default=lambda self: self.env.user, string='Created By', readonly=True)
    company_id = fields.Many2one('res.company', required=True, default=lambda self: self.env.user.company_id, string='Company', readonly=True)
    state = fields.Selection([
         ('draft', 'Draft'),
         ('confirm', 'Confirmed'),
         ('exit', 'Exit'),
         ('cancel', 'Cancelled')], default='draft',
        tracking=True,
        copy=False, string="Status")
    
#     @api.multi                   #odoo13
    def action_confirm(self):
        self.state = 'confirm'
        self.name = self.env['ir.sequence'].next_by_code('hr.visitor')

#     @api.multi                  #odoo13
    def action_exit(self):
        for record in self:
            record.state = 'exit'
            if record.out_datetime == False:
                raise ValidationError("Please Enter The Date Time Out.")

#     @api.multi                   #odoo13
    def action_cancel(self):
        self.state = 'cancel'
        
#     @api.multi                   #odoo13
    def action_reset_to_draft(self):
        self.state = 'draft'

#     @api.multi                   #odoo13
    def print_visitor_card(self):
        return self.env.ref('xrero_hr_visitor.visitor_process_report').report_action(self)
        # odoo11 return self.env['report'].get_action(self, 'xrero_hr_visitor.visitor_report_view')
    
    @api.onchange('partner_id')
    def _onchange_partner(self):
        self.department_id = self.partner_id.department_id
        
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
