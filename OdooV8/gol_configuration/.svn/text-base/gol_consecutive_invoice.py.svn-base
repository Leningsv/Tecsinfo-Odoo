#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Importaciones
from datetime import date, datetime, timedelta
from openerp.osv import osv, fields
from openerp import models, fields, api
from duplicity.tempdir import default
# Configuramos

class GolConsecutive(osv.Model):
    _name = 'gol.consecutive.invoice'
    _inherit = 'gol.consecutive' 
    idFormatCorrelative=fields.Many2one('gol.consecutive','Formato Correlativo')
GolConsecutive()
