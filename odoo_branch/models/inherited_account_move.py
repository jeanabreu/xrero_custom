# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _
from odoo.exceptions import UserError
from odoo.tools.float_utils import float_compare




class AccountMove(models.Model):
    _inherit = 'account.move'

    @api.constrains('branch_id')
    def _get_onclick_image(self):
        for rec in self:
            if rec.branch_id:
                for aml in rec.line_ids:
                    if not aml.branch_id:
                        aml.branch_id = rec.branch_id.id

    @api.model
    def default_get(self, default_fields):
        res = super(AccountMove, self).default_get(default_fields)
        branch_id = False
        if self._context.get('branch_id') and not self.env.company.branch_not_used:
            branch_id = self._context.get('branch_id')
        elif self.env.user.branch_id and not self.env.company.branch_not_used:
            branch_id = self.env.user.branch_id.id
        res.update({
            'branch_id' : branch_id
        })
        return res


    branch_id = fields.Many2one('res.branch', string="Branch")
    branch_name = fields.Char( string="Branch",related='branch_id.name',store=True)
    branch_not_used = fields.Boolean(string="", compute='check_branch_not_used')

    @api.depends('company_id')
    def check_branch_not_used(self):
        for rec in self:
            if self.env.company.branch_not_used == True:
                rec.branch_not_used = True
            else:
                rec.branch_not_used = False


class AccountMoveLine(models.Model):
    _inherit = 'account.move.line'

    @api.model
    def default_get(self, default_fields):
        res = super(AccountMoveLine, self).default_get(default_fields)
        branch_id = False

        if self._context.get('branch_id') and not self.env.company.branch_not_used:
            branch_id = self._context.get('branch_id')
        elif self.env.user.branch_id and not self.env.company.branch_not_used:
            branch_id = self.env.user.branch_id.id
        res.update({'branch_id' : branch_id})
        return res

    branch_id = fields.Many2one('res.branch', string="Branch")
    branch_not_used = fields.Boolean(string="", compute='check_branch_not_used')

    @api.depends('company_id')
    def check_branch_not_used(self):
        for rec in self:
            if self.env.company.branch_not_used == True:
                rec.branch_not_used = True
            else:
                rec.branch_not_used = False

