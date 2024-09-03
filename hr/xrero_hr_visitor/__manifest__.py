# -*- coding: utf-8 -*-
{
    'name': "Human Resource - Company Visitors Pass",
    'version': '7.1.15',
    'category': 'Human Resources/Employees',
    'summary': """Company Visitors Pass & Details (Human Resource)""",
    'description': """
        HR Visitor Process module for company visit.
Tags:
company visitor
visitor process 
hr visitor process
visitor pass
visitor report
company visit
employee visitors
odoo visitor
visit company
pass print
    """,
    'author': "Probuse Consulting Service Pvt. Ltd.",
    'website': 'www.xrero.com',
    'images': ['static/description/icon.png'],
    'depends': ['hr'],
    'data': [
            'security/ir.model.access.csv',
            'security/security.xml',
            'datas/visitor_sequence.xml',
            'views/visitor_process.xml',
            'reports/visitor_report.xml',
            ],
    'installable': True,
    'application': False,
}

