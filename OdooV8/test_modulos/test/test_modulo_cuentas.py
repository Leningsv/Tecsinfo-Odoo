import unittest
class TestModuloCuentas(unittest.TestCase):


    def testRegistrarCuentaParametrosCorrectos(self):
        self.assertEquals('Parametros ingresados Correctamente')
        #pass
    def testRegistrarCuentaParametrosIncorrectos(self):
        self.assertEquals('Parametros ingresados Incorrectos')
        #pass    
    
    def registrarCuentasBanco(self):
        self.assertEquals('Exito')
        
    def registrarCuentaBancofallido(self):
        self.assertEquals('Falla')
        
    def registrarProrrateo(self):
        self.assertEquals('Exito')
        
    def registrarProrrateoFallido(self):
        self.assertEquals('Falla')
        
    def registrarOrdenador(self):
        self.assertEquals('Exito')
    
    def registrarOrdenadorFallido(self):
        self.assertEquals('Falla')
    
    def registrarClasificador(self):
        self.assertEquals('Exito')
    
    def registrarClasificadorFallido(self):
        self.assertEquals('Falla')
        
    def registrarTipoCuenta(self):
        self.assertEquals('Exito')
    
    def registrarTipoCuentaFallido(self):
        self.assertEquals('Falla')
    
    def registrarModuloAsociado(self):
        self.assertEquals('Exito')
    
    def registrarModuloAsociadoFallido(self):
        self.assertEquals('Falla')
        
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()