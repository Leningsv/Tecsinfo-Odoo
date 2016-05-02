
{
    'name': "Gol Payment",
    'version': '1.0',
    'depends': ['base','account_voucher'],
    'author': "Author Name",
    'category': 'Category',
    'description': """
    Description text
    """,
    # data files always loaded at installation
    'data': [
        'views/gol_payment.xml',
    ],
    # data files containing optionally loaded demonstration data
    ''''demo': [
        #'demo_data.xml',
    ],'''
    'auto_install': False,
    'installable': True,
}
