
{
    'name': "Gol Company",
    'version': '1.0',
    'depends': ['base','gol_general','gol_configuration','account'],
    'author': "Lenin",
    'category': 'Category',
    'description': """
    Description text
    """,
    # data files always loaded at installation
    'data': [
        'views/gol_company.xml',
        'views/gol_bank_account_company.xml',
        'views/gol_view_company_inherit_form.xml',
    ],
    # data files containing optionally loaded demonstration data
    ''''demo': [
        'demo_data.xml',
    ],'''
    'auto_install': False,
    'installable': True,
}
