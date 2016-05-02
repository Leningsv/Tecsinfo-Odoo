#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Importaciones
from datetime import date, datetime, timedelta
from openerp.osv import osv, fields
from openerp import models, fields, api
class GolPointOfSale(osv.Model):
    _name = 'gol.point.of.sale'
    _inherit = 'gol.basic.entity'  
    idBranchOffice=fields.Many2one('gol.branch.office','Sucursal')  
    correlative=fields.Char('Correlativo', size=80)
    itemUser=fields.One2many('gol.item.user','idItemUser','Usuarios')
    document=fields.One2many('gol.document','idPointOfSale','Documentos Asociados')
GolPointOfSale()

