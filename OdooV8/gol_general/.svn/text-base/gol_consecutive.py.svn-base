#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Importaciones
from datetime import date, datetime, timedelta
from openerp.osv import osv, fields
from openerp import models, fields, api
from duplicity.tempdir import default
# Configuramos

class GolConsecutive(osv.Model):
    _name = 'gol.consecutive'
    #Decalaracion de campos
    cosecutive=fields.Char('Consecutivo',size=50,help='Posicion del consecutivo mas 1')
    mont=fields.Boolean('Mes',default=True,help='Permite agrupar los consecutivos en funcion de mes')
    year=fields.Boolean('Año',default=True,help='Permite agrupar los consecutivos en funcion de año')
GolConsecutive()
