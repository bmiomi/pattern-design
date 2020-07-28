class Singleton:

  __instance=None
  count=0
  
  def __new__(cls,s,*args, **kwargs): 
    print('Estoy creando la instancia')
    if cls.__instance == None:
        cls.__instance=super(Singleton, cls).__new__(cls,*args, **kwargs) 
    return cls.__instance
    
  def __init__(self,fun):
    self.fu=fun

  def __call__(self, *args, **kwargs):
    self.count+=1
    print(f'llamada {self.count} instancia {self}')
