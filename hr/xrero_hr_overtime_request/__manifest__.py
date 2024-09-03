# -*- coding: utf-8 -*-
{
    'name' : 'Employee Overtime Request',
    'version': '5.3.8',
    'category' : 'Human Resources/Employees',
    'images': ['static/description/icon.png'],
    'website': 'https://www.xrero.com',
    'summary': 'Employee Overtime Request and Multiple Overtime Request.',
    'description': ''' 
This module add below features which can be used to manage overtime requests:
  * Overtime Requests: This will be request by employee.
  * Multiple Overtime Requests: This request can be created by HR Manager or Department Manager on behalf of multiple employees together.

Note: This module add new group called "Department Manager(Overtime)" under Usability group.
Menus:
Human Resources/Overtimes
Human Resources/Overtimes/Overtime Requests
Human Resources/Overtimes/Overtime Requests to Approve
Human Resources/Overtimes/Overtime Requests to Approve By Department
Human Resources/Multiple Overtimes
Human Resources/Multiple Overtimes/Multiple Overtime Requests
Human Resources/Multiple Overtimes/Multiple Requests to Approve
Human Resources/Multiple Overtimes/Multiple Requests to Approve By Department
  ''',
    'depends':['hr', 
                'portal',
               #'hr_payroll', 
               # 'portal',
               ],
    'data' : [
              'security/overtime_security.xml',
              'security/ir.model.access.csv',
              'views/hr_overtime_view.xml',
              'views/hr_overtime_multiple_view.xml',
              'views/hr_view.xml',
              #'data/ot_salary_rule_data.xml',
              
              ],
    'installable':True,
    'auto_install':False

}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
