#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Importaciones
from datetime import date, datetime, timedelta
from openerp.osv import osv, fields
from openerp import models, fields, api
class GolPayment(osv.Model):
    _name = 'account.voucher'
    _inherit = 'account.voucher'    
    
    auxTotalAmount=fields.Float('Monto Total')
    
 
GolPayment()

