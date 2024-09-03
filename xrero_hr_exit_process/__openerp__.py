# -*- coding: utf-8 -*-
{
    'name': 'Xrero HR Exit Process Management',
    'version': '4.1.7',
    'images': ['static/description/icon.png'],
    # 'live_test_url': 'https://youtu.be/WxKofWvXqjk',
    'category': 'Human Resources/Employees',
    'summary': 'Employee Out/Exit/Termination Process Management',
    'description': """
        Employee Exit process:
            ---> Configure CheckLists
            ---> Employee Exit Request
            ---> Employee Exit Checklists
            ---> Print Employee Exit Report 

Tags:
exit process
employee exit process
employee termination process
employee leave process
employee leave company
employee exit company
hr exit process
human resource exit process
checklist for exit process
Termination terminate
            """,
    'author': 'Probuse Consulting Service Pvt. Ltd.',
    'website': 'www.xrero.com',
    'depends': ['hr', 'hr_contract', 'survey', 'calendar'],
    'data': [
            'security/hr_exit_security.xml',
            'security/ir.model.access.csv',
            'views/hr_exit_view.xml',
            'report/hr_exit_process_report.xml',
             ],
    'installable': True,
    'application': False,
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
