/** @odoo-module **/

import { patch } from "@web/core/utils/patch";
import { useService } from "@web/core/utils/hooks";
import { Numpad } from "@point_of_sale/app/generic_components/numpad/numpad";
import { usePos } from "@point_of_sale/app/store/pos_hook";

const { onWillStart, useEffect, useState } = owl;

patch(Numpad.prototype, {
  setup() {
    super.setup(...arguments);
    this.pos = usePos();
    this.state = useState({
      isNumpadAvailable: false,
      // isPriceAvailable: false,
      // isDiscountAvailable: false,
      // isPlusMinusAvailable: false,
      // isQtyAvailable: false,
    });

    onWillStart(async () => {
      const res = await await this.env.services.orm.call(
        "pos.config",
        "get_unified_valid_user",
        [this.pos.config.id, this.pos.user.id, ["hide_numpad"]]
      );
      this.state.isNumpadAvailable = Boolean(res.hide_numpad);
      // this.state.isPriceAvailable = Boolean(res.hide_price);
      // this.state.isDiscountAvailable = Boolean(res.hide_discount);
      // this.state.isPlusMinusAvailable = Boolean(res.hide_plus_minus);
      // this.state.isQtyAvailable = Boolean(res.hide_qty);

      // if (!this.state.isQtyAvailable) {
      //   if (this.state.isPriceAvailable) this.props.onClick("price");
      //   else if (this.state.isDiscountAvailable) {
      //     this.props.onClick("discount");
      //   }
      // }
    });
  },
});
