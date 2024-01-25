{
    'name': "université",
    'version': '1.0',
    'depends': ['base'],
    'author': "saye badiane",
    'category': 'Category',
    'description': """
    Projet université
    """,
    # data files always loaded at installation
    'data': [
        'views/student.xml',
        'views/professor.xml',
        'views/department.xml',
        'views/subject.xml',
        'views/classroom.xml',
    ],
    # data files containing optionally loaded demonstration data
    'demo': [
        # 'demo/demo_data.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
}   