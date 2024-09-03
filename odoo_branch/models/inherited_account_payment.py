# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _

MAP_INVOICE_TYPE_PARTNER_TYPE = {
    'out_invoice': 'customer',
    'out_refund': 'customer',
    'in_invoice': 'supplier',
    'in_refund': 'supplier',
}

class AccountPayment(models.Model):
    _inherit = 'account.payment'

    @api.model
    def default_get(self, default_fields):
        res = super(AccountPayment, self).default_get(default_fields)
        if self.env.user.branch_id and not self.env.company.branch_not_used:
            res.update({
                'branch_id': self.env.user.branch_id.id or False
            })
        return res

    # @api.model
    # def default_get(self, fields):
    #     rec = super(AccountPayment, self).default_get(fields)
    #
    #     invoice_defaults = self.resolve_2many_commands('invoice_ids', rec.get('invoice_ids'))
    #
    #     if invoice_defaults and len(invoice_defaults) == 1:
    #         invoice = invoice_defaults[0]
    #         rec['communication'] = invoice['name'] or invoice['number']
    #         rec['currency_id'] = invoice['currency_id'][0]
    #         rec['payment_type'] = invoice['type'] in ('out_invoice', 'in_refund') and 'inbound' or 'outbound'
    #         rec['partner_type'] = MAP_INVOICE_TYPE_PARTNER_TYPE[invoice['type']]
    #         rec['partner_id'] = invoice['partner_id'][0]
    #         rec['amount'] = invoice['amount_residual']
    #         rec['branch_id'] = invoice.get('branch_id') and invoice.get('branch_id')[0] if not not self.env.company.branch_not_used else False
    #     return rec

    branch_id = fields.Many2one('res.branch')
    branch_not_used = fields.Boolean(string="", compute='check_branch_not_used')

    @api.depends('company_id')
    def check_branch_not_used(self):
        for rec in self:
            if self.env.company.branch_not_used == True:
                rec.branch_not_used = True
            else:
                rec.branch_not_used = False


class AccountPaymentRegister(models.TransientModel):
    _inherit = 'account.payment.register'

    def _create_payment_vals_from_wizard(self):
        res = super(AccountPaymentRegister, self)._create_payment_vals_from_wizard()
        invoice_ids = self.env['account.move'].browse(self._context.get('active_ids', []))
        branch_id = False
        for rec in invoice_ids:
            branch_id = rec.branch_id.id
        res.update({'branch_id':branch_id})
        return res

    def _create_payment_vals_from_batch(self, batch_result):
        res = super(AccountPaymentRegister, self)._create_payment_vals_from_batch(batch_result)
        invoice_ids = self.env['account.move'].browse(self._context.get('active_ids', []))
        branch_id = False
        for rec in invoice_ids:
           branch_id = rec.branch_id.id

        res.update({'branch_id': branch_id})
        return res

