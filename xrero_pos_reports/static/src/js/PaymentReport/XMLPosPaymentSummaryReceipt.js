/** @odoo-module */

import { usePos } from "@point_of_sale/app/store/pos_hook";
import {Component } from "@odoo/owl";

export class XMLPosPaymentSummaryReceipt extends Component {
    static template = "xrero_pos_reports.XMLPosPaymentSummaryReceipt";
    
    setup() {
        this.pos = usePos();
        
    }
    
}

