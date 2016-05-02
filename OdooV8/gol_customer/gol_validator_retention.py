#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Importaciones
from datetime import date, datetime, timedelta
from openerp.osv import osv, fields
from openerp import models, fields, api
# Configuramos

class GolValidatorRetention(osv.Model):
    _name = 'gol.validator.retention'
    _description = u'descripcion modulo'
    #Decalaracion de campos
    initialCorrelative=fields.Char('Correlativo inicial',size=50,required=True)
    correlativeEnd=fields.Char('Correlativo Final',size=50,required=True)
    broadcastDate=fields.Datetime('Fecha de Emisión')
    expirationDate=fields.Datetime('Fecha de Caducidad')
    authorizationNumber=fields.Char('Número de Autorización')
    idRulesRetention=fields.Many2one('res.partner','Reglas Retención')
GolValidatorRetention()


