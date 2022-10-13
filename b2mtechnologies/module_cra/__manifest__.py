# -*- coding: utf-8 -*-
{
    'name': "CRA",

    'summary': """
        Ce Module à été créé pour faire un reporting des activité dans une entreprise""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Marshall-Pierre",
    'website': "http://www.yourcompany.com",

    'category': 'Applications',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/view_admin.xml',
        'views/report_views.xml',
        'views/project_views.xml',
        'views/menus.xml',
    ],

    'application': True
}
