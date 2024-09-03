/** @odoo-module **/

import { patch } from "@web/core/utils/patch";
import { useService } from "@web/core/utils/hooks";
import { TicketScreen } from "@point_of_sale/app/screens/ticket_screen/ticket_screen";
const { onWillStart, onMounted, useState } = owl;

patch(TicketScreen.prototype, {
  setup() {
    super.setup();
    this.access = useState({
      isDeleteAvailable: false,
      isFilterShown: false,
      isNewAvailable: false,
    });
    onWillStart(async () => {
      const res = await this.env.services.orm.call(
        "pos.config",
        "get_unified_valid_user",
        [
          this.pos.config.id,
          this.pos.user.id,
          [
            "hide_delete_order",
            "only_show_active_order",
            "only_show_active_order",
          ],
        ]
      );
      this.access.isDeleteAvailable = Boolean(res.hide_delete_order);
      this.access.isFilterShown = Boolean(res.only_show_active_order);
    });
  },

  shouldHideDeleteButton(order) {
    const res = super.shouldHideDeleteButton(...arguments);
    return !this.access.isDeleteAvailable || res;
  },

  getSearchBarConfig() {
    const res = super.getSearchBarConfig(...arguments);
    res.filter.show = this.access.isFilterShown;
    return res;
  },
});
