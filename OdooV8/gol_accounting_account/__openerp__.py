
{
    'name': "Gol Accounting Account",
    'version': '1.0',
    'depends': ['base','account','gol_general'],
    'author': "Author Name",
    'category': 'Category',
    'description': """
    Description text
    """,
    # data files always loaded at installation
    'data': [
        'views/gol_account.xml',
        'views/gol_organizer_account.xml',
        'views/gol_apportionment.xml',
        'views/gol_item_center_cost.xml',
    ],
    # data files containing optionally loaded demonstration data
    ''''demo': [
        #'demo_data.xml',
    ],'''
    'auto_install': False,
    'installable': True,
}
