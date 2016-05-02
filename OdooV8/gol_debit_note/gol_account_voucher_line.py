#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Importaciones
from datetime import date, datetime, timedelta
from openerp.osv import osv, fields
from openerp import models, fields, api
# Configuramos

class modulo(osv.Model):
    _name = 'account.voucher.line'
    _inherit = 'account.voucher.line' 
    #Decalaracion de campos
    amounInvoice=fields.Float('Monto Factura',Store=True)
    residualInvoice=fields.Float('Residuo Factura', Store=True)

    def onchange_gol_move_line_id(self, cr, user, ids, move_line_id, context=None):
        """
        Returns a dict that contains new values and context

        @param move_line_id: latest value from user input for field move_line_id
        @param args: other arguments
        @param context: context arguments, like lang, time zone

        @return: Returns a dict which contains new values, and context
        """
        res = {}
        move_line_pool = self.pool.get('account.move.line')
        if move_line_id:
            move_line = move_line_pool.browse(cr, user, move_line_id, context=context)
            if move_line.credit:
                ttype = 'dr'
            else:
                ttype = 'cr'
            res.update({
                'account_id': move_line.account_id.id,
                'type': ttype,
                'currency_id': move_line.currency_id and move_line.currency_id.id or move_line.company_id.currency_id.id,
                'amounInvoice':move_line.invoice.amount_total,
                'residualInvoice':move_line.invoice.residual,
            })
        return {
            'value':res,
        }

        
modulo()


