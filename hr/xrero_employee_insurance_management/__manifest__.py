# -*- coding: utf-8 -*-
{
    'name':'Employee Insurance Management',
    'version':'5.2.6',
    'category': 'Human Resources',
    'summary': 'This app allow you to manage Insurance of your Employees.',
    'description': """
Employees
Employee Insurance
Health Insurance
Insurance odoo
Insurance Management Systems
Insurance providers
Insurance provider
Insurance
user Insurance
    """,
    'website': 'http://www.xrero.com',
    'images': ['static/description/icon.png'],
    'depends': [
        'hr',
    ],
    'data':[
        'data/employee_insurance_policy_expire.xml',
        'data/employee_insurance_policy_reminder.xml',
        'security/insurance_security.xml',
        'security/ir.model.access.csv',
        'wizard/policy_renew.xml',
        'views/employee_insurance.xml',
        'views/insurance_property.xml',
        'views/employee_view.xml',
        'views/res_config_settings_view.xml',
        'report/insurance.xml',
    ],
    'installable': True,
    'application': False,
}
