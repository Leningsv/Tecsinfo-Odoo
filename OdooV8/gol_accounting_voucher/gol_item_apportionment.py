#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Importaciones
from openerp.exceptions import ValidationError
from datetime import date, datetime, timedelta
from openerp.osv import osv, fields
from openerp import models, fields, api
#from openerp.models import NewId
# Configuramos

class GolItemApportionment(osv.Model):
    _name = 'gol.item.apportionment'
    _description = u'descripcion modulo'

    
    idItemApportionment=fields.Many2one('gol.aux.item.apportionment','Cuenta Asociada')
    centerCost=fields.Many2one('gol.center.cost','Centro de Costo')
    auxValue=fields.Float('Valor (%)',readonly=False)
    amount=fields.Float('Monto',Store=True)

    @api.multi
    def onchange_CalculateAmount(self,auxValue,centerCost,context):
        values = {}
        domain = {}
        if centerCost:
            values['amount']=context["amount"]*auxValue/100
        return {'value': values, 'domain':domain}  


        '''if isinstance(idItemApportionment, models.NewId):
            print idItemApportionment
            print models.NewId
        #if isinstance(current_record.id, models.NewId):
            # do your stuff
        #prueba=self.env['gol.item.apportionment'].create({'line': [(0, 0, {})]})
        #print prueba.id
        #print prueba.idItemApportionment
        print idItemApportionment
        print self.ids
        auxAuxItemApportionment=self.env['gol.aux.item.apportionment'].browse(self.idItemApportionment)
        print auxAuxItemApportionment.amount
        auxAuxItemApportionment=self.env['gol.aux.item.apportionment'].browse(idItemApportionment)
        print auxAuxItemApportionment.amount
        #if value != 0.00:'''

GolItemApportionment()


