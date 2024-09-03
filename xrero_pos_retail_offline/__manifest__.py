# -*- coding: utf-8 -*
{
    "name": "POS Offline (Resume Session Offline) - Retail and Restaurant",
    "version": "1.0.3",
    "category": "Point of Sale",
    "author": "Xrero",
    "summary":
        """
        Point Of Sale Offline Mode\n
        Allow Sale Products, create Orders without Internet and Odoo Server \n
        Allow Reload, Refresh POS Page  without Internet and Odoo Server\n
        Allow Resume POS Session without Internet and Odoo Server
        """,
    "description":
        """
        Point Of Sale Offline Mode\n
        Allow Sale Products, create Order without Internet and Odoo Server \n
        Allow Reload, Refresh POS Page  without Internet and Odoo Server\n
        Allow Resume POS Session without Internet and Odoo Server
        """,
    "website": "http://xrero.com",
    "sequence": 0,
    "depends": [
        "point_of_sale",
        "pos_hr",
        "pos_restaurant",
    ],
    "demo": [],
    "data": [
        "import_libraries.xml"
    ],
    "currency": "EUR",
    "installable": True,
    "application": True,
    "images": ["static/description/icon.png"],
    "support": "thanhchatvn@gmail.com",
    "license": "OPL-1",
    "assets": {
        "point_of_sale._assets_pos": [
            "xrero_pos_retail_offline/static/src/apps/idb-keyval.js",
            "xrero_pos_retail_offline/static/src/apps/PosIDB.js",
            "xrero_pos_retail_offline/static/src/apps/models.js",
            "xrero_pos_retail_offline/static/src/apps/webClient.js",
        ],
        'web.assets_backend': [

        ],
    },
}
