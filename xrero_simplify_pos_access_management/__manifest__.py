{
    "name": "Simplify POS access rights",
    "version": "17.0",
    "sequence": 5,
    "author": "Xrero",
    "category": "Extra Tools",
    "website": "https://www.xrero.com",
    "description": """
        All In One POS Access Management App for setting the correct access rights for various pos features like related to order, product, customer, payment etc. 
        pos cashier access rights, pos manager access,pos cashier access, pos waiter access, pos floor access, pos category access,
        userwise pos access rights.
    """,
    "summary": """All In One POS Access Management App for setting the correct access rights for various pos features like related to order, product, customer, payment etc.
        All in one pos access management App. 
        """,
    "depends": ["point_of_sale", "pos_sale"],
    "data": [
        "security/res_groups.xml",
        "security/ir.model.access.csv",
        "views/point_of_sale_access_view.xml",
    ],
    "assets": {
        "point_of_sale._assets_pos": [
            "xrero_simplify_pos_access_management/static/src/js/ActionPadWidgetAccessPatch.js",
            "xrero_simplify_pos_access_management/static/src/js/DebugWidgetAccessPatch.js",
            "xrero_simplify_pos_access_management/static/src/js/PartnerListScreenAccessPatch.js",
            "xrero_simplify_pos_access_management/static/src/js/TicketScreenAccessPatch.js",
            "xrero_simplify_pos_access_management/static/src/js/NumpadWidgetAccessPatch.js",
            "xrero_simplify_pos_access_management/static/src/js/NavbarAccessPatch.js",
            "xrero_simplify_pos_access_management/static/src/js/ProductAccessPatch.js",
            "xrero_simplify_pos_access_management/static/src/js/PaymentScreenAccessPatch.js",
            "xrero_simplify_pos_access_management/static/src/js/PosActionButtonAccessPatch.js",
            "xrero_simplify_pos_access_management/static/src/js/ProductWidgetAccessPatch.js",
            "xrero_simplify_pos_access_management/static/src/xml/DebugWidgetAccessPatch.xml",
            "xrero_simplify_pos_access_management/static/src/xml/NavbarAccessPatch.xml",
            "xrero_simplify_pos_access_management/static/src/xml/ActionPadWidgetAccessPatch.xml",
            "xrero_simplify_pos_access_management/static/src/xml/PartnerListScreenAccessPatch.xml",
            "xrero_simplify_pos_access_management/static/src/xml/ProductAccessPatch.xml",
            "xrero_simplify_pos_access_management/static/src/xml/NumpadWidgetAccessPatch.xml",
            "xrero_simplify_pos_access_management/static/src/xml/PaymentScreenAccessPatch.xml",
            "xrero_simplify_pos_access_management/static/src/xml/PaymentValidateAccessPatch.xml",
            "xrero_simplify_pos_access_management/static/src/xml/PosActionButtonAccessPatch.xml",
        ]
    },
    "installable": True,
    "application": True,
    'images': ['static/description/icon.png'],
}
