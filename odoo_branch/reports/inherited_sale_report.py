# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models


class SaleReport(models.Model):
    _inherit = "sale.report"

    branch_id = fields.Many2one('res.branch')

    # def _query(self, with_clause='', fields={}, groupby='', from_clause=''):
    #     res =  super(SaleReport, self)._query(with_clause, fields, groupby, from_clause)
    #     index = res.find('pos.user_id AS user_id,')
    #     final_string = res[:index] + 'pos.branch_id as branch_id, ' + res[index:]
    #     index = final_string.find('pos.partner_id,')
    #     final_string = final_string[:index] + 'pos.branch_id,' + final_string[index:]
    #
    #     index = final_string.find('s.user_id as user_id,')
    #     final_string = final_string[:index] + 's.branch_id as branch_id, ' + final_string[index:]
    #     index = final_string.find('s.user_id,')
    #     final_string = final_string[:index] + 's.branch_id,' + final_string[index:]
    #
    #     return final_string



    def _query(self, with_clause='', fields={}, groupby='', from_clause=''):
        res =  super(SaleReport, self)._query(with_clause, fields, groupby, from_clause)
        index = res.find('s.user_id as user_id,')
        final_string = res[:index] + 's.branch_id as branch_id, ' + res[index:]
        index = final_string.find('s.user_id,')
        final_string = final_string[:index] + 's.branch_id,' + final_string[index:]
        return final_string
