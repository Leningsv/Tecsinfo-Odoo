#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Importaciones
from datetime import date, datetime, timedelta
from openerp.osv import osv, fields
from openerp import models, fields, api
# Configuramos

class GolFormatCorrelative(osv.Model):
    _name = 'gol.format.correlative'
    _rec_name='preview'
    #Decalaracion de campos
    companyPrefix=fields.Char('Prefijo de la Empresa',size=10,required=False)
    charactersAmount=fields.Integer('Cantidad de Caracteres',size=3,required=True,help='Este atrubuto determina la longitud del correlativo')
    separator=fields.Char('Separador',size=3,required=False,help='Separador que hay entre los números que conforman el correlativo')
    dateFormat=fields.Selection([('empty','Sin Fecha'),
                                 ('MMAAAA','MMAAAA'),
                                 ('AAAAMM','AAAAMM'),
                                 ('AAAA','AAAA'),
                                 ('MMAA','MMAA'),
                                 ('AAMM','AAMM')],'Formato Fecha',
                                 default ='empty', required=True)        
    dateSeparator=fields.Char('Separador Fecha',size=3,required=False,help='Separador que hay entre los números que conforman la fecha del correlativo')        
    consecutiveTypeAccountingVoucher=fields.One2many('gol.consecutive','idFormatCorrelative','Formato Correlativo')
    preview= fields.Char('Vista Previa', Store=False,readonly=True,compute='_GetPreview')
    
    @api.one
    def _GetPreview(self):
        if self.companyPrefix == False:
            self.companyPrefix = ''
        if self.separator == False:
            self.separator = ''
        if self.dateSeparator == False:
            self.dateSeparator = ''  
        if self.dateFormat == 'empty':          
            self.preview=str(self.companyPrefix)+str(self.separator)+'X'*int(self.charactersAmount)
        if self.dateFormat == 'MMAAAA':
            self.preview=self.companyPrefix+str(self.separator)+'MM'+self.dateSeparator+'AAAA'+self.dateSeparator+'X'*int(self.charactersAmount)
        if self.dateFormat == 'AAAAMM':
            self.preview=self.companyPrefix+str(self.separator)+'AAAA'+self.dateSeparator+'MM'+self.dateSeparator+'X'*int(self.charactersAmount)
        if self.dateFormat == 'AAAA':
            self.preview=self.companyPrefix+str(self.separator)+'AAAA'+self.dateSeparator+'X'*int(self.charactersAmount)
        if self.dateFormat == 'MMAA':
            self.preview=self.companyPrefix+str(self.separator)+'MM'+self.dateSeparator+'AA'+self.dateSeparator+'X'*int(self.charactersAmount)
        if self.dateFormat == 'AAMM':
            self.preview=self.companyPrefix+str(self.separator)+'AA'+self.dateSeparator+'MM'+self.dateSeparator+'X'*int(self.charactersAmount)
        
    @api.onchange('companyPrefix','charactersAmount','separator','dateFormat','dateSeparator')
    def GetPreview(self):
        if self.companyPrefix == False:
            self.companyPrefix = ''
        if self.separator == False:
            self.separator = ''
        if self.dateSeparator == False:
            self.dateSeparator = ''  
        if self.dateFormat == 'empty':          
            self.preview=str(self.companyPrefix)+str(self.separator)+'X'*int(self.charactersAmount)
        if self.dateFormat == 'MMAAAA':
            self.preview=self.companyPrefix+str(self.separator)+'MM'+self.dateSeparator+'AAAA'+self.dateSeparator+'X'*int(self.charactersAmount)
        if self.dateFormat == 'AAAAMM':
            self.preview=self.companyPrefix+str(self.separator)+'AAAA'+self.dateSeparator+'MM'+self.dateSeparator+'X'*int(self.charactersAmount)
        if self.dateFormat == 'AAAA':
            self.preview=self.companyPrefix+str(self.separator)+'AAAA'+self.dateSeparator+'X'*int(self.charactersAmount)
        if self.dateFormat == 'MMAA':
            self.preview=self.companyPrefix+str(self.separator)+'MM'+self.dateSeparator+'AA'+self.dateSeparator+'X'*int(self.charactersAmount)
        if self.dateFormat == 'AAMM':
            self.preview=self.companyPrefix+str(self.separator)+'AA'+self.dateSeparator+'MM'+self.dateSeparator+'X'*int(self.charactersAmount)
        
    
GolFormatCorrelative()


