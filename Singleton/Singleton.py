from Singleton.Decorador_Singleton import Singleton

@Singleton
class Empleador:

  def __init__(self,g,d,s,f,w):
    self.nombre=g

  @property       
  def getNombre(self):
    return f'Hola me llamo {self.nombre} y soy  Empleador, mi instancia es \n{self}\n'

  @getNombre.setter
  def setNombre(self,value):
    self.nombre=value


if __name__ == "__main__":
    
    OPersona3=Empleador('MARIA')
    OPersona4=Empleador('ANA')
    
    print(OPersona3.getNombre,sep='\n')
    print(OPersona4.getNombre,sep='\n')
    
    print( OPersona3==OPersona4)
    
    OPersona=Empleador()
    OPersona2=Empleador()
    print(OPersona is OPersona2)