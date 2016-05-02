#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Importaciones
from datetime import date, datetime, timedelta
from openerp.osv import osv, fields
from openerp import models, fields, api
from duplicity.tempdir import default
from openerp.api import onchange
# Configuramos

class GolDebitNote(osv.Model):
    _name = 'gol.debit.note'
    _description = u'descripcion modulo'
    #Decalaracion de campos
    documentType=fields.Many2one('gol.document.type','Tipo de Documento')
    correlative=fields.Char('Correlativo',required=False)
    date = fields.Date('Fecha',default=datetime.now().strftime('%Y-%m-%d'))
    #date=fields.Datetime('Fecha',default=datetime.now())    
    state = fields.Selection([('active','Activo'),
                                        ('annulled','Anulado')],'Estado del Comprobante',
                                        default ='active', required=True)
    invoice = fields.Many2one('account.invoice','Factura')
    authorizationNumber = fields.Char('Número de Autorización')
    typeDebitNote = fields.Many2one('gol.type.debit.note','Tipo')
    accountingVoucher =fields.One2many('account.move','idAccountMove','Comprobantes Contables')
    debitNoteAmount = fields.Float('Monto')
    taxAmount = fields.Float('Monto Impuesto')
    gloss=fields.Text('Glosa')
    #Campos Temporales Factura
    authorizationNumberInvoice = fields.Char('Número de Autorización de la Factura', Store=False)
    numberInvoice = fields.Char('Número de Factura', Store=False)
    estateInvoice = fields.Char('Estado', Store=False)
    amountInvoice = fields.Char('Monto Factura', Store=False)
    
    @api.onchange('invoice')
    def GetDatasInvoiceAndCustomer(self):
        self.authorizationNumberInvoice=self.invoice.authorizationNumber
        #self.numberInvoice=self.invoice.number
        self.estateInvoice=self.invoice.state
        #self.amountInvoice=self.invoice.amount_total
    
    
GolDebitNote()