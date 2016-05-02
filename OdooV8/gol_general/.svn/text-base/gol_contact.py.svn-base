#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Importaciones
from datetime import date, datetime, timedelta
from openerp.osv import osv, fields
from openerp import models, fields, api


class GolContact(osv.Model):
    _name = 'gol.contact'
    _rec_name = 'completeName' 
    completeName=fields.Char('Nombre Completo', size=80, required=True)
    phone=fields.Char('Teléfono',size=15)    
    cellphone=fields.Char('Télefono Celular',size=15,required=False,help='Teléfono Celular')    
    email=fields.Char('Email',required=True,help='Email del contacto')
    identificationType=fields.Many2one('gol.identification.type','Tipo de Identificación')    
    identificationNumber=fields.Char('Número de Identificación')
    _sql_constraints = [('ValidateContactUnduplicated',
                         'unique(email)',
                         'El mail a ser ingresado existe, ingrese uno nuevo'),]
GolContact()

