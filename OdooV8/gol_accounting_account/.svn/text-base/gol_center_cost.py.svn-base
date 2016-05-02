
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Importaciones
from datetime import date, datetime, timedelta
from openerp.osv import osv, fields
from openerp import models, fields, api
class GolCenterCost(osv.Model):
    _name = 'gol.center.cost'
    _inherit = 'gol.basic.entity'    
    centerCostFather=fields.Many2one('gol.center.cost','Centro de costo padre')
GolCenterCost()

