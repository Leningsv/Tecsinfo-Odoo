
{
    'name': "Gol Branch Office",
    'version': '1.0',
    'depends': ['base','gol_general'],
    'author': "Author Name",
    'category': 'Category',
    'description': """
    Description text
    """,
    # data files always loaded at installation
    'data': [
        'views/gol_branch_office.xml',
        'views/gol_point_of_sale.xml',
    ],
    # data files containing optionally loaded demonstration data
    ''''demo': [
        #'demo_data.xml',
    ],'''
    'auto_install': False,
    'installable': True,
}
