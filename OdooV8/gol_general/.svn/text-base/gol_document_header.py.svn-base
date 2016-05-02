
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Importaciones
from datetime import date, datetime, timedelta
from openerp.osv import osv, fields
from openerp import models, fields, api
from duplicity.tempdir import default
# Configuramos

class GolDocumentHeader(osv.Model):
    _name = 'gol.document.header'
    _description = u'descripcion modulo'
    #Decalaracion de campos
    documentType=fields.Many2one('gol.document.type','Tipo de Documento')
    correlative=fields.Char('Correlativo',required=False)
    date=fields.Datetime('Fecha',default=datetime.now())    
    state = fields.Selection([('active','Activo'),
                                        ('annulled','Anulado')],'Estado del Comprobante',
                                        default ='active', required=True)

    gloss=fields.Text('Glosa')
GolDocumentHeader()


