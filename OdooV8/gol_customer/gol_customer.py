#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Importaciones
from datetime import date, datetime, timedelta
from openerp.osv import osv, fields
from openerp import models, fields, api
from openerp.osv.fields import related
from openerp.exceptions import ValidationError

class GolCustomer(osv.Model):
    _name = 'res.partner'
    _inherit = 'res.partner' 
    
    comment=fields.Text("Descripción u Observación")
    
    tradename=fields.Char('Nombre Comercial', size=80)
    phone=fields.Char('Teléfono 1', size=15)
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
    #Datos del cliente
    shortName=fields.Char('Nombre Corto', size=80)
    customerType=fields.Many2one('gol.customer.type','Tipo de Cliente')
    #accountingAccount=fields.Many2one('account.account','Cuenta Contable')
    balance=fields.Float('Saldo')             
    customerType=fields.Many2one('gol.customer.type','Tipo de Cliente')
    discount=fields.Many2one('gol.generic.discount','Descuento Cliente')
    rulesRetention=fields.One2many('gol.validator.retention','idRulesRetention','Reglas Retención')
    #Campos para el Credito
    maximunAmount=fields.Float('Monto Maximo',size=50,help='Monto maximo de crédito')
    warranty=fields.Text('Garantía',help='Que tiene de garantia por el crédito') 
    #Validar Clientes no duplicados
    
GolCustomer()








