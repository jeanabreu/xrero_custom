# -*- coding: utf-8 -*-

# Part of Probuse Consulting Service Pvt Ltd. See LICENSE file for full copyright and licensing details.

{
    'name': 'Employee Advance Salary Requests',
    'version': '7.5.1',
    'category': 'Human Resources',
    'summary': 'Employee Advance Salary Requests and Workflow - Integrated with Accounting',
    'description': """
Employee Advance Salary Requests:
Employee advance salary
Employee advance salary request
            """,
    'author': 'Probuse Consulting Service Pvt. Ltd.',
    'website': 'www.probuse.com',
    'depends': ['hr', 'account'],
    'images': ['static/description/icon.png'],
    'data': ['security/employee_advance_salary_security.xml',
             'security/ir.model.access.csv',
             # 'data/salary_rule_data.xml',
             'views/employee_advance_salary.xml',
             'views/hr_job.xml',
             'report/employee_advance_salary_report.xml'
             ],
    'demo': [
       'data/salary_rule_data.xml'
    ],
    'installable': True,
    'application': False,
}
