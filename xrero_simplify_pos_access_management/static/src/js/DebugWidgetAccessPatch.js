/** @odoo-module **/

import { patch } from "@web/core/utils/patch";
import { DebugWidget } from "@point_of_sale/app/debug/debug_widget";

const { onWillStart, useState } = owl;

patch(DebugWidget.prototype, {
  setup() {
    super.setup(...arguments);
    this.access = useState({ debugWidgetIsShown: false });
    onWillStart(async () => {
      const res = await this.env.services.orm.call(
        "pos.config",
        "get_unified_valid_user",
        [this.pos.config.id, this.pos.user.id, ["hide_debug_window"]]
      );
      this.access.debugWidgetIsShown = Boolean(res.hide_debug_window);
      this.state.isShown = this.access.debugWidgetIsShown && this.state.isShown;
    });
  },
  // showCashMoveButton() {
  //   const res = super.showCashMoveButton(...arguments);
  //   return res && this.access.isCashInAvailable;
  // },
});
