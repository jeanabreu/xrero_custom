# -*- coding: utf-8 -*-
# Part of Softhealer Technologies.
{
    "name": "Responsive POS Theme",
    "version": "0.0.1",
    "category": "Point Of Sale",
    "sequence": 1,
    "summary": "POS Theme pos screen beautiful Responsive POS Screen point of sales Theme POS Responsive Theme mobile POS mobile theme point of sale Theme point of sale responsive theme point of sale mobile point of sale order theme POS theme responsive point of sale theme responsive pos responsive theme point of sale responsive theme Odoo",
    "description": """Are you bored with your standard odoo POS theme? Are You are looking for modern, creative, clean, clear, materialize Odoo theme for your POS? So you are at the right place, We have made sure that this theme is highly customizable and it comes with a premium look and feels. Our theme is not only beautifully designed but also fully functional, flexible, fast, lightweight, animated and modern theme.""",
    "author": "Xrero",
    "website": "https://www.xrero.com/",
    "depends": ["point_of_sale"],
    "data": [
        "data/pos_theme_settings_data.xml",
        "security/ir.model.access.csv",
        "views/sh_pos_theme_settings_views.xml",
    ],
    'assets': { 'point_of_sale._assets_pos': [
            "/xrero_pos_theme_responsive/static/src/overrides/pos_theme_variables.scss",
            'xrero_pos_theme_responsive/static/src/scss/mixin.scss',
            'xrero_pos_theme_responsive/static/lib/owl.carousel.js',
            'xrero_pos_theme_responsive/static/lib/owl.carousel.css',
            'xrero_pos_theme_responsive/static/lib/owl.theme.default.min.css',
            'xrero_pos_theme_responsive/static/src/app/**/*',
            'xrero_pos_theme_responsive/static/src/overrides/**/*',
            'xrero_pos_theme_responsive/static/src/scss/**/*',
            ],
        },
    'images': [
        'static/description/icon.png',
    ],
    "installable": True,
    "auto_install": False,
    "application": True
}
