#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Importaciones
from datetime import date, datetime, timedelta
from openerp.osv import osv, fields
from openerp import models, fields, api
from openerp.exceptions import ValidationError
# Configuramos

class GolItemCenterCost(osv.Model):
    _name = 'gol.item.center.cost'
    _description = u'descripcion modulo'
    
    centerCost=fields.Many2one('gol.center.cost','Centro de costo')
    value=fields.Float('Valor (%)')    
    #Decalaracion de campos
    idItemCenterCost=fields.Many2one('gol.apportionment','Tabla de Prorrateo')
          
GolItemCenterCost()


