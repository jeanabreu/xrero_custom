/** @odoo-module **/

import { patch } from "@web/core/utils/patch";
const MobileOrderWidget = require("point_of_sale.MobileOrderWidget");

const { onWillStart, useState } = owl;

patch(MobileOrderWidget.prototype, {
  setup() {
    super.setup(...arguments);
    this.state = useState({ isPaymentAvailable: false });
    onWillStart(async () => {
      const res = await this.env.services.rpc({
        model: "pos.config",
        method: "get_unified_valid_user",
        args: [this.pos.config.id, this.pos.user.id, ["hide_payment"]],
      });
      this.state.isPaymentAvailable = Boolean(res.hide_payment);
    });
  },
});
