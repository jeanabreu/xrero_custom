# -*- coding: utf-8 -*-
{
    "name": "Car Repair and Automotive Service Maintenance Management Odoo App",
    "version": "17.0",
    "depends": ['base', 'sale', 'purchase', 'account', 'sale_stock', 'mail', 'product', 'stock', 'fleet','sale_management', 'website', 'calendar', 'hr_timesheet','web'],
    "author": "Xrero",
    "summary": "Fleet repair vehicle repair car Maintenance auto-fleet service repair Car Maintenance Repair workshop automobile repair Automotive Service repair Automotive repair machine repair workshop equipment repair service Repair auto repair shop Auto Shop repair",
    "description": """
    BrowseInfo developed a new odoo/OpenERP module apps.
    This module use for autorepair industry , workshop management, Car Repair service industry, Spare parts industry. Fleet repair management. Vehicle Repair shop, Mechanic workshop, Mechanic repair software.Maintenance and Repair car. Car Maintenance Spare Part Supply. Car Servicing, Auto Servicing, Auto mobile Service, Bike Repair Service. Maintenance and Operation.Car Maintenance Repair management module helps to manage repair order, repair diagnosis, Diagnosis report, Diagnosis analysis, Quote for Repair, Invoice for Repair, Repair invoice, Repair orders, Workorder for repair, Fleet Maintenance.
    product repair, car workshop management, auto workshop management, repair workshop, workorder for product, 
    automotive workshop management software
    """,
    'category': 'Industries',
    "website": "https://www.xrero.com",
    "data": [
        'security/fleet_repair_security.xml',
        'security/ir.model.access.csv',
        'data/data.xml',
        'data/mail_template_data.xml',
        'wizard/fleet_repair_assign_to_head_tech_view.xml',
        'wizard/fleet_diagnose_assign_to_technician_view.xml',
        'views/fleet_repair_view.xml',
        'views/fleet_repair_service_checklist_view.xml',
        'views/fleet_repair_sequence.xml',
        'views/fleet_diagnose_view.xml',
        'views/fleet_workorder_sequence.xml',
        'views/fleet_workorder_view.xml',
        'views/custom_sale_view.xml',
        'views/calendar_event_view.xml',
        'views/appointment_slots_views.xml',
        'views/dashboard.xml',
        'views/templates.xml',
        'report/fleet_repair_label_view.xml',
        'report/fleet_repair_label_menu.xml',
        'report/fleet_repair_receipt_view.xml',
        'report/fleet_repair_receipt_menu.xml',
        'report/fleet_repair_checklist_view.xml',
        'report/fleet_repair_checklist_menu.xml',
        'report/fleet_diagnostic_request_report_view.xml',
        'report/fleet_diagnostic_request_report_menu.xml',
        'report/fleet_diagnostic_result_report_view.xml',
        'report/fleet_diagnostic_result_report_menu.xml',
        'report/fleet_workorder_report_view.xml',
        'report/fleet_workorder_report_menu.xml',
    ],
    'assets': {
        'web.assets_frontend': [
            'xrero_car_repair_industry/static/src/css/custom.css',
            'xrero_car_repair_industry/static/src/js/slot_time.js',
        ],
        'web.assets_backend': [
            'xrero_car_repair_industry/static/src/js/fleet_repair_dashboard.js',
            'xrero_car_repair_industry/static/src/xml/**/*',
        ],
    },
    'qweb': [
    ],
    "auto_install": False,
    "installable": True,
    "images": ['static/description/icon.png'],
}
