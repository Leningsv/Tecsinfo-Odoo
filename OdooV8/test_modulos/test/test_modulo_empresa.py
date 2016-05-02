'''
Created on 11 de dic. de 2015

@author: Milton
'''
import unittest


class Test(unittest.TestCase):

    def testRegistrarEmpresaParametrosCorrectos(self):
        self.assertEquals('Parametros ingresados Correctamente')
        #pass
    def testRegistrarEmpresaParametrosIncorrectos(self):
        self.assertEquals('Parametros ingresados Incorrectos')
        #pass    
    
    def registrarContacto(self):
        self.assertEquals('ContactoRegistrado')
        
    def registrarContactofallido(self):
        self.assertEquals('ContactoRegistradoFallido')
        
    def registrarSucursal(self):
        self.assertEquals('ContactoRegistrado')
        
    def registrarSucursalFallido(self):
        self.assertEquals('ContactoRegistrado')
        
    def registrarPuntoVentaCredito(self):
        self.assertEquals('Exito')
    
    def registrarPuntoVentaFallido(self):
        self.assertEquals('Falla')
    
    def registrarDocumento(self):
        self.assertEquals('Exito')
    
    def registrarDocumentoFallido(self):
        self.assertEquals('Falla')
        
    def registrarIdentificacion(self):
        self.assertEquals('Exito')
    
    def registrarIdentificacionFallido(self):
        self.assertEquals('Falla')
    
    def registrarRepresentanteLegal(self):
        self.assertEquals('Exito')
    
    def registrarRepresentanteLegalFallido(self):
        self.assertEquals('Falla')
        
    def registrarObligacionTributaria(self):
        self.assertEquals('Exito')
    
    def registrarObligacionTributariaFallido(self):
        self.assertEquals('Falla')
    
    def registrarContador(self):
        self.assertEquals('Exito')
    
    def registrarContadorFallido(self):
        self.assertEquals('Falla')
    
    def registrarCuentasBanco(self):
        self.assertEquals('Exito')
    
    def registrarCuentasBancoFallido(self):
        self.assertEquals('Falla')
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()