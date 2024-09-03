# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _


class account_bank_statement_line(models.Model):

    _inherit = 'account.bank.statement.line'

    @api.model
    def default_get(self, default_fields):
        res = super(account_bank_statement_line, self).default_get(default_fields)
        branch_id = False
        if self._context.get('branch_id') and not self.env.company.branch_not_used:
            branch_id = self._context.get('branch_id')
        elif self.env.user.branch_id and not self.env.company.branch_not_used:
            branch_id = self.env.user.branch_id.id
        res.update({
            'branch_id' : branch_id
        })
        return res

    branch_id = fields.Many2one('res.branch', string='Branch')
    branch_not_used = fields.Boolean(string="", compute='check_branch_not_used')

    @api.depends('company_id')
    def check_branch_not_used(self):
        for rec in self:
            if self.env.company.branch_not_used == True:
                rec.branch_not_used = True
            else:
                rec.branch_not_used = False

