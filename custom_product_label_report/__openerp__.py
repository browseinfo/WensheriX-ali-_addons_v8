# -*- coding: utf-8 -*-
##############################################################################
#
#    This module uses OpenERP, Open Source Management Solution Framework.
#    Copyright (C) 2015-Today BrowseInfo (<http://www.browseinfo.in>)
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>
#
##############################################################################

{
    'name': 'Custom Product Label',
    'description': """
Customise product label report and add QR code and barcode.
================================================================================================.
""",
    'author': 'BrowseInfo',
    'version': '0.1',
    'depends': ['base','product'],
    'data': ['custom_report_menu.xml',
              'wizard/custom_wizard_label_print.xml',
              'views/custom_product_label_report_view.xml',],
    'demo': [],
    'installable': True,
}



# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
