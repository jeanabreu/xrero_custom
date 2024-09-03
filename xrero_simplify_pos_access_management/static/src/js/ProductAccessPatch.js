/** @odoo-module **/

import { patch } from "@web/core/utils/patch";
import { useService } from "@web/core/utils/hooks";
import { ProductScreen } from "@point_of_sale/app/screens/product_screen/product_screen";
import { usePos } from "@point_of_sale/app/store/pos_hook";

const { onWillStart, onMounted, useState } = owl;

patch(ProductScreen.prototype, {
  setup() {
    super.setup(...arguments);
    this.pos = usePos();
    this.state = useState({
      isPaymentAvailable: false,
      isPriceAvailable: false,
      isDiscountAvailable: false,
      isPlusMinusAvailable: false,
      isQtyAvailable: false,
    });

    onWillStart(async () => {
      const res = await this.env.services.orm.call(
        "pos.config",
        "get_unified_valid_user",
        [
          this.pos.config.id,
          this.pos.user.id,
          ["hide_payment", "hide_price", "hide_discount", "hide_plus_minus", "hide_qty"],
        ]
      );
      this.state.isPaymentAvailable = Boolean(res.hide_payment);
      this.state.isPriceAvailable = Boolean(res.hide_price);
      this.state.isDiscountAvailable = Boolean(res.hide_discount);
      this.state.isPlusMinusAvailable = Boolean(res.hide_plus_minus);
      this.state.isQtyAvailable = Boolean(res.hide_qty);

      if (!this.state.isQtyAvailable) {
        if (this.state.isPriceAvailable) this.onNumpadClick("price");
        else if (this.state.isDiscountAvailable) {
          this.onNumpadClick("discount");
        }
      }
    });

    onMounted(() => {
      if(!this.state.isPaymentAvailable && this.ui.isSmall) {
        $(".switchpane.d-flex").find(".review-button").attr('style', 'width: 100% !important');
        ;
      }
    })
  },

  getNumpadButtons() {
    let data = super.getNumpadButtons();
    if (!this.state.isQtyAvailable) {
      if (this.state.isPriceAvailable) this.onNumpadClick("price");
      else if (this.state.isDiscountAvailable) {
        this.onNumpadClick("discount");
      }
    }
    return data.map((ele) => {
      if(ele.value == "discount") {
        ele.disabled = ele.disabled || !this.state.isDiscountAvailable;
      }
      if(ele.value == "quantity") {
        ele.disabled = ele.disabled || !this.state.isQtyAvailable;
      }
      if(ele.value == "price") {
        ele.disabled = ele.disabled || !this.state.isPriceAvailable;
      }
      if(ele.value == "-") {
        ele.disabled = ele.disabled || !this.state.isPlusMinusAvailable;
      }
      return ele;
    })
  },
});
