# -*- coding: utf-8 -*-

from odoo import fields, models


class AccountingCommonPartnerReport(models.TransientModel):
    _name = 'account.common.partner.report'
    _inherit = "account.common.report"
    _description = 'Account Common Partner Report'

    result_selection = fields.Selection([('customer', 'Receivable Accounts'),
                                         ('supplier', 'Payable Accounts'),
                                         ('customer_supplier', 'Receivable and Payable Accounts')
                                         ], string="Partner's", required=True, default='customer')
    partner_ids = fields.Many2many('res.partner', string='Partners')

    def pre_print_report(self, data):
        partner_ids = self.partner_ids
        if not self.partner_ids:
            partner_ids = self.env['res.partner'].search([])
        data['form'].update(self.read(['result_selection'])[0])
        data['form'].update({'partner_ids': partner_ids.ids})
        print('data', data)
        return data
