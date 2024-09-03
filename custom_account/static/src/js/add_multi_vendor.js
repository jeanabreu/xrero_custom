odoo.define('custom_purchase_order.action_add_multi_vendor', function (require) {
"use strict";

var core = require('web.core');
var ListController = require('web.ListController');
ListController.include({
   renderButtons: function($node) {
   this._super.apply(this, arguments);
       if (this.$buttons) {
         this.$buttons.find('.o_list_add_multi_vendor').click(this.proxy('action_add_multi_vendor'));
       }
    },

    action_add_multi_vendor: function (e) {
        var self = this;
        var model_name = this.model.get(this.handle).getContext()['active_model'];
            this._rpc({
                    model: 'vendor.settings',
                    method: 'js_python_method',
                    args: ["", model_name],
                }).then(function (result) {
                    self.do_action({
                        name: ("Add Multi Vendor"),
                        type: 'ir.actions.act_window',
                        res_model: 'add.multi.vendor.wizard',
                        view_mode: 'form',
                        views: [[false, 'form']],
                        target: 'new'
                    });
                });
   },
});
});