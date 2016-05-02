#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Importaciones
from datetime import date, datetime, timedelta
from openerp.osv import osv, fields
from openerp import models, fields, api
class Product(osv.Model):
    _name = 'product.template'
    _inherit = 'product.template'


    @api.multi
    def name_get(self):
        res = []
        for asset in self:
            res.append((asset.id,
                        str(asset.default_code) + '-' + str(asset.name)))
        return res
Product()


