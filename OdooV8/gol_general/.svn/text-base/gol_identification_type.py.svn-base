#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Importaciones
from datetime import date, datetime, timedelta
from openerp.osv import osv, fields
from openerp import models, fields, api
from openerp.exceptions import ValidationError
class GolIdentificaionType(osv.Model):
    _name = 'gol.identification.type'
    _inherit = 'gol.basic.entity'
    name=fields.Char('Nombre', required=True)
    validationType=fields.Selection([('numerical','Solo Numeros'),
                                    ('characters','Caracteres'),
                                    ('mixed','Caracteres y Números'),],'Tipo de validación',
                                    default ='numerical', required=True)
    charactersAmount=fields.Integer('Cantidad de Caracteres',required=True,help='Cantidad de digitos para la validación')
    #Validacion para no ingresar Typo de identificaciones duplicados
    _sql_constraints = [('unique_name',
                         'unique(name)',
                         'El tipo de identificación a ser registrada ya existe, ingrese una nueva'),]
                                   
GolIdentificaionType()
