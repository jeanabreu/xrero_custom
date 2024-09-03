# -*- coding: utf-8 -*-
{
  "name"                 :  "POS Order Return",
  "summary"              :  """This module is use to Return orders in running point of sale session.Return Order|Order Return|Return|Custom Order Return""",
  "category"             :  "Point Of Sale",
  "version"              :  "1.1.2",
  "sequence"             :  1,
  "author"               :  "Xrero",
  "website"              :  "https://xrero.com",
  "depends"              :  ['pos_orders'],
  "data"                 :  ['views/pos_order_return_view.xml'],
  "images"               :  ['static/description/Banner.png'],
  "application"          :  True,
  "installable"          :  True,
  "assets"               :  {
                                'point_of_sale._assets_pos': [ 'xrero_pos_order_return/static/src/**/*' ],
                            },
  "auto_install"         :  False,
  "pre_init_hook"        :  "pre_init_check",
}