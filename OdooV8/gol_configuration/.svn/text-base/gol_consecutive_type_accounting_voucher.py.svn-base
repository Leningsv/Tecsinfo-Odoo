#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Importaciones
from datetime import date, datetime, timedelta
from openerp.osv import osv, fields
from openerp import models, fields, api
from duplicity.tempdir import default
# Configuramos

class GolConsecutiveTypeAccountingVoucher(osv.Model):
    _name = 'gol.consecutive'
    #Decalaracion de campos
    typeVoucher=fields.Many2one('gol.type.voucher','Tipo de Comprobante',required=True)
    cosecutive=fields.Char('Consecutivo',size=50,readonly=True,help='Posicion del consecutivo mas 1')
    mont=fields.Boolean('Mes',default=True,help='Permite agrupar los consecutivos en funcion de mes')
    year=fields.Boolean('Año',default=True,help='Permite agrupar los consecutivos en funcion de año')
    idFormatCorrelative=fields.Many2one('gol.format.correlative','Formato Correlativo')
GolConsecutiveTypeAccountingVoucher()


