/** @odoo-module **/

import { patch } from "@web/core/utils/patch";
import { useService } from "@web/core/utils/hooks";
const HeaderButton = require("point_of_sale.HeaderButton");

const { onWillStart, onMounted, useState } = owl;

patch(HeaderButton.prototype, {
  setup() {
    super.setup(...arguments);
    this.state = useState({ isCloseAvailable: false });
    onWillStart(async () => {
      const res = await this.env.services.rpc({
        model: "pos.config",
        method: "get_unified_valid_user",
        args: [this.pos.config.id, this.pos.user.id, ["hide_close"]],
      });
      this.state.isCloseAvailable = Boolean(res.hide_close);
    });
  },
});
