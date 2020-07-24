from abc import ABC, abstractmethod

class GESTOR_DB_RELACIONAL (ABC):

    @abstractmethod
    def NAmeDB(self):
        pass

class POSGRESS (GESTOR_DB_RELACIONAL):

    def NAmeDB(self):
        print('Tu conexion con ma base de datos POSGRESS fue EXITOSA')
    
    
    def __str__(self):
        return str('Instancia de tipo POSSGRESS')

class SQLSERVER (GESTOR_DB_RELACIONAL):
    
    def NAmeDB(self):
        print('Tu conexion con ma base de datos SQLSERVER fue EXITOSA')
    
    def __str__(self):
        return str('Instancia de tipo SQLSERVER')

class MYSQL (GESTOR_DB_RELACIONAL):
    
    def NAmeDB(self):
        print('Tu conexion con ma base de datos MYSQL FUE EXITOSA')

    def __str__(self):
        return str('Instancia de tipo MYSQL')
