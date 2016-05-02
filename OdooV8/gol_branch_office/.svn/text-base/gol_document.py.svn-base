#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Importaciones
from datetime import date, datetime, timedelta
from openerp.osv import osv, fields
from openerp import models, fields, api
from duplicity.tempdir import default
# Configuramos

class GolDocument(osv.Model):
    _name = 'gol.document'
    _description = u'descripcion modulo'
    #Decalaracion de campos
    authorizationNumber=fields.Char('Número de Autorización')
    documentType=fields.Many2one('gol.document.type','Tipo de Documento')
    correlativeFrom=fields.Char('Correlativo Desde')
    correlativeTo=fields.Char('Correlativo Hasta')
    broadcastDate=fields.Date('Fecha Desde')
    expirationDate=fields.Date('Fecha Hasta')
    correlativeCurrentPosition=fields.Char('Posición Actual')
    active=fields.Boolean('Activo',default=True)
    #description=fields.Text('Descripción')
    correlativeLength=fields.Integer('Longitud')
    idPointOfSale=fields.Many2one('gol.point.of.sale','Punto de Venta')
GolDocument()


