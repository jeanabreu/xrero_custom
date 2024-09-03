from odoo import fields, models, api

class pos_session(models.Model):
    _inherit="pos.session"

    def _get_pos_ui_pos_payment_method(self, params):
        payment_methods = super()._get_pos_ui_pos_payment_method(params)
        res = self.config_id.get_matched_payment_method(self.env.user.id)
        filtered_payment_methods = [payment_method for payment_method in payment_methods if payment_method['id'] and payment_method['id'] not in res]
        return filtered_payment_methods

