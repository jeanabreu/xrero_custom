# -*- coding: utf-8 -*-
{
    'name': 'Xrero Odoo 17 Accounting Excel Reports',
    'version': '17.0',
    'category': 'Invoicing Management',
    'summary': 'Accounting Excel Reports, Odoo Excel Reports, Odoo Accounting Excel Reports, Odoo Financial Reports, '
               'Accounting Reports In Excel For Odoo 17, Financial Reports in Excel, Odoo Account Reports',
    'description': 'Accounting Excel Reports, Odoo Excel Reports, Odoo Accounting Excel Reports, Odoo Financial Reports, '
               'Accounting Reports In Excel For Odoo 17, Financial Reports in Excel, Odoo Account Reports',
    'sequence': '5',
    'author': 'Xrero',
    'website': '',
    'depends': ['accounting_pdf_reports'],
    'images': ['static/description/icon.png'],
    'demo': [],
    'data': [
        'security/ir.model.access.csv',
        'wizard/account_excel_reports.xml',
        'views/settings.xml',
        'report/report.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'assets': {
        "web.assets_backend": [
            "accounting_excel_reports/static/src/js/action_manager_report.esm.js",
        ],
    },
}
