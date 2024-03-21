"""
    Crea una clase llamada Cuenta que tenga un atributo llamado saldo un método
    llamado depositar aumente el saldo en una cantidad dada. Luego, crea una
    instancia de la clase y usa el método para depositar una cantidad dada.
"""

class Cuenta:
    def __init__(self, saldo=0):
        self.saldo = saldo

    def depositar(self, deposito, cantidad_maxima):
        self.saldo += deposito
        if deposito > cantidad_maxima:
            print(f"Solo puedes hacer depositos menores a ${cantidad_maxima} pesos")
        else:
            print(f'Deposito exitoso') 
    
    def retirar(self, retiro):
        self.saldo -= retiro
        print(f'Realizaste un retiro de ${self.saldo} pesos')
    
    def consulta_saldo(self, consulta):
        consulta = self.saldo
        print(f'Tu saldo actual es de ${consulta} pesos')
    
    def menu(self):
        opcion = None
        while True:
            print("""
                  -----------------------
                      Menú principal
                  -----------------------
                    1- Depositar
                    2- Retirar
                    3- Consulta de saldo
                    4- Salir 
                    """)
            
            opcion = int(input("Selecciona una opcion: "))
            match opcion:
                case 1:
                    cantidad_maxima = 7000
                    deposito = int(input("Ingresa la cantidad a depositar " + "$"))
                    self.depositar(deposito, cantidad_maxima)
                case 2:
                    retiro = int(input("Ingresa la cantidad a retirar " + "$"))
                    self.retirar(retiro)
                case 3:
                    consulta = 0
                    self.consulta_saldo(consulta)
                case 4:
                    print("¡Fin del programa, Adios!")
                    exit()
                case _:
                    print("¡ Opción incorrecta, intentalo de nuevo !")
cuenta = Cuenta()
cuenta.menu()




  
  
  