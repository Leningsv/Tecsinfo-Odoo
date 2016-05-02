#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Importaciones
#!/usr/bin/python
from datetime import date, datetime, timedelta
from openerp.osv import osv, fields
from openerp import models, fields, api
from duplicity.tempdir import default

class GolAccount(osv.Model):
    _name = 'account.account'
    _inherit = 'account.account'    
    classifier=fields.Many2one('gol.classifier', 'Tipo Clasificador')
    itemOrganizerAccount=fields.One2many('gol.item.organizer.account','idItemOrganizerAccount','Articulo Cuenta Ordenador') 
    associatedModule=fields.Many2one('gol.associated.module','Modulo Asociado')
    centerCostUse=fields.Boolean('Usa centros de costo',Store=True, visible=False)
    apportionmentUse=fields.Boolean('Es prorrateable',Store=True, visible=False)
    apportionment=fields.Many2one('gol.apportionment','Tabla de Prorrateo', visible=False)
    #Campos si es de tipo Banco
    isBank=fields.Boolean('Es cuenta Bancaria',Store=True)
    bankAccountCompany=fields.Many2one('res.partner.bank','Cuenta Bancaria', visible=False)
    
    #Campos Temporales
    auxType=fields.Selection([
            ('view', 'Totalizadora'),
            ('other', 'Movimiento'),] , 'Tipo Interno',default='other', required=True, Store=False)
    
    #Campos modificados
    type=fields.Selection([
            ('view', 'Totalizadora'),
            ('other', 'Movimiento'),
            ('receivable', 'Receivable'),
            ('payable', 'Payable'),
            ('liquidity','Liquidity'),
            ('consolidation', 'Consolidation'),
            ('closed', 'Closed'),], 'Tipo Interno',default='other', required=False)   
    
    '''Con esta clase es para no motrar todos los tipos de cuenta
    Limitandolos a tipo view y other'''
    @api.onchange('auxType')
    def SetType(self):
        if self.auxType == 'view':
            self.type = 'view'
        if self.auxType == 'other':
            self.type = 'other'
    @api.onchange('isBank')
    def HideBankAccountCompany(self):
        if self.isBank == False:
            self.bankAccountCompany=False
        if self.isBank == True:
            self.centerCostUse=False
            self.associatedModule=False
    
    @api.onchange('centerCostUse','apportionmentUse','type')
    def HideApportionment(self):
        if self.type == 'view':
            self.apportionmentUse =False
            self.centerCostUse= False
        if self.centerCostUse == False:
            self.apportionmentUse = False
            self.apportionment=False
        if self.apportionmentUse == False: 
            self.apportionment=False
        if self.centerCostUse == True or self.apportionmentUse == True:
            self.isBank=False  
    
    '''Con esta Funcion pongo valores por defecto el las cuentas de tipo ordenador
    Esto lo hago con la finalidad que esten listadas todas las cuentas tipo ordenador'''          
    @api.model
    def default_get(self, vals):
        auxOrganizerType= self.env['gol.organizer.type'].search([])
        listItemOrganizerAccount=[]
        for item in auxOrganizerType:
            '''Aqui lleno mi lista con un array para esto adjunte () diciendole a mi lista que lo que
            ingreso es un array'''
            listItemOrganizerAccount.append((0,0,{'auxType':item.id}))
        res = super(GolAccount, self).default_get(vals)      
        res.update({'itemOrganizerAccount': listItemOrganizerAccount})
        return res
    
    
    
    
    
    '''@api.onchange('type')
    def LoadItemOrganizerAccount(self):   
        
        #Intento 3 Funcionando --- :)
        auxOrganizerType= self.env['gol.organizer.type'].search([])        
        print self.id
        if isinstance(self.id, models.NewId):
            print self.id
        for item in auxOrganizerType:
            auxItemOrganizerAccount=self.env['gol.item.organizer.account'].create({})
            self.itemOrganizerAccount=auxItemOrganizerAccount           
            print self.env['account.account'].browse()
            print auxItemOrganizerAccount.id 
            self.env['gol.item.organizer.account'].browse(int(auxItemOrganizerAccount.id)).write({'idItemOrganizerAccount':self.id,
                                                                                                  'auxType':item.id})
            
            #self.env['gol.item.organizer.account'].search('id','=',auxItemOrganizerAccount.id).write({'auxType':self.type.id})
            #print items.id
   
    @api.model
    def default_get(self, vals):
        auxAccount = self.env['account.account'].search([['code','=','0']])
        auxIds = str(auxAccount.itemOrganizerAccount).replace('gol.item.organizer.account','')
        auxIds = auxIds.replace('(', '')
        auxIds = auxIds.replace(')', '')
        auxIds = auxIds.replace(' ', '')
        auxList=[]
        for item in auxIds.split(','):
            auxList.append(int(item))
        print auxList
        print auxIds.split(',')
        res = super(GolAccount, self).default_get(vals)        
        res.update({'itemOrganizerAccount': auxList                   
                  })
        return res
    
    @api.multi
    def insertOrganizerType(self,auxItemId, auxId):
        values = {}
        auxItem=self.env['gol.item.organizer.account'].create({
                        'idItemOrganizerAccount':auxId,
                        'auxType':auxItemId})
        values['auxType']=auxItem.auxType
        values['auxType']=auxItem.auxType
        return {'value': values}'''            

          
GolAccount()

