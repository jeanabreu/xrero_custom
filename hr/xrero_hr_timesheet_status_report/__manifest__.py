# -*- coding: utf-8 -*-
{
    'name': 'Timesheet Incomplete Report Employees',
    'version': '8.2.4',
    'category': 'Services/Timesheets',
    'summary': 'This app allow you to print timesheet incomplete report and cron job allow to auto send weekly.',
    'description': """
incomplete timesheet
missing timesheet
not complete timesheet
Pending time sheet report (Frequency every week) : 
Report to be emailed to HR Manager and hierarchy of all managers. Better we can select and set default all followers who received.
If employee weekly timesheet not filled or not validated it will weekly report generated and send to managers
This module allows Timesheet Manager to print Timesheet Report.
Timesheet Employee Weekly Report
print Timesheet PDF Report
Timesheet Report PDF
Timesheet QWEB Report
This module allows Timesheet Manager to print Weekly Timesheet Report.
week timesheet
weekly timesheet
employee timesheet
employee week timesheet
employee weekly timesheet
timesheet pdf report
timesheet report
customer timesheet report
Timesheet Incomplete Report Employees

Notification Report Managers List

Cron Job to Send Report Weekly to All Managers Configured on Company Settings


customer timesheet
timesheet employee pdf
employee print timesheet
* INHERIT res.company.form.timesheet.followers (form)
HR Timesheet Report Form View (form)
report_hr_timesheet (qweb)
print odoo timesheet
probuse
timesheet
timesheet pdf report
weekly
week
timesheet week
analytic line
hr timesheet sheet
timesheet by project
timesheet line by project
timesheet line on project
project on timesheet
timesheet sheet
timesheet sheet employee
timesheet report to customer
timesheet activities
my timesheet
                    """,
    'website': 'http://www.xrero.com',
    'support': 'contact@probuse.com',
    'images': ['static/description/icon.png'],
    'depends': [
        'hr_timesheet_attendance',
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/company_views.xml',
        'report/report_hr_timesheet.xml',
        'data/timesheet_reminder_data.xml',
        'wizard/hr_timesheet_report_wizard.xml',
    ],
    'installable': True,
    'application': False,
}
