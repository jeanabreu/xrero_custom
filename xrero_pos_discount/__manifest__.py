# -*- coding: utf-8 -*-
{
    "name": "POS Discount Percentage and Fixed Amount in Odoo",
    "version": "17.0",
    "category": "Point of Sale",
    "depends": ['base', 'sale', 'point_of_sale'],
    "author": "Xrero",
    'summary': 'Point Of Sales discount on POS Discount Amount Display POS Discount Coupons POS Custom Discount pos fix discount pos offers POS Global Discount point of sales fixed POS global Discount on POS order Discount on POS Discount Coupons on pos',
    "description": """
    
    Purpose :-
	pos discount 
	point of sales discount 
	pos fixed discount
    odoo percentage discount on point of sale point of sale Global Discount point of sale custom discount point of sale discount
    """,
    "website": "https://www.xrero.com",
    "data": [
        'views/custom_pos_view.xml',
    ],
    'assets': {
        'point_of_sale._assets_pos': [
            'xrero_pos_discount/static/src/js/pos.js',
            'xrero_pos_discount/static/src/xml/orderLine.xml',
        ],
    },
    "auto_install": False,
    "installable": True,
    "images": ['static/description/icon.png'],
}
