# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

# {
#     'name': 'school manage',
#     'version': '14.0.1.0.0',
#     'category': 'School manage/Employees',
#     'sequence': 1,
#     'summary': 'Centralize employee information',
#     'description': "",
#     'website': 'https://www.odoo.com/page/employees',
#     'depends': ['base','sale', ],
#     'data': [
#         'security/ir.model.access.csv',
#         'views/school_view.xml',
#         'views/sale.xml',
#     ],
#     'demo': [],
#     'installable': True,
#     'auto_install': False,
#     'application': True
# }



{
    'name': 'school manage',
    'version': '14.0.1.0.0',
    'category': 'School manage/Employees',
    'summary': 'Centralize employee information',
    'description': """
This module contains all the common details of collage student.
    """,
    'website': 'https://www.odoo.com/page/employees',
    'depends': ['sale', ],
    'data': [
        'security/ir.model.access.csv',
        'views/school_view.xml',
        'views/sale_view.xml',
    ],
    'demo': [],
    'installable': True,
    'auto_install': False,
    'application': True
}