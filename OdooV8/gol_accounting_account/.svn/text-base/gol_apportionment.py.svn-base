#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Importaciones
from openerp.exceptions import ValidationError
from datetime import date, datetime, timedelta
from openerp.osv import osv, fields
from openerp import models, fields, api
class GolApportionment(osv.Model):
    _name = 'gol.apportionment'
    _inherit = 'gol.basic.entity'
    itemCenterCost=fields.One2many('gol.item.center.cost','idItemCenterCost','Articulo Centro de Costo')
    totalValue=fields.Float('Valor Total (%)',readonly=False,Store=True)

    @api.constrains('totalValue')
    def ValidatePercent(self):
        if self.totalValue != 100.0:
            raise ValidationError('La sumatoria del valor asignado a los centros de costo tiene que ser 100.00 %')
         
    @api.onchange('itemCenterCost','totalValue')
    def ValidateValue(self):
        self.totalValue=0.00
        for value in self.itemCenterCost:
            self.totalValue= value.value+self.totalValue

GolApportionment()




