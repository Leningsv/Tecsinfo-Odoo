#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Importaciones
from datetime import date, datetime, timedelta
from openerp.osv import osv, fields
from openerp import models, fields, api
class GolItemInvoice(osv.Model):
    _name = 'account.invoice.line'
    _inherit = 'account.invoice.line'    
    isProduct=fields.Boolean('Producto',default=True, invisible=True)    
    itemDiscount=fields.Many2one('gol.generic.discount','Descuento')
    amountItemDiscount=fields.Float('Descuento asociado segun el articulo o servicio',compute='_ItemDiscountCalculation')
    #amountAutomaticDiscount=fields.Float('Descuento asociado a un periodo de Tiempo')
    amountCustomerDiscount=fields.Float('Descuento asociado al Cliente')
    amountAutomaticDiscount=fields.Float('DescuentoAutomatico')
    
    amountTotalDiscount=fields.Float('Monto Descuentos',Store=True)
    amountTotalTax=fields.Float('Monto Impuestos',Store=True)
    amountTotal=fields.Float('Total',Storage=True)
    price_unit=fields.Float('Precio Unitatio',Storage=True,compute='_SetPriceUnit')
    
    price_subtotal = fields.Float(string='Amount',
        store=True, readonly=False, compute='_ComputePrice')    
    
    @api.one
    def _ItemDiscountCalculation(self):
        self.amountItemDiscount=(self.price_unit*self.quantity)*(self.itemDiscount.value*0.01)
    
    @api.onchange('price_unit','quantity','itemDiscount','customerDiscount','automaticDiscount','amountTotalDiscount')
    def TotalDiscountCalculation(self):
        self.amountTotalDiscount=(self.price_unit*self.quantity)*(self.itemDiscount.value*0.01)          
    
    @api.onchange('price_subtotal','invoice_line_tax_id','amountTotalTax')
    def TotalTaxCalculation(self):
        totalTax=0;
        for tax in self.invoice_line_tax_id:
            totalTax=self.price_subtotal*tax.amount+totalTax
        self.amountTotalTax=totalTax
            
    @api.onchange('price_subtotal','amountTotalTax','amountTotal')
    def TotalAmountCalculation(self):
        self.amountTotal=self.price_subtotal+self.amountTotalTax
    
    @api.one
    def _SetPriceUnit(self):
        if self.isProduct == False:
            self.price_unit = self.price_subtotal/ self.quantity
        if self.isProduct == True:
            self.price_unit=self.product_id.list_price     

    @api.onchange('quantity','price_unit','amountTotalDiscount','price_subtotal')
    def SubtotalCalculation(self):
        self.price_subtotal=(self.price_unit*self.quantity)-self.amountTotalDiscount
    @api.one
    def _ComputePrice(self):
        self.price_subtotal=(self.price_unit*self.quantity)-self.amountTotalDiscount
    
    ''' Con este metodo hago editables o solo lectura los campos de los articulos que 
    conforman la factura, el resto de la logica se encuentra en la vista'''

GolItemInvoice()









