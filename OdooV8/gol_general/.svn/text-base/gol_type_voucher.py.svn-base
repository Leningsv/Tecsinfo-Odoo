#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Importaciones
from datetime import date, datetime, timedelta
from openerp.osv import osv, fields
from openerp import models, fields, api
class GolTypeVoucher(osv.Model):
    _name = 'gol.type.voucher'
    _inherit = 'gol.basic.entity'
    _sql_constraints = [('ValidateTypeVoucherUnduplicated',
                         'unique(name)',
                         'El tipo de comprobante a ser ingresado existe, ingrese uno nuevo'),]
GolTypeVoucher()

