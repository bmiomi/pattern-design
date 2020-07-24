from abcFactoryGestoresDB import factoryGestoresDB
from Gestores_Relacionales import POSGRESS,SQLSERVER,MYSQL
from Gestores_No_Relacionales import MARIADB,MONGODB


class FactoryDB_Relacional(factoryGestoresDB):
    
    __dic={'POSGRESS':POSGRESS,'SQLSERVER':SQLSERVER,'MYSQL':MYSQL}
    
    @staticmethod
    def getDB_Relacional(type):
        return FactoryDB_Relacional.__dic.get(type)  

    @staticmethod
    def getDB_No_Relacional(type):
        return None
        

class FactoryDB_No_Relacional(factoryGestoresDB):
    
    __dic={'MONGODB':MONGODB,'MARIADB':MARIADB}

    @staticmethod
    def getDB_Relacional(type):
        return None  

    @staticmethod
    def getDB_No_Relacional(type):
        return FactoryDB_No_Relacional.__dic.get(type)
