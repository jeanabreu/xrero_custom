/** @odoo-module **/

import { patch } from "@web/core/utils/patch";
import { useService } from "@web/core/utils/hooks";
import { PartnerListScreen } from "@point_of_sale/app/screens/partner_list/partner_list";

const { onWillStart, onMounted, useState } = owl;

patch(PartnerListScreen.prototype, {
  setup() {
    super.setup(...arguments);
    this.access = useState({
      isCreateAvailable: false,
      isSaveAvailable: false,
    });
    onWillStart(async () => {
      const res = await this.env.services.orm.call(
        "pos.config",
        "get_unified_valid_user",
        [
          this.pos.config.id,
          this.pos.user.id,
          ["hide_create_customer", "hide_save_customer"],
        ]
      );
      this.access.isCreateAvailable = Boolean(res.hide_create_customer);
      this.access.isSaveAvailable = Boolean(res.hide_save_customer);
    });
  },
});
