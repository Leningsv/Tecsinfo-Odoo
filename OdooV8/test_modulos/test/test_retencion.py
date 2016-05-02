'''
Created on 11 de dic. de 2015

@author: Milton
'''
import unittest


class TestModuloRetencion(unittest.TestCase):


  
        
    def ingresarDatosFiltroFactura(self):
        self.assertEquals('Exito')
    
    def ingresarDatosFiltroFacturaFallido(self):
        self.assertEquals('Falla')
    
    def ValidarFiltroFacturas(self):
        self.assertEquals('Exito')
    
    def ValidarFiltroFacturasFallido(self):
        self.assertEquals('Falla')
        
    def CargarDatosTablaFactura(self):
        self.assertEquals('Exito')
    
    def CargarDatosTablaFacturaFallido(self):
        self.assertEquals('Falla')
    
    def SeleccionFacturaTablaFactura(self):
        self.assertEquals('Exito')
    
    def SeleccionFacturaTablaFacturaFallido(self):
        self.assertEquals('Falla')
                
    def CargarDatosFacturaParaLaRetencion(self):
        self.assertEquals('Parametros ingresados Correctamente')
        #pass
    def CargarDatosFacturaParaLaRetencionFallida(self):
        self.assertEquals('Parametros ingresados Incorrectos')
        #pass    
    
    def registrarRetencion(self):
        self.assertEquals('Exito')
        
    def registrarRetencionfallido(self):
        self.assertEquals('Falla')
        
    def CalcularTotalRetenciones(self):
        self.assertEquals('Exito')
        
    def CalcularTotalRetencionesFallido(self):
        self.assertEquals('Falla')
    
    def registrarRetencionesTabla(self):
        self.assertEquals('Exito')
        
    def registrarRetencionesTablafallido(self):
        self.assertEquals('Falla')
        
    def CalcularValorRetencion(self):
        self.assertEquals('Exito')
        
    def CalcularValorRetencionFallido(self):
        self.assertEquals('Falla')
        
    def registrarRetenciones(self):
        self.assertEquals('Exito')
        
    def registrarRetencionesfallido(self):
        self.assertEquals('Falla')
        
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()