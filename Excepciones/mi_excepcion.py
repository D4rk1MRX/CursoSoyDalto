#creando mi excepcion propia
class MiExcepcion(Exception):
    def __init__(self,err):
        print(f"impresionando cometiste este error{err}")
        
    
#lanzando excepcion  
try:
    raise MiExcepcion("Jajaja loco")
except:
    print("como cometeras ese error tan bobo")