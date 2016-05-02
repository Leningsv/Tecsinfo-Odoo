
{
    'name': "Gol Debit Note",
    'version': '1.0',
    'depends': ['base','gol_invoice','gol_general','gol_accounting_voucher','account_voucher'],
    'author': "Lenin",
    'category': 'Category',
    'description': """
    Description text
    """,
    # data files always loaded at installation
    'data': [
        'views/gol_debit_note.xml',
    ],
    # data files containing optionally loaded demonstration data
    ''''demo': [
        #'demo_data.xml',
    ],'''
    'auto_install': False,
    'installable': True,
}
