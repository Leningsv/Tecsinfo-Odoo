#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Importaciones
from datetime import date, datetime, timedelta
from openerp.osv import osv, fields
from openerp import models, fields, api
class GolBankAccountCompany(osv.Model):
    _name = 'res.partner.bank'
    _inherit = 'res.partner.bank'    
    
    state = fields.Selection([('iban','IBAN'),
                              ('bank','Cuenta Bancaria')],'Tipo de Cuenta Bancaria',
                            default ='bank', required=True)
    checkFormat=fields.Char('Formato de Cheque',help='Dirección en la que se Encuentra el formato de Cheque')
GolBankAccountCompany()

