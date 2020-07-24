from abc import ABC,abstractmethod,abstractproperty

class GESTORDB_NO_RELACIONAL(ABC):

    @abstractmethod
    def Namedb(self):
        pass

class MONGODB (GESTORDB_NO_RELACIONAL):
    
    def Namedb(self):
        print('Tu conexion con ma base de datos MONGODB fue EXITOSA')

    def __str__(self):
        return('Instancia de tipo MONGODB')

class MARIADB (GESTORDB_NO_RELACIONAL):
    
    def Namedb(self):
        print('Tu conexion con ma base de datos MARIADB fue EXITOSA')


    def __str__(self):
        return('Instancia de tipo MARIADB')
