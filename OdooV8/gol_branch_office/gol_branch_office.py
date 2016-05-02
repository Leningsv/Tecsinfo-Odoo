#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Importaciones
from datetime import date, datetime, timedelta
from openerp.osv import osv, fields
from openerp import models, fields, api
class GolBrachOffice(osv.Model):
    _name = 'gol.branch.office'  
    company=fields.Many2one('res.company','Compañia')  
    branchOffice=fields.Many2one('res.company','Sucursal') 
    correlative=fields.Char('Correlativo Sucursal')
    pointOfSale=fields.One2many('gol.point.of.sale','idBranchOffice','Punto de venta')
    
    @api.onchange('branchOffice')
    def GetBranchOffice(self):
        print self.branchOffice.parent_id
GolBrachOffice()

