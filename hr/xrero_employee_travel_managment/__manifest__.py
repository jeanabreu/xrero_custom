# -*- coding: utf-8 -*-

# Part of Probuse Consulting Service Pvt Ltd. See LICENSE file for full copyright and licensing details.
{
    'name': "Employee Travel and Travel Expense Management",
    'summary': """This module allow you to manage travel of your employees.""",
    'description': """
    Employee Travel Management,
Travel Request,
Travel Request Confirmation,
Advance Payment Request,
Expenses
employee expense
Expenses Sheet
travel expense
expense advance
advance expense
This module will allow you to manage travel of your employees and expense advance and submit expense claim.
employee travelling
travel expense
travel employee
advance expense
advance salary

expense claim
expense employee
Employee Travel Expense Report
Employee Travel Expense QWEB
Employee Travel Expense PDF
Travel Expense
employee travel
employee travel management
travel app
travel module
employee location
Employee Travel Management

Created Menus :

Travel/Travel Request
Travel/Travel Request/Employee Travel Request
Travel/Travel Request/Travel Requests To Approve
Defined Reports

Travel Request
Workflow: Draft ->Confirmed -> Canceled -> Approved -> Rejected ->Returned ->Expenses Submitted

This module Manage Travel Request of the employee for the particular project.

""",
    'website': "www.xrero.com",
    'version': '7.36.3',
    'category' : 'Human Resources/Employees',
    'images' : ['static/description/icon.png'],
    'depends': ['hr','project','account','hr_expense'],
    'data':[
        'security/travel_request_security.xml',
        'security/ir.model.access.csv',
        'data/travel_sequence.xml',
        'views/travel_request_view.xml',
        'views/travel_request_report.xml',
    ],
    'installable' : True,
    'application' : False,
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
