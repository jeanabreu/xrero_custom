/** @odoo-module **/

import { patch } from "@web/core/utils/patch";
import { OrderlineCustomerNoteButton } from "@point_of_sale/app/screens/product_screen/control_buttons/customer_note_button/customer_note_button";
// const ProductInfoButton = require("point_of_sale.ProductInfoButton");
import { RefundButton } from "@point_of_sale/app/screens/product_screen/control_buttons/refund_button/refund_button";
import { SaveButton } from "@point_of_sale/app/screens/product_screen/control_buttons/save_button/save_button";
import { SetFiscalPositionButton } from "@point_of_sale/app/screens/product_screen/control_buttons/fiscal_position_button/fiscal_position_button";
import { SetPricelistButton } from "@point_of_sale/app/screens/product_screen/control_buttons/pricelist_button/pricelist_button";
import { SetSaleOrderButton } from "@pos_sale/app/set_sale_order_button/set_sale_order_button";

const { onWillStart, useState } = owl;

patch(OrderlineCustomerNoteButton.prototype, {
  setup() {
    super.setup(...arguments);
    this.access = useState({
      isCustomerAvaliable: false,
    });
    onWillStart(async () => {
      const res = await this.env.services.orm.call(
        "pos.config",
        "get_unified_valid_user",
        [this.pos.config.id, this.pos.user.id, ["hide_customer_note_button"]]
      );
      this.access.isCustomerAvaliable = Boolean(res.hide_customer_note_button);
    });
  },
});

patch(SaveButton.prototype, {
  setup() {
    super.setup(...arguments);
    this.access = useState({
      isSaveAvailable: false,
    });
    onWillStart(async () => {
      const res = await  await this.env.services.orm.call(
        "pos.config",
        "get_unified_valid_user",[this.pos.config.id, this.pos.user.id, ["hide_save_button"]],
      );
      this.access.isSaveAvailable = Boolean(res.hide_save_button);
    });
  },
});

patch(RefundButton.prototype, {
  setup() {
    super.setup(...arguments);
    this.access = useState({
      isRefundAvailable: false,
    });
    onWillStart(async () => {
      const res = await this.env.services.orm.call(
        "pos.config",
        "get_unified_valid_user",
        [this.pos.config.id, this.pos.user.id, ["hide_refund_button"]]
      );
      this.access.isRefundAvailable = Boolean(res.hide_refund_button);
    });
  },
});

patch(SetFiscalPositionButton.prototype, {
  setup() {
    super.setup(...arguments);
    this.access = useState({
      isFiscalAvailable: false,
    });
    onWillStart(async () => {
      const res = await this.env.services.orm.call(
        "pos.config",
        "get_unified_valid_user",
        [this.pos.config.id, this.pos.user.id, ["hide_fiscal_button"]]
      );
      this.access.isFiscalAvailable = Boolean(res.hide_fiscal_button);
    });
  },
});

patch(SetPricelistButton.prototype, {
  setup() {
    super.setup(...arguments);
    this.access = useState({
      isPriceListAvailable: false,
    });
    onWillStart(async () => {
      const res = await this.env.services.orm.call(
        "pos.config",
        "get_unified_valid_user",
        [this.pos.config.id, this.pos.user.id, ["hide_price_list_button"]]
      );
      this.access.isPriceListAvailable = Boolean(res.hide_price_list_button);
    });
  },
});

patch(SetSaleOrderButton.prototype, {
  setup() {
    super.setup(...arguments);
    this.access = useState({
      isQuotationAvailable: false,
    });
    onWillStart(async () => {
      const res = await this.env.services.orm.call(
        "pos.config",
        "get_unified_valid_user",
        [this.pos.config.id, this.pos.user.id, ["hide_quotation_button"]]
      );
      this.access.isQuotationAvailable = Boolean(res.hide_quotation_button);
    });
  },
});
