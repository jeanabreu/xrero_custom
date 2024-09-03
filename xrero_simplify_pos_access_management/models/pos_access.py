from odoo import models, fields,api

class pos_access(models.Model):
    _name = 'pos.access'
    _description = 'POS Access Domain'

    pos_config_ids = fields.Many2many('pos.config', 'pos_access_config_rel', 'pos_access_id', 'pos_config_id', string='Pos Shop', required=True)
    name = fields.Char('Name', required=True)
    user = fields.Many2many('res.users', 'pos_access_user_rel', 'pos_access_id', 'user_id')
    active = fields.Boolean(string="Is rule active", default=True)

    hide_close = fields.Boolean('Hide close POS button', help='Select this option to hide close button from POS screen')
    # restrict_pos = fields.Boolean('Hide selected POS', help='Select this option to hide selected POS for user')
    hide_cash_in = fields.Boolean('Hide cash in/out POS button', help='Select this option to hide cash in/out button from POS screen')
    hide_debug_window = fields.Boolean('Hide debug window', help='Select this option to hide debug window from POS screen')

    hide_delete_order = fields.Boolean('Hide delete order button', help='Select this option to hide delete order button from orders screen')
    only_show_active_order = fields.Boolean('Only show active order', help='Select this option to hide filter option from orders screen')
    hide_create_order = fields.Boolean('Hide create order button', help='Select this option to hide new order button from orders screen')

    hide_customer = fields.Boolean('Hide customer button', help='Select this option to hide customer button from order screen')
    hide_create_customer = fields.Boolean('Hide create customer button', help='Select this option to create customer payment button from customer screen')
    hide_save_customer = fields.Boolean('Hide save customer button', help='Select this option to hide save button from customer screen')
    
    hide_numpad = fields.Boolean('Hide numpad buttons', help='Select this option to hide whole numpad from order screen')
    hide_price = fields.Boolean('Disable price button', help='Select this option to disable price button from order screen')
    hide_qty = fields.Boolean('Disable qty button', help='Select this option to disable qty  button from order screen')
    hide_discount = fields.Boolean('Disable discount button', help='Select this option to disable dicount button from order screen')
    hide_plus_minus = fields.Boolean("Disable '(+/-)' button", help='Select this option to Disable (+/-) button from order screen')

    hide_payment = fields.Boolean('Hide payment button', help='Select this option to hide payment button from order screen')
    hide_payment_customer_button = fields.Boolean("Hide payment customer button", help='Select this option to hide customer button from payment screen')
    hide_payment_validate_button = fields.Boolean("Hide payment validate button", help='Select this option to hide customer button from payment screen')
    hide_payment_ship_later_button = fields.Boolean("Hide payment ship later button", help='Select this option to hide sip later button from payment screen')
    hide_payment_invoice_button = fields.Boolean("Hide payment invoice button", help='Select this option to hide invoice button from payment screen')
    hide_payment_tip_button = fields.Boolean("Hide payment tip button", help='Select this option to hide customer tip from payment screen')
    
    hide_customer_note_button = fields.Boolean("Hide customer note button", help='Select this option to hide customer note from product screen')
    hide_refund_button = fields.Boolean("Hide refund button", help='Select this option to hide refund from product screen')
    hide_save_button = fields.Boolean("Hide save button", help='Select this option to hide save from product screen')
    hide_quotation_button = fields.Boolean("Hide quotation button", help='Select this option to hide quotation from product screen')
    hide_fiscal_button = fields.Boolean("Hide fiscal button", help='Select this option to hide fiscal from product screen')
    hide_price_list_button = fields.Boolean("Hide price list button", help='Select this option to hide price list from product screen')

    pos_payment_method_ids = fields.Many2many("pos.payment.method", "pos_access_payment_method_rel", "pos_access_id", "pos_payment_method_id", string="Restrict payment method", help='Select the payment method you want to restrict for selected user')
    pos_category_ids = fields.Many2many('pos.category', 'pos_access_rel', 'pos_access_id', 'pos_category_id', string="Restrict pos categories", help='Select the categories you want to restrict for selected user')

    # def read(self, fields, load='_classic_read'):
    #     result = super().read(fields=fields, load=load)
    #     return result

    def toggle_active_value(self):
        res = self.write({"active": not self.active})
        return res
