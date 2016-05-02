
{
    'name': "Gol Accounting Voucher",
    'version': '1.0',
    'depends': ['base','gol_general','account','gol_accounting_account'],
    'author': "Author Name",
    'category': 'Category',
    'description': """
    Description text
    """,
    # data files always loaded at installation
    'data': [
        'views/gol_accounting_voucher.xml',
        'views/gol_item_apportionment.xml',
    ],
    # data files containing optionally loaded demonstration data
    ''''demo': [
        #'demo_data.xml',
    ],'''
    'auto_install': False,
    'installable': True,
}
