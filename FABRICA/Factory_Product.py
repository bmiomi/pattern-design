from ABC_Fabricas import FactoryDB_Relacional,FactoryDB_No_Relacional

if __name__ == '__main__':
    
    # se hace el llamado a la instancia que se requiere en caso de no existir  retornara None

    print(FactoryDB_Relacional.getDB_Relacional('SQLSERVER')())

    print('*'*12)

    print(FactoryDB_No_Relacional.getDB_No_Relacional('MONGODB')())

