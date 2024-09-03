{
    "name": "Real estate | Property management",
    "version": '17.0.1.0.0',
    "category": "Real Estate",
    "sequence": 14,
    "summary": """
        This module allows you to manage the real estate project, sell and rental property contracts, and calculate broker commission and many more.
        Advanced Property Sale & Rental Management | Property Sales | Property Rental 
    """,
    "description": """ 
        This module allows you to manage the real estate project, sell and rental property contracts, and calculate broker commission and many more.
        Advanced Property Sale & Rental Management | Property Sales | Property Rental 
    """,
    "author": "Xrero",
    "website": "https://www.xrero.com",
    "depends": ["base", "account", "analytic", 'repair', 'sale_management', 'web'],
    "data": [
        "data/ir_sequence.xml",
        'security/ir.model.access.csv',
        "views/view_account_invoice.xml",
        "views/view_attachment_line.xml",
        "views/view_crm_team.xml",
        "views/view_installment_template.xml",
        "views/view_product_category.xml",
        "views/view_project_worksite.xml",
        "views/view_property.xml",
        "views/view_property_contract.xml",
        "views/view_property_reservation.xml",
        "views/view_region.xml",
        "views/view_repair_order.xml",
        "views/view_res_config_settings.xml",
        "views/view_sale_order.xml",
        "views/view_sales_commission.xml",
        "views/menu_items.xml",
    ],
    "assets": {
        "web.assets_backend": [
            "xrero_real_estate_bits/static/src/libs/Chart.min.js",
            "xrero_real_estate_bits/static/src/xml/gmap.xml",
            # "xrero_real_estate_bits/static/src/js/init.js",
            # "xrero_real_estate_bits/static/src/js/map_widget.js",
            # "xrero_real_estate_bits/static/src/js/map_widget_multi.js",
            "xrero_real_estate_bits/static/src/js/place_autocomplete.js",
            # "xrero_real_estate_bits/static/src/js/place_autocomplete_multi.js",
            "xrero_real_estate_bits/static/src/xml/dashboard_view.xml",
            "xrero_real_estate_bits/static/src/xml/autocomplete.xml",
            "xrero_real_estate_bits/static/src/css/dashboard_view.css",
            "xrero_real_estate_bits/static/src/js/dashboard_view.js",
        ],
    },
    "images": ["static/description/icon.png"],
    "installable": True,
    "auto_install": False,
    "application": True,

}
