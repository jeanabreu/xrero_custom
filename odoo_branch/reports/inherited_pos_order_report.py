# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models


class ReportPosOrder(models.Model):
    _inherit = "report.pos.order"

    branch_id = fields.Many2one('res.branch')

    def _select(self):
        return super(ReportPosOrder, self)._select() + ',s.branch_id AS branch_id'

    def _group_by(self):
        return super(ReportPosOrder, self)._group_by() + ',s.branch_id'
