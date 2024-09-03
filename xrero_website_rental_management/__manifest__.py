# -*- coding: utf-8 -*-
{
    'name': 'Property Management Website',
    'description': 'Property Sale & Rental Website',
    'summary': 'Property Sale & Rental Website',
    'category': 'Website',
    'version': '2.0',
    'category': 'Website',
    'website': "https://www.xrero.com",
    'depends': [
        'web',
        'crm',
        'xrero_rental_management',
        'portal',
        'website',
        'website_blog',
        'website_mass_mailing'
    ],
    'data': [
        # data
        'data/data.xml',
        # security
        'security/ir.model.access.csv',
        # backend
        'views/backend/property_theme_config.xml',
        'views/backend/property_details.xml',
        # templates
        'views/assets.xml',
        'views/footer.xml',
        'views/header.xml',
        'views/home.xml',
        'views/listing.xml',
        'views/property_details.xml',
        'views/my_portal.xml',
        'views/map_view.xml',
    ],
    'assets': {
        'web.assets_frontend': [
            'xrero_website_rental_management/static/src/scss/colors.scss',
            'xrero_website_rental_management/static/src/css/reset.css',
            'xrero_website_rental_management/static/src/css/plugins.css',
            'xrero_website_rental_management/static/src/css/style.css',
            'xrero_website_rental_management/static/src/css/color.css',
            'xrero_website_rental_management/static/src/js/plugins.js',
            'xrero_website_rental_management/static/src/js/scripts.js',
            'xrero_website_rental_management/static/src/js/website_rental.js',
            'xrero_website_rental_management/static/src/js/map-single.js',
            'xrero_website_rental_management/static/src/js/map-plugins.js',
            'xrero_website_rental_management/static/src/js/map-listing.js',
        ],
        'web._assets_primary_variables': [
            'xrero_website_rental_management/static/src/scss/primary_variables.scss',
        ],
    },
    'images': [
        'static/description/icon.png',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'price': 274,
    'currency': 'USD',
}
