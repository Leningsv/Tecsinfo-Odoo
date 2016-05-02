#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Importaciones
from datetime import date, datetime, timedelta
from openerp.osv import osv, fields
from openerp import models, fields, api
class GolAccountMoveLine(osv.Model):
    _name = 'account.move.line'
    _inherit = 'account.move.line'
    
    ############Intento 1
    #Campos Adicionales
    auxItemApportionment= fields.Many2one('gol.aux.item.apportionment','Distribución centros de costo')  
    
    @api.onchange('partner_id')
    def GetPartnerInformation(self):       
        if str(self.partner_id) != 'res.partner()':
            self.account_id=self.partner_id.property_account_receivable
    @api.multi
    def onchange_account_id(self,account_id,debit,credit):      
        #Intento 3 Funcionando --- :)
        values = {}
        domain = {}
        values['auxItemApportionment']=False
        if account_id:
            auxAmount=0.00
            if debit != 0.00:
                auxAmount=debit
            elif credit != 0.00:
                auxAmount=credit
            if auxAmount != 0.00:                            
                auxAccount=self.env['account.account'].browse(account_id)           
                if auxAccount.centerCostUse == True and auxAccount.apportionmentUse == False and str(auxAccount.apportionment) == 'gol.apportionment()':                                                  
                    auxAuxItemApportionment=self.env['gol.aux.item.apportionment'].create({'id':self.auxItemApportionment,
                                                                                           'amount':auxAmount})
                    values['auxItemApportionment']=auxAuxItemApportionment.id
                if auxAccount.centerCostUse == True and auxAccount.apportionmentUse == True and str(auxAccount.apportionment) == 'gol.apportionment()':                
                    auxAuxItemApportionment=self.env['gol.aux.item.apportionment'].create({})              
                    values['auxItemApportionment']=auxAuxItemApportionment.id  
                
                if auxAccount.centerCostUse == True and auxAccount.apportionmentUse == True and str(auxAccount.apportionment) != 'gol.apportionment()':    
                    auxItemCenterCost=self.env['gol.item.center.cost'].search([['idItemCenterCost', '=', auxAccount.apportionment.id]])           
                    auxAuxItemApportionment=self.env['gol.aux.item.apportionment'].create({})              
                    for item in auxItemCenterCost:       
                        self.insertarItems(auxAuxItemApportionment.id, item.value, item.centerCost.id,auxAmount)
                    values['auxItemApportionment']=auxAuxItemApportionment.id                             
        return {'value': values, 'domain':domain} 
    
    @api.multi
    def insertarItems(self,auxId,auxValue,auxIdCenterCost,auxAmount):
        values = {}
        domain = {}
        auxAmount=auxAmount*auxValue*0.01
        auxItem=self.env['gol.item.apportionment'].create({
                        'idItemApportionment':auxId,
                        'centerCost':auxIdCenterCost,
                        'auxValue':auxValue,
                        'amount':auxAmount})
        values['idItemApportionment']=auxItem.idItemApportionment
        values['centerCost']=auxItem.centerCost        
        values['auxValue']=auxItem.auxValue
        values['amount']=auxItem.amount    
        return {'value': values, 'domain':domain}  
                        
GolAccountMoveLine()

