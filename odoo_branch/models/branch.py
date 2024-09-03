# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _


class ResBranch(models.Model):
    _name = 'res.branch'
    _description = 'Branch'

    name = fields.Char(required=True)
    company_id = fields.Many2one('res.company', required=True)
    telephone = fields.Char(string='Telephone No')
    address = fields.Text('Address')
    zip = fields.Char(change_default=True)
    invoice_address = fields.Many2one("res.partner", string="Invoice Address")
    delivery_address = fields.Many2one("stock.picking.type", string="Delivery Address")
