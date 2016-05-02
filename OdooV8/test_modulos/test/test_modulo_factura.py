'''
Created on 11 de dic. de 2015

@author: Milton
'''
import unittest

class FacturaTestCase(unittest.TestCase):
    
    def ResgistrarFacturaParametrosCorrectos(self):
        self.assertEqual('parametros ingresados correctos')
                
    def ResgistrarFacturaParametrosIncorrectos(self):
        self.assertEqual('parametros ingresados incorrectos')

#class RegistrarItemFactura(unittest.TestCase):
    
    def RegistrarItemFacturaParametrosCorrectos(self):
        self.assertEquals('paramtros ingresados correctos')
               
    def RegistrarItemFacturaParametrosIncorrectos(self):
        self.assertEquals('paramtros ingresados incorrectos')

#class CalculoSubtotal(unittest.TestCase):

    def CalculoSubtotalOperacionExitosa(self):
        self.assertEquals('exito')
        
    def CalculoSubtotalOperacionFallido(self):
        self.assertEquals('operacion Fallida')
        
#class CalculoDescuento(unittest.TestCase):

    def CalculoDescuentoCalculoDescuentoOperacionExitosa(self):
        self.assertEquals('exito')
        
    def CalculoDescuentoCalculoDescuentoOperacionFallido(self):
        self.assertEquals('operacion Fallida')
        
#class CalculoDescuentoCliente(unittest.TestCase):
    def CalculoDescuentoClienteOperacionExitosa(self):
        self.assertEquals('exito')
        
    def CalculoDescuentoClienteOperacionFallido(self):
        self.assertEquals('operacion Fallida')
        
#class CalculoDescuentoAutomatico(unittest.TestCase):
    def CalculoDescuentoAutomaticoOperacionExitosa(self):
        self.assertEquals('exito')
        
    def CalculoDescuentoAutomaticoOperacionFallido(self):
        self.assertEquals('operacion Fallida')
        
#class CalculoDescuentoTotal(unittest.TestCase):
    def CalculoDescuentoTotalOperacionExitosa(self):
        self.assertEquals('exito')
        
    def CalculoDescuentoTotalOperacionFallido(self):
        self.assertEquals('operacion Fallida')
        
#class CalculoImpuesto(unittest.TestCase):
    def CalculoImpuestoOperacionExitosa(self):
        self.assertEquals('exito')
        
    def CalculoImpuestoOperacionFallido(self):
        self.assertEquals('operacion Fallida')
        
#class CalculoImpuestoTotal(unittest.TestCase):
    def CalculoImpuestoTotalOperacionExitosa(self):
        self.assertEquals('exito')
        
    def CalculoImpuestoTotalOperacionFallido(self):
        self.assertEquals('operacion Fallida')

#class CalculoValorTotal(unittest.TestCase): 
    def CalculoValorTotalOperacionExitosa(self):
        self.assertEquals('exito')
        
    def CalculoValorTotalOperacionFallido(self):
        self.assertEquals('operacion Fallida')
        
    def EjecutarEventoGeneralComprovate(self):
        self.assertEquals("Envento Generar Comprobante exitoso")
        
    def registrarIdentifiacion(self):
        self.assertEquals('Exito')
        
    def registrarIdentificacionFallido(self):
        self.assertEquals('Falla')
        
    def registrarDocumento(self):
        self.assertEquals('Exito')
        
    def registrarDocumentoFallido(self):
        self.assertEquals('Falla')

    def registrarDescuentoGenerico(self):
        self.assertEquals('Exito')
        
    def registrarDescuentoGenericoFallido(self):
        self.assertEquals('Falla')
        
    def registrarDescuentoCliente(self):
        self.assertEquals('Exito')
        
    def registrarDescuentoClienteFallido(self):
        self.assertEquals('Falla')  
        
    def registrarDescuentoAutomatico(self):
        self.assertEquals('Exito')
        
    def registrarDescuentoAutomaticoFallido(self):
        self.assertEquals('Falla')  
        
    def registrarImpuesto(self):
        self.assertEquals('Exito')
        
    def registrarImpuestoFallido(self):
        self.assertEquals('Falla')
        
    def registrarImpuestoISE(self):
        self.assertEquals('Exito')
        
    def registrarImpuestoISEFallido(self):
        self.assertEquals('Falla')
        
    def registrarProducto(self):
        self.assertEquals('Exito')
        
    def registrarProductoFallido(self):
        self.assertEquals('Falla')
        
              
                  
if __name__ == '__main__':
    unittest.main()