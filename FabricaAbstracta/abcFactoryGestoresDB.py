from abc import ABC,abstractmethod

class factoryGestoresDB (ABC):

    def getDB_Relacional(self):
        pass

    def getdb_No_relacional(self):
        pass