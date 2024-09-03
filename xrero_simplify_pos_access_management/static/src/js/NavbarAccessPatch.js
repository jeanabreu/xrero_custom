/** @odoo-module **/

import { patch } from "@web/core/utils/patch";
import { Navbar } from "@point_of_sale/app/navbar/navbar";

const { onWillStart, useState } = owl;

patch(Navbar.prototype, {
  setup() {
    super.setup(...arguments);
    this.access = useState({
      isCashInAvailable: false,
      isCloseAvailable: false,
      isDebugAvailable: false,
    });
    onWillStart(async () => {
      const res = await this.env.services.orm.call(
        "pos.config",
        "get_unified_valid_user",
        [this.pos.config.id, this.pos.user.id, ["hide_cash_in", "hide_close", "hide_debug_window"]]
      );
      this.access.isCashInAvailable = Boolean(res.hide_cash_in);
      this.access.isCloseAvailable = Boolean(res.hide_close);
      this.access.isDebugAvailable = Boolean(res.hide_debug_window);
    });
  },

  get showCashMoveButton() {
    const res = super.showCashMoveButton;
    return res && this.access.isCashInAvailable;
  },
});
