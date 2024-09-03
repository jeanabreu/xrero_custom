/** @odoo-module **/

import { patch } from "@web/core/utils/patch";
import { useService } from "@web/core/utils/hooks";
import { PaymentScreen } from "@point_of_sale/app/screens/payment_screen/payment_screen";
import { registry } from "@web/core/registry";

const { onWillStart, onMounted, useState } = owl;

patch(PaymentScreen.prototype, {
  setup() {
    super.setup();
    this.access = useState({
      isInvoiceAvailable: false,
      isTipAvailable: false,
      isShipLaterAvailable: false,
      isCustomerAvailable: false,
      isValidateAvailable: false,
    });
    onWillStart(async () => {
      const res = await this.env.services.orm.call(
        "pos.config",
        "get_unified_valid_user",
        [
          this.pos.config.id,
          this.pos.user.id,
          [
            "hide_payment_invoice_button",
            "hide_payment_ship_later_button",
            "hide_payment_customer_button",
            "hide_payment_validate_button",
            "hide_payment_tip_button",
          ],
        ]
      );
      this.access.isInvoiceAvailable = Boolean(res.hide_payment_invoice_button);
      this.access.isShipLaterAvailable = Boolean(
        res.hide_payment_ship_later_button
      );
      this.access.isCustomerAvailable = Boolean(
        res.hide_payment_customer_button
      );
      this.access.isValidateAvailable = Boolean(
        res.hide_payment_validate_button
      );
      this.access.isTipAvailable = Boolean(res.hide_payment_tip_button);
    });
  },
});
