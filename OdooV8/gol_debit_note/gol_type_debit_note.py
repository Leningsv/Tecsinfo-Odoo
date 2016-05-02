#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Importaciones
from datetime import date, datetime, timedelta
from openerp.osv import osv, fields
from openerp import models, fields, api
class GolTypeDebitNote(osv.Model):
    _name = 'gol.type.debit.note'
    _inherit = 'gol.basic.entity'    
GolTypeDebitNote()

