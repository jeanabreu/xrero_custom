# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _
from odoo.exceptions import UserError


# class SaleAdvancePaymentInv(models.TransientModel):
#     _inherit = 'sale.advance.payment.inv'
#
#
#     def _create_invoice(self, order, so_line, amount):
#         result = super(SaleAdvancePaymentInv, self)._create_invoice(order, so_line, amount)
#
#         branch_id = False
#
#         if order.branch_id and not self.env.company.branch_not_used:
#             branch_id = order.branch_id.id
#         elif self.env.user.branch_id and not self.env.company.branch_not_used:
#             branch_id = self.env.user.branch_id.id
#
#         result.write({
#             'branch_id' : branch_id
#             })
#
#         return result

class account_payment_register(models.TransientModel):
    _inherit = 'account.payment.register'

    branch_id = fields.Many2one('res.branch')
    branch_not_used = fields.Boolean(string="", compute='check_branch_not_used')

    @api.depends('company_id')
    def check_branch_not_used(self):
        for rec in self:
            if self.env.company.branch_not_used == True:
                rec.branch_not_used = True
            else:
                rec.branch_not_used = False




