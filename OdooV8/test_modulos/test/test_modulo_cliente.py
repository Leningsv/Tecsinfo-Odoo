'''
Created on 11 de dic. de 2015

@author: Milton
'''
import unittest


class TestModuloCliente(unittest.TestCase):


    def testRegistrarClienteParametrosCorrectos(self):
        self.assertEquals('Parametros ingresados Correctamente')
        #pass
    def testRegistrarClienteParametrosIncorrectos(self):
        self.assertEquals('Parametros ingresados Incorrectos')
        #pass    
    
    def registrarContactoCobro(self):
        self.assertEquals('ContactoRegistrado')
        
    def registrarContactoCobrofallido(self):
        self.assertEquals('ContactoRegistradoFallido')
        
    def registrarContacto(self):
        self.assertEquals('ContactoRegistrado')
        
    def registrarContactoFallido(self):
        self.assertEquals('ContactoRegistrado')
        
    def registrarContactoCredito(self):
        self.assertEquals('Exito')
    
    def registrarContactoCreditoFallido(self):
        self.assertEquals('Falla')
    
    def registrarIdentificacion(self):
        self.assertEquals('Exito')
    
    def registrarIdentificaionFallido(self):
        self.assertEquals('Falla')
        
    def registrarDescuentoCliente(self):
        self.assertEquals('Exito')
    
    def registrarDescuentoClienteFallido(self):
        self.assertEquals('Falla')
    
    def registrarVerificarRetencion(self):
        self.assertEquals('Exito')
    
    def registrarVerificarRetencionFallido(self):
        self.assertEquals('Falla')
        
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()