# -*- coding: utf-8 -*-
{
    'name': 'Xrero Theme Common',
    'description': 'Xrero Theme Common',
    'category': 'eCommerce',
    'version': '17.0',
    'depends': [
        'sale_product_configurator',
        'website_sale_comparison',
        'website_sale_wishlist',
        'website_sale_stock',
        'website_sale_stock_wishlist',
    ],
    'website': 'https://www.xrero.com/',
    'data': [
        'security/ir.model.access.csv',
        'deprecated/ir.model.access.csv',
        'views/templates.xml',
        # Backend
        'views/backend/menu_label.xml',
        'views/backend/website_menu.xml',
        'views/backend/product_label.xml',
        'views/backend/product_template.xml',
        'views/backend/product_attribute.xml',
        'views/backend/product_brand.xml',
        'views/backend/dr_website_content.xml',
        'views/backend/product_pricelist.xml',
        'views/backend/pwa_screenshots.xml',
        'views/backend/pwa_shortcuts.xml',
        'views/backend/res_config_settings.xml',
        'views/backend/dr_theme_config.xml',
        'views/backend/category_label.xml',
        'views/backend/product_category.xml',
        'views/backend/website.xml',
        'views/backend/search_report.xml',
        'data/search_report_cron.xml',
        # Snippets
        'views/snippets/s_mega_menu.xml',
    ],
    'images': [
        'static/description/icon.png',
    ],
    'assets': {
        'web.assets_backend': [
            'droggol_theme_common/static/src/js/components/*.xml',
            'droggol_theme_common/static/src/js/hooks.js',
        ],
        'website.assets_editor': [
            'droggol_theme_common/static/src/js/components/*.js',
            'droggol_theme_common/static/src/js/components/*.scss',
            'droggol_theme_common/static/src/js/navbar/*.js',
        ]
    },
}
