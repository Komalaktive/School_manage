# -*- coding: utf-8 -*-
{
    'name': "docu_item",

    'summary': """apps.openerp.com""",

    'description': """Long description of module's purpose""",

    'author': "My Company",
    'website': "http://www.yourcompany.com",
    'category': 'Document',
    "version": "14.0.1.0.0",
    'depends': ['base',],
    'data': [
        'security/ir.model.access.csv',
        'views/models_views.xml',
    ],
    "demo": [],
    "installable": True,
    "auto_install": False,
    "application": True,
}
