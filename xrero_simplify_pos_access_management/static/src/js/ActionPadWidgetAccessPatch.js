/** @odoo-module **/

import { patch } from "@web/core/utils/patch";
import { useService } from "@web/core/utils/hooks";
import { ActionpadWidget } from "@point_of_sale/app/screens/product_screen/action_pad/action_pad";

const { onWillStart, onMounted, useState } = owl;

patch(ActionpadWidget.prototype, {
  setup() {
    super.setup(...arguments);
    this.state = useState({
      isPaymentAvailable: false,
      isCustomerAvailable: false,
    });
    onWillStart(async () => {
      const res = await this.env.services.orm.call(
        "pos.config",
        "get_unified_valid_user",
        [
          this.pos.config.id,
          this.pos.user.id,
          ["hide_payment", "hide_customer"],
        ]
      );
      this.state.isPaymentAvailable = Boolean(res.hide_payment);
      this.state.isCustomerAvailable = Boolean(res.hide_customer);
    });

    onMounted(() => {
      if (!this.pos.config.module_pos_restaurant) {
        if (!this.state.isPaymentAvailable) {
          const $subpad = $(".subpads");
          $subpad.css("flex-flow", "wrap");
        }
        if (this.state.isPaymentAvailable && !this.state.isCustomerAvailable) {
          const $paymentButton = $(".button.pay.validation");
          $paymentButton.css("height", "100%");
        }
      }
    });
  },
});
