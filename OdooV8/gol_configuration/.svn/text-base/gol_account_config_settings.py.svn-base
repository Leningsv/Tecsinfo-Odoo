#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Importaciones
from datetime import date, datetime, timedelta
from openerp.osv import osv, fields
from openerp import models, fields, api
class GolAccountConfigSettings(osv.Model):
    _name = 'account.config.settings'
    _inherit = 'account.config.settings'  
    invoicePrefix=fields.Char('Prefijo de la Factura',size=10,required=False)
    charactersAmount=fields.Integer('Cantidad de Caracteres',size=3,
                                    required=True, store=True,
                                    help='Este atrubuto determina la longitud del correlativo')
    separator=fields.Char('Separador',size=3,required=False,help='Separador que hay entre los números que conforman el correlativo')
    dateFormat=fields.Selection([('empty','Sin Fecha'),
                                 ('MMAAAA','MMAAAA'),
                                 ('AAAAMM','AAAAMM'),
                                 ('AAAA','AAAA'),
                                 ('MMAA','MMAA'),
                                 ('AAMM','AAMM')],'Formato Fecha',
                                 default ='empty', required=True)        
    dateSeparator=fields.Char('Separador Fecha',size=3,required=False,help='Separador que hay entre los números que conforman la fecha del correlativo')        
    consecutiveInvoice=fields.One2many('gol.consecutive','idFormatCorrelative','Consecutivo')
    preview= fields.Char('Vista Previa', Store=False,readonly=True,compute='_GetPreview')
    @api.one
    def _GetPreview(self):
        if self.invoicePrefix == False:
            self.invoicePrefix = ''
        if self.separator == False:
            self.separator = ''
        if self.dateSeparator == False:
            self.dateSeparator = ''  
        if self.dateFormat == 'empty':          
            self.preview=str(self.invoicePrefix)+str(self.separator)+'X'*int(self.charactersAmount)
        if self.dateFormat == 'MMAAAA':
            self.preview=self.invoicePrefix+str(self.separator)+'MM'+self.dateSeparator+'AAAA'+self.dateSeparator+'X'*int(self.charactersAmount)
        if self.dateFormat == 'AAAAMM':
            self.preview=self.invoicePrefix+str(self.separator)+'AAAA'+self.dateSeparator+'MM'+self.dateSeparator+'X'*int(self.charactersAmount)
        if self.dateFormat == 'AAAA':
            self.preview=self.invoicePrefix+str(self.separator)+'AAAA'+self.dateSeparator+'X'*int(self.charactersAmount)
        if self.dateFormat == 'MMAA':
            self.preview=self.invoicePrefix+str(self.separator)+'MM'+self.dateSeparator+'AA'+self.dateSeparator+'X'*int(self.charactersAmount)
        if self.dateFormat == 'AAMM':
            self.preview=self.invoicePrefix+str(self.separator)+'AA'+self.dateSeparator+'MM'+self.dateSeparator+'X'*int(self.charactersAmount)

    
    @api.model
    def default_get(self, vals):
        auxIds=self.env['account.config.settings'].search([])
        auxId=0
        for item in auxIds:
            auxId=item.id       
        auxFormatCorrelative= self.env['account.config.settings'].browse(auxId)
        res = super(GolAccountConfigSettings, self).default_get(vals)
        res.update({
            'invoicePrefix':auxFormatCorrelative.invoicePrefix,
            'separator':auxFormatCorrelative.separator,
            'dateFormat':auxFormatCorrelative.dateFormat,
            'dateSeparator':auxFormatCorrelative.dateSeparator,
            'charactersAmount':auxFormatCorrelative.charactersAmount,
            'sale_secuence_prefix':auxFormatCorrelative.sale_sequence_prefix, # Many2one field            
           })
            
        return res
    
    @api.onchange('invoicePrefix','charactersAmount','separator','dateFormat','dateSeparator')
    def GetPreview(self):
        if self.invoicePrefix == False:
            self.invoicePrefix = ''
        if self.separator == False:
            self.separator = ''
        if self.dateSeparator == False:
            self.dateSeparator = ''  
        if self.dateFormat == 'empty':          
            self.preview=str(self.invoicePrefix)+str(self.separator)+'X'*int(self.charactersAmount)
            self.sale_sequence_prefix= self.invoicePrefix
        if self.dateFormat == 'MMAAAA':
            self.preview=self.invoicePrefix+str(self.separator)+'MM'+self.dateSeparator+'AAAA'+self.dateSeparator+'X'*int(self.charactersAmount)
            self.sale_sequence_prefix= self.invoicePrefix+self.separator+'%(month)s'+self.dateSeparator+'%(year)s'+self.separator
        if self.dateFormat == 'AAAAMM':
            self.preview=self.invoicePrefix+str(self.separator)+'AAAA'+self.dateSeparator+'MM'+self.dateSeparator+'X'*int(self.charactersAmount)
            self.sale_sequence_prefix= self.invoicePrefix+self.separator+'%(year)s'+self.dateSeparator+'%(month)s'+self.separator
        if self.dateFormat == 'AAAA':
            self.preview=self.invoicePrefix+str(self.separator)+'AAAA'+self.dateSeparator+'X'*int(self.charactersAmount)
            self.sale_sequence_prefix= self.invoicePrefix+self.separator+'%(year)s'+self.separator
        if self.dateFormat == 'MMAA':
            self.preview=self.invoicePrefix+str(self.separator)+'MM'+self.dateSeparator+'AA'+self.dateSeparator+'X'*int(self.charactersAmount)
            self.sale_sequence_prefix= self.invoicePrefix+self.separator+'%(month)s'+self.separator+'%(y)s'+self.separator
        if self.dateFormat == 'AAMM':
            self.preview=self.invoicePrefix+str(self.separator)+'AA'+self.dateSeparator+'MM'+self.dateSeparator+'X'*int(self.charactersAmount)
            self.sale_sequence_prefix= self.invoicePrefix+self.separator+'%(y)s'+self.separator+'%(month)s'+self.separator   
GolAccountConfigSettings()

