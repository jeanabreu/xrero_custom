from odoo import models, fields,api

class pos_config(models.Model):
    _inherit = 'pos.config'

    pos_access_ids = fields.Many2many('pos.access', 'pos_access_config_rel', 'pos_config_id', 'pos_access_id', string='POS Access')

    # def read(self, fields, load='_classic_read'):
    #     result = super().read(fields=fields, load=load)
    #     res = self.pos_access_ids.mapped("id")
    #     if res and len(res) < 0:
    #         return result
    #     arr = self.pos_access_ids.search([('id', 'in', res), ('active', '=', True), ('pos_config_ids', 'in', [self.id]), ('user', '=', self.env.user.id), ('restrict_pos', '=', True)]).mapped('pos_config_ids.id')
    #     filtered_pos_config = [pos_config for pos_config in result if pos_config['id'] and pos_config['id'] not in arr]
    #     return filtered_pos_config

    @api.model
    def get_unified_valid_user(self, config_id, user_id, fields):
        return_data = {}
        res = self.browse(config_id).pos_access_ids.mapped("id")
        for field in fields:
            if res and len(res) < 0:
                return_data[field] = True
                continue
            users_in_domain = self.browse(config_id).pos_access_ids.search([(field, '=', True), ('active', '=', True), ('pos_config_ids', 'in', [config_id])]).mapped('user.id')
            return_data[field] = user_id not in users_in_domain
        return return_data
    
    def get_matched_category(self, config_id, user_id):
        res = self.browse(config_id).pos_access_ids.mapped("id")
        if res and len(res) < 0:
            return []
        arr = self.pos_access_ids.search([('id', 'in', res), ('active', '=', True), ('pos_config_ids', 'in', [config_id]), ('user', '=', user_id)]).mapped('pos_category_ids.id')
        for i in arr:
            self.env['pos.category'].get_all_child_nodes(i, arr)
        return arr
    
    def get_matched_payment_method(self, user_id):
        res = self.pos_access_ids.mapped("id")
        if res and len(res) < 0:
            return []
        arr = self.pos_access_ids.search([('id', 'in', res), ('active', '=', True), ('user', '=', user_id)]).mapped('pos_payment_method_ids.id')
        return arr
