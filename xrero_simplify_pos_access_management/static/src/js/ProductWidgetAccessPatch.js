/** @odoo-module **/

import { patch } from "@web/core/utils/patch";
import { useService } from "@web/core/utils/hooks";
import { ProductsWidget } from "@point_of_sale/app/screens/product_screen/product_list/product_list";

const { onWillStart, useState } = owl;

patch(ProductsWidget.prototype, {
  setup() {
    super.setup();
    this.access = useState({
      removableCategories: [],
    });
    onWillStart(async () => {
      const res = await this.env.services.orm.call(
        "pos.config",
        "get_matched_category",
        [{}, this.pos.config.id, this.pos.user.id]
      );
      this.access.removableCategories = res;
    });
  },

  getCategories() {
    const data = super.getCategories();
    const filteredData = data.filter(
      (ele) => !this.access.removableCategories.includes(ele.id)
    );
    if (filteredData.length == 1) {
      this.pos.setSelectedCategoryId(0);
    }
    return filteredData;
  },

  get productsToDisplay() {
    const data = super.productsToDisplay;
    const filteredData = data.filter((ele) => !ele.pos_categ_ids.some((el) => this.access.removableCategories.includes(el)))
    return filteredData;
  },
});
