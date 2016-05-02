'''
Created on 11 de dic. de 2015

@author: Milton
'''
import unittest


class TestModuloNotaCredito(unittest.TestCase):
       
    def IngresarDatosFiltroFactura(self):
        self.assertEquals('Exito')
    
    def IngresarDatosFiltroFacturaFallido(self):
        self.assertEquals('Falla')
    
    def ValidarFiltroFacturas(self):
        self.assertEquals('Exito')
    
    def ValidarFiltroFacturasFallido(self):
        self.assertEquals('Falla')
        
    def DesplegarFactura(self):
        self.assertEqual('Exito')
    
    def DesplegarFacturaFallido(self):
        self.assertEqual('Falla')
            
    def ValidarDatosTablaFactura(self):
        self.assertEquals('Exito')
    
    def ValidarDatosTablaFacturaFallido(self):
        self.assertEquals('Falla')
    
    def SeleccionarFacturaparaNotaCredito(self):
        self.assertEquals('Exito')
    
    def SeleccionarFacturaparaNotaCreditoFallido(self):
        self.assertEquals('Falla')
                
    def CargarDatosFacturaParaLaNotaCredito(self):
        self.assertEquals('exito')
        #pass
    def CargarDatosFacturaParaLaNotaCreditoFallido(self):
        self.assertEquals('Falla')
        #pass    
    
    def ValidarAlterarItemsFactura(self):
        self.assertEquals('exito')
        #pass
    def ValidarAlterarItemsFacturaFallido(self):
        self.assertEquals('Falla')
        #pass    
    
    def ValidarAlteracionEstadoFactura(self):
        self.assertEquals('exito')
        #pass
        
    def ValidarAlteracionEstadoFacturaFallido(self):
        self.assertEquals('Falla')
        
    
    def RegistrarItemsDevueltos(self):
        self.assertEquals('Exito')
        
    def RegistrarItemsDevueltosFallido(self):
        self.assertEquals('Falla')
    
    #########################
    
    def ValidarCalculoSubtotal(self):
        self.assertEquals('Exito')
        
    def ValidarCalculoSubtotalFallido(self):
        self.assertEquals('Falla')
        
    def ValidarCalculoDescuento(self):
        self.assertEquals('Exito')
        
    def ValidarCalculoDescuentoFallido(self):
        self.assertEquals('Falla')
        
    def ValidarCalculoDescuentoCliente(self):
        self.assertEquals('Exito')
        
    def ValidarCalculoDescuentoClienteFallido(self):
        self.assertEquals('Falla')
        
    def ValidarCalculoDescuentoAutomatico(self):
        self.assertEquals('Exito')
        
    def ValidarCalculoDescuentoAutomaticoFallido(self):
        self.assertEquals('Falla')
    
    def ValidarCalculoDescuentoTotal(self):
        self.assertEquals('Exito')
        
    def ValidarCalculoDescuentoTotalFallido(self):
        self.assertEquals('Falla')
        
    def ValidarCalculoImpuestos(self):
        self.assertEquals('Exito')
        
    def ValidarCalculoImpuestosFallido(self):
        self.assertEquals('Falla')
        
    def ValidarCalculoValorTotal(self):
        self.assertEquals('Exito')
        
    def ValidarCalculoValorTotalFallido(self):
        self.assertEquals('Falla')

    #####################
    
    def ValidarReversoComprobanteContableFactura(self):
        self.assertEquals('Exito')
    
    def ValidarReversoComprobanteContableFacturaFallido(self):
        self.assertEquals('Falla')
        
    def ValidarGenerarComprobanteContable(self):
        self.assertEquals('Exito')
    
    def ValidarGenerarComprobanteContableFallido(self):
        self.assertEquals('Falla')
       
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()