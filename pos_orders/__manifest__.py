# -*- coding: utf-8 -*-
{
    "name"              :  "POS All Orders List",
    "summary"           :  """POS All Orders List shows the list of orders placed in an Odoo POS session.
                              The user can also view customers' previous orders in the running POS session. Also, you can search for all orders by customer name or order reference number. The POS all order list module eases order searching and offers three different options to view orders; Load all past orders, load orders of current session, and load order of last 'n' days. Reorder list| POS Load previous orders| Past orders pos| Pos past orders| Orders POS session
                            """,
    "category"          :  "Point of Sale",
    "version"           :  "1.0.2",
    "sequence"          :  1,
    "website"           :  "https://xrero.com",
    "description"       :  """
                            POS all orders list allows you to view all the POS orders in the running POS session by searching by the customer name and order reference number.

                            """,
    "depends"           :  ['point_of_sale'],
    "data"              :  ['views/res_config_view.xml'],
    "demo"              :  ['data/pos_orders_demo.xml'],
    "images"            :  ['static/description/Banner.png'],
    "application"       :  True,
    "installable"       :  True,
    "assets"            :  {
                                'point_of_sale._assets_pos': [ 'pos_orders/static/src/**/*' ],
                            },
    "auto_install"      :  False,
    "price"             :  27,
    "pre_init_hook"     :  "pre_init_check",
}