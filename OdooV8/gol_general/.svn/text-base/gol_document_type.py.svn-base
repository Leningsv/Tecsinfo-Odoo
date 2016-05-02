
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Importaciones
from datetime import date, datetime, timedelta
from openerp.osv import osv, fields
from openerp import models, fields, api
class GolDocumentType(osv.Model):
    _name = 'gol.document.type'
    _inherit = 'gol.basic.entity'
    _sql_constraints = [('ValidateDocumentTypeUnduplicated',
                     'unique(name)',
                     'El tipo de documento a ser registrado ya existe, ingrese uno nuevo'),]
    
GolDocumentType()



