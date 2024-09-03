# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _
from odoo.exceptions import UserError

class pos_session(models.Model):
    _inherit = 'pos.session'
    branch_not_used = fields.Boolean(string="", compute='check_branch_not_used')

    @api.depends('company_id')
    def check_branch_not_used(self):
        for rec in self:
            if self.env.company.branch_not_used == True:
                rec.branch_not_used = True
            else:
                rec.branch_not_used = False
    '''@api.model
    def _get_pos_session_default_branch(self):
        user_pool = self.env['res.users']
        branch_id = user_pool.browse(self.env.uid).branch_id.id  or False
        return branch_id'''

    @api.model
    def create(self,vals):
        res = super(pos_session, self).create(vals)
        user_pool = self.env['res.users']
        res.branch_id = user_pool.browse(self.env.uid).branch_id.id  or False
        return res

    branch_id = fields.Many2one('res.branch', 'Branch')

    def _create_account_move(self, balancing_account=False, amount_to_balance=0, bank_payment_method_diffs=None):
        return super(pos_session, self.with_context(branch_id=self.branch_id.id))._create_account_move(balancing_account, amount_to_balance, bank_payment_method_diffs)