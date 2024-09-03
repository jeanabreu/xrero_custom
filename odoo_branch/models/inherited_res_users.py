# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _


class ResUsers(models.Model):
    _inherit = 'res.users'

    branch_ids = fields.Many2many('res.branch',string="Allowed Branch")
    branch_id = fields.Many2one('res.branch', string= 'Branch')
    branch_not_used = fields.Boolean(string="",compute='check_branch_not_used'  )

    @api.depends('company_id')
    def check_branch_not_used(self):
        for rec in self:
            if self.env.company.branch_not_used == True:
                rec.branch_not_used = True
            else:
                rec.branch_not_used = False

    def write(self, values):
        if 'branch_id' in values or 'branch_ids' in values:
            self.env['ir.model.access'].call_cache_clearing_methods()
            self.env['ir.rule'].clear_caches()
            self.has_group.clear_cache(self)
        user = super(ResUsers, self).write(values)
        return user
