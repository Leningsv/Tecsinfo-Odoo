#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Importaciones
from datetime import date, datetime, timedelta
from openerp.osv import osv, fields
from openerp import models, fields, api
# Configuramos

class GolOrganizerAccount(osv.Model):
    _name = 'gol.organizer.account'
    _inherit = 'gol.basic.entity'     
    _description = u'descripcion modulo'
    
    type = fields.Selection([('totalizer','Totalizadora'),
                            ('movement','Movimiento')],'Tipo Interno',
                            default ='movement', required=True)
    fatherAccount=fields.Many2one('gol.organizer.account','Cuenta Padre')
    classifier=fields.Many2one('gol.classifier','Clasificador de Cuenta')
    accountType=fields.Many2one('account.account.type','Tipo Cuenta')
    description=fields.Text('Descripción u Observación')
    organizerType=fields.Many2one('gol.organizer.type','Tipo Ordenador')      
    _sql_constraints = [('ValidateAccountUnduplicated',
                         'unique(code)',
                         'El código de la Cuenta Tipo Ordenador a ser ingresado existe, ingrese una nueva'),]
    
    @api.model
    def create(self, vals):
        rec = super(GolOrganizerAccount, self).create(vals)
        if(rec.fatherAccount.code is not False):           
            rec.code=str(rec.fatherAccount.code)+'.'+rec.code
        # ...        
        return rec    
GolOrganizerAccount()


