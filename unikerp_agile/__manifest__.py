{
    'name': "unikerp_agile",
    'version': '1.0',
    'depends': ['base','contacts'],
    'author': "saye badiane",
    'category': 'Category',
    'description': """
    Test technique 
    """,
    # data files always loaded at installation
    'data': [
         'views/unikerp.xml',
         'views/unikerp_spring.xml',
         'views/unikerp_events.xml',
         'data/demo.xml',
         'views/menuitem.xml',
         'security/ir.model.access.csv',
    ],
    # data files containing optionally loaded demonstration data
    'demo': [
        # 'demo/demo_data.xml',
    ],
    'installable': True,
    'auto_install': False,
}    