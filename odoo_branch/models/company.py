# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _


class Comapny(models.Model):
    _inherit = 'res.company'

    branch_not_used = fields.Boolean(string="Branch Not Used",  )