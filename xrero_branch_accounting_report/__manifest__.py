# -*- coding: utf-8 -*-
{
    "name" : "Financial Reports For Branch Enterprise Edition Odoo",
    "version" : "14.0.0",
    "category" : "Accounting",
    'summary': 'Multiple Branch Management Multi Branch app Multiple Unit Operating unit branch Invoicing branch financial branch wise filter reports branch reports branch Accounting statement Financial branch Reports for single company with Multi Branches multi company',
    "description": """
      odoo multiple branch accounting reports multiple branch accounting reports multiple branch accounting enterprise reports
    """,
    "author": "Xrero",
    "website" : "https://www.xrero.com",
    "depends" : ['account', 'account_accountant', 'account_reports','branch'],
    "data": [
            'views/search_template_view.xml',
            ],
    'assets': {
        'web.assets_backend': [
            '/xrero_branch_accounting_report/static/src/js/custom_account_reports.js',
        ],
    },
    'qweb': [],
    "auto_install": False,
    "installable": True,
    "images":['static/description/icon.png'],
}
