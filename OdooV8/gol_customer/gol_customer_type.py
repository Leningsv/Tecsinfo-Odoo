#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Importaciones
from datetime import date, datetime, timedelta
from openerp.osv import osv, fields
from openerp import models, fields, api
class GolCustomerType(osv.Model):
    _name = 'gol.customer.type'
    _inherit = 'gol.basic.entity'    
GolCustomerType()

