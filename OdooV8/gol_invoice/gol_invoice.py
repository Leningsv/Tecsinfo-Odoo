#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Importaciones
from datetime import date, datetime, timedelta
from openerp.osv import osv, fields
from openerp import models, fields, api
from openerp.exceptions import ValidationError
class GolInvoice(osv.Model):
    _name = 'account.invoice'
    _inherit = 'account.invoice'    
    documentType=fields.Many2one('gol.document.type')
    amountPaid=fields.Float('Monto Abonado', compute='_GetAmountPaid', Store=True)
    purchaseOrder=fields.Char('Orden de Compra')
    contractName=fields.Char('Nombre del Contrato')
    authorizationNumber=fields.Char('Número de Autorización')
    description=fields.Text('Observación')
    amountDiscount=fields.Float('Descuentos')    
    #Elementos Modificados
    date_invoice=fields.Date('Fecha',default=datetime.now().strftime('%Y-%m-%d'))
    
    #Metodos Modificados
    
    @api.one
    @api.constrains('invoice_line')
    @api.onchange('partner_id','invoice_line')
    def ValidateFields(self):
        if(self.partner_id == False):
            raise ValidationError('Usted debe seleccionar un cliente')  
        
    @api.one
    def _GetAmountPaid(self):         
        self.amountPaid=self.amount_total - self.residual
  
GolInvoice()






