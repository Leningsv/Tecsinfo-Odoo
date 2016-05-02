
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Importaciones
from datetime import date, datetime, timedelta
from openerp.osv import osv, fields
from openerp import models, fields, api
class GolOrganizerType(osv.Model):
    _name = 'gol.organizer.type'
    _inherit = 'gol.basic.entity'    
    
    '''@api.model
    def create(self, vals):
        rec = super(GolOrganizerType, self).create(vals)
        auxAccount = self.env['account.account'].search([['code','=','0']])
        # 
        auxOrganizerType= self.env['gol.organizer.type'].search([])        
        auxItemsOrganizerAccount=self.env['gol.item.organizer.account'].search([['idItemOrganizerAccount','=',auxAccount.id]])
        auxItemsOrganizerAccount.unlink()
        
        #Crea las item ordenador asociados a la cuenta prinsipal       
        for item in auxOrganizerType:
            self.create_item_corganizer_account(auxAccount.id, item.id)           
        return rec
        
    @api.multi
    def create_item_corganizer_account(self,idAccount,organizerType):
        values = {}
        domain = {}
        auxItem=self.env['gol.item.organizer.account'].create({
                        'idItemOrganizerAccount':idAccount,
                        'auxType':organizerType,
                        })
        values['idItemOrganizerAccount']=auxItem.idItemOrganizerAccount
        values['auxType']=auxItem.auxType        
        return {'value': values, 'domain':domain}
    
    @api.multi
    def delete_item_corganizer_account(self,idAccount,organizerType):
        values = {}
        domain = {}
        auxItem=self.env['gol.item.organizer.account'].create({
                        'idItemOrganizerAccount':idAccount,
                        'auxType':organizerType,
                        })
        values['idItemOrganizerAccount']=auxItem.idItemOrganizerAccount
        values['auxType']=auxItem.auxType        
        return {'value': values, 'domain':domain}  '''
        
GolOrganizerType()

