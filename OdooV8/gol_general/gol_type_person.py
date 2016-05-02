#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Importaciones
from datetime import date, datetime, timedelta
from openerp.osv import osv, fields
from openerp import models, fields, api
class GolPersonType(osv.Model):
    _name = 'gol.type.person'
    _inherit = 'gol.basic.entity'
    name=fields.Char('Tipo de persona', size=80)  
    _sql_constraints = [('ValidatePersonTypeUnduplicated',
                         'unique(name)',
                         'El tipo de persona a ser ingresada existe, ingrese una nueva'),]  
GolPersonType()



