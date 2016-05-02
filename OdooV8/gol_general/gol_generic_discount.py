#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Importaciones
from datetime import date, datetime, timedelta
from openerp.osv import osv, fields
from openerp import models, fields, api
class GolGenericDiscount(osv.Model):
    _name = 'gol.generic.discount'
    _inherit = 'gol.basic.entity'
    _rec_name='code'    
    relatedAccount=fields.Many2one('account.account','Cuenta Asociada')
    code=fields.Char('Código',size=50,Storage=True, readonly=True, compute='_SetCode')
    name=fields.Char('Nombre',size=50,required=False,help='Ingrese el Nombre')
    value=fields.Float('Valor',help='Este valor fluctua de 0% a 100%, y determina el descuento que se asocia a un producto')
    '''_sql_constraints = [('ValidateGenericDiscountUnduplicated',
                         'unique(name)',
                         'El descuento a ser ingresado existe, ingrese uno nuevo'),]'''
        
    @api.onchange('value')
    def GenerateCode(self):
        self.code= 'Descuento ('+str(self.value)+' %)'
    @api.one
    def _SetCode(self):
        self.code= 'Descuento ('+str(self.value)+' %)'   
GolGenericDiscount()


