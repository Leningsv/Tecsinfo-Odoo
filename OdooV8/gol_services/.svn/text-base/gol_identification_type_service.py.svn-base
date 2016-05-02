
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Importaciones
# Configuramos

from __builtin__ import int
class GolIdentificationTypeService():
    
    
    def ValidateIdentificationSize(self,objtest, idIdentificationType,identificationNumber): 
        #rec = self.GetIdentificationTypeByID(idIdentificationType)            
        rec= objtest.search([('id', '=', idIdentificationType)])
        if(len(identificationNumber)==int(rec.charactersAmount)):
            return True  
        return False
    
    def ValidateIdentificationType(self,objtest, idIdentificationType,identificationNumber): 
        #Busqueda del typo de identificaion en funcion del ID 
        #Asignacion a variable el objeto encontrado         
        identificationType= objtest.search([('id', '=', idIdentificationType)])
        
        if(str(identificationType.validationType) == 'numerical'):
            if(str(identificationNumber).isdigit()== True):
                return True
            return False
        if(str(identificationType.validationType) == 'characters'):
            if(str(identificationNumber).isalpha() == True):
                return True
            return False
        if(str(identificationType.validationType) == 'mixed'):
            if(str(identificationNumber).isalnum() == True):
                return True
            return False
    def ValidateIdentificationType1(self,objtest, idIdentificationType,identificationNumber): 
        #Busqueda del typo de identificaion en funcion del ID 
        #Asignacion a variable el objeto encontrado         
        self.identificationType=self.env['gol.identification.type'].search([('id', '=', idIdentificationType)])
        
        if(str(self.identificationType.validationType) == 'numerical'):
            if(str(identificationNumber).isdigit()== True):
                return True
            return False
        if(str(self.identificationType.validationType) == 'characters'):
            if(str(identificationNumber).isalpha() == True):
                return True
            return False
        if(str(self.identificationType.validationType) == 'mixed'):
            if(str(identificationNumber).isalnum() == True):
                return True
            return False
            
        
        

       
        

    