# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _


class StockWarehouse(models.Model):
    _inherit = 'stock.warehouse'

    branch_id = fields.Many2one('res.branch')
    branch_not_used = fields.Boolean(string="", compute='check_branch_not_used')

    @api.depends('company_id')
    def check_branch_not_used(self):
        for rec in self:
            if self.env.company.branch_not_used == True:
                rec.branch_not_used = True
            else:
                rec.branch_not_used = False


class StockPickingTypeIn(models.Model):
    _inherit = 'stock.picking.type'

    branch_id = fields.Many2one('res.branch',related='warehouse_id.branch_id', store=True,)

