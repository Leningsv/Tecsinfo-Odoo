#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Importaciones
from datetime import date, datetime, timedelta
from openerp.osv import osv, fields
from openerp import models, fields, api
class GolAuxItemApportionment(osv.Model):
    _name = 'gol.aux.item.apportionment'        
    #Campos Adicionales
    itemApportionment= fields.One2many('gol.item.apportionment','idItemApportionment','Tabla de Prorrateo Asociada a la Cuenta')
    amount = fields.Float('Valor')                      
GolAuxItemApportionment()