{
    'name': 'Custom Account',
    'version': '1.0.0',
    'category': 'Account',
    'sequence': 1,
    'summary': 'Custom Account Odoo v17',
    'description': """Custom Account for Odoo v17""",
    'author': 'Xrero',
    'website': 'https://xrero.com/',
    'depends': ['account','purchase','base','project'],
    'data': [
        'views/account_view.xml'
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
