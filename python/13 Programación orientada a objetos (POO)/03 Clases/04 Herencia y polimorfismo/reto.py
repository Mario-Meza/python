"""
Crea una clase Gato que herede de la clase Animal y que tenga un método hablar()
que imprima Miau, soy un gato y me llamo [nombre].
"""

class Calculadora:        
    def sumar(self, numero1, numero2):
        return numero1 + numero2
    
    def restar(self, numero1, numero2):
        return numero1 - numero2
        
    def multiplicar(self, numero1, numero2):
        return numero1 * numero2
    
    def dividir(self, numero1, numero2):
        return numero1 / numero2
    
    def menu(self):
        opcion = 0
        lista_opciones_validas = [1,2,3,4]
        while True:
            print("""
                  1- Suma
                  2- Resta
                  3- Multiplicacion
                  4- Division
                  5- Salir
                  """)
            opcion = int(input("Selecciona una opcion del Menú: "))
            if opcion in lista_opciones_validas:
                numero1 = int(input("Ingresa el primer número: "))
                numero2 = int(input("Ingresa el segundo número: "))
            
            match opcion:
                case 1:
                    resultado = self.sumar(numero1, numero2)
                    print("Resultado: ", resultado)
                case 2:
                    resultado = self.restar(numero1, numero2)
                    print("Resultado: ", resultado)
                case 3:
                    resultado = self.multiplicar(numero1, numero2)
                    print("Resultado: ", resultado)
                case 4:
                    resultado = self.dividir(numero1, numero2)
                    print("Resultado: ", resultado)
                case 5:
                    print("Fin del programa")
                    exit()
                case _:
                    print("Opcion invalida")
                
calculo = Calculadora()
calculo.menu()