#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Importaciones
from datetime import date, datetime, timedelta
from openerp.osv import osv, fields
from openerp import models, fields, api
from Crypto.Util.number import size
class GolCompany(osv.osv):
    _name = 'res.company'
    _inherit = 'res.company'
    #Para el eliminar el tex area en empresa
    overdue_msg=fields.Text('Descripción')
    
    tradename=fields.Char('Nombre Comercial', size=80)
    phone2=fields.Char('Teléfono 2', size=15)
    phone3=fields.Char('Teléfono 3', size=15)
    riseUse=fields.Selection([('rise','Rise'),
                                    ('contributorSpecial','Contribuyente Especial')],'Seleccione',
                                    default ='rise', required=True)
    identificationType=fields.Many2one('gol.identification.type','Tipo de Identificación')    
    identificationNumber=fields.Char('Número de Identificación',help='Ingrese el numero de identificación')
    typePerson=fields.Many2one('gol.type.person','Tipo de persona')
    bussinesName=fields.Char('Razón Social',help='Ingrese el razón social')
    forcedToTakeAccounting=fields.Boolean('Obligado a llevar contabilidad',default=False)      
    accountant=fields.Many2one('gol.accountant','Contador')
    taxLiability=fields.One2many('gol.tax.liability','idCompany','Obligaciones Tributarias')
    legalRepresentative=fields.Many2one('gol.contact','Representante Legal')
    formatCorrelative=fields.Many2one('gol.format.correlative','Formatos Correlativos')
    
    child_contact_ids=fields.One2many('res.partner', 'parent_id', 'Contacts', domain=[('active','=',True)]),
 
    
GolCompany()

