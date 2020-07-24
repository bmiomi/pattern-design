from ABC_Fabricas import FactoryDB_Relacional,FactoryDB_No_Relacional
class Factory_Product:

    __dic={'DBRELACIONAL':FactoryDB_Relacional,'DBNORELACIONAL':FactoryDB_No_Relacional}

    @staticmethod
    def getfabrica(type):
        return Factory_Product.__dic.get(type)

if __name__ == '__main__':

    ObDBR=Factory_Product.getfabrica('DBRELACIONAL')
    print(ObDBR.getDB_Relacional('SQLSERVER')())    

    print('*'*12)

    OBDBNR=Factory_Product.getfabrica('DBNORELACIONAL')
    print(OBDBNR.getDB_No_Relacional('MARIADB')())    

