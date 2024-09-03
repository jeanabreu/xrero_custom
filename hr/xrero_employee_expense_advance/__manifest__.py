# -*- coding: utf-8 -*-

# Part of Probuse Consulting Service Pvt Ltd. See LICENSE file for full copyright and licensing details.

{
    'name': 'Expense Advance Request - Employee',
    'version': '9.9.1',
    'category': 'Human Resources',
    'summary': 'Allow employee to request expense in advance.',
    'description': """
        Employee Advance Expense Requests:
Expense Advance Request - Employee
Expense Advance
lary

            """,
    'images': ['static/description/icon.png'],
    'website': 'www.xrero.com',
    'depends': ['hr_expense'],
    'data': ['security/employee_advance_expense_security.xml',
             'security/ir.model.access.csv',
             'data/expense_sequence_data.xml',
             'views/employee_advance_expense.xml',
             'views/hr_expense.xml',
             'views/advance_expense_sheet.xml',
             'report/employee_advance_expense_report.xml'
             ],
    'installable': True,
    'application': False,
}
