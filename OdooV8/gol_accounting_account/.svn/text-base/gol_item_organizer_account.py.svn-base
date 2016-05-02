#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Importaciones
from datetime import date, datetime, timedelta
from openerp.osv import osv, fields
from openerp import models, fields, api
class GolItemOrganizerAccount(osv.Model):
    _name = 'gol.item.organizer.account'
    idItemOrganizerAccount=fields.Many2one('account.account','Cuenta Ordenador')
    auxType=fields.Many2one('gol.organizer.type','Tipo')
    organizerAccount=fields.Many2one('gol.organizer.account','Cuenta Ordenador')
    code=fields.Char('Código')    
    
    @api.onchange('organizerAccount','code')
    def getCode(self):
        if self.organizerAccount:
            self.code=self.organizerAccount.code
            
    
    
GolItemOrganizerAccount()

