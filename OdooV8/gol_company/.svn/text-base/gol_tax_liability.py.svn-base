#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Importaciones
from datetime import date, datetime, timedelta
from openerp.osv import osv, fields
from openerp import models, fields, api
class GolTaxLiability(osv.osv):
    _name = 'gol.tax.liability'
    _inherit = 'gol.basic.entity'       
    state=fields.Boolean('Estado')
    date=fields.Datetime('Fecha de Ingreso')
    idCompany=fields.Many2one('res.company','Empresa')
GolTaxLiability()

