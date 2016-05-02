#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Importaciones
from datetime import date, datetime, timedelta
from openerp.osv import osv, fields
from openerp import models, fields, api
# Configuramos

class GolItemUser(osv.Model):
    _name = 'gol.item.user'
    _description = u'descripcion modulo'
    #Decalaracion de campos
    user=fields.Many2one('res.users','Usuario')
    idItemUser=fields.Many2one('gol.item.user','Punto de Venta')
GolItemUser()


