# -*- coding: utf-8 -*-
{
    'name': 'POS ESC/POS Printer',
    'summary': 'POS ESC/POS Printer, ',
    'description': """Use Point of Sale TCP ESC/POS Printers Without an IoT Box""",
    'version': '17.0',
    'author': 'xrero',
    'website': "https://xrero.com",
    "category": "Point of Sale",
    'depends': ['point_of_sale'],
    'data': [
        'views/pos_config_views.xml',
        'views/res_config_settings_views.xml',
        'views/pos_printer_views.xml',
    ],
    'images': ['static/description/icon.png'],
    'installable': True,
    'auto_install': False,
    'assets': {
        'point_of_sale._assets_pos': [
            'xrero_pos_tcp_esc_printer/static/src/**/*',
        ],
    },
}
