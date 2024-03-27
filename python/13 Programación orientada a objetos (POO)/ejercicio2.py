#creame una clase del juego llamado ahorcado
class Ahorcado:
    def __init__(self):
        self.palabra_correcta = "elote"
        self.palabra_guiones_bajos = ["_"] * len(self.palabra_correcta)
        self.contador_intentos = 0
        self.cantidad_intentos = 5
        
    def comprobar_letra(self,letra_input, palabra_correcta, palabra_guiones_bajos):
        encontrada = False
        for position, value in enumerate(palabra_correcta):
            if letra_input == value:# si la letra ingresada es igual a la letra en la posicion de la palabra correcta
                palabra_guiones_bajos[position] = letra_input# la letra ingresada se agrega a la lista de guiones bajos en la posicion de la palabra correcta
                encontrada = True
        
        return encontrada
    
    def mensaje_error(self, letra_input):
        print(f"¡LETRA INCORRECTA, INTENTA DE NUEVO! La letra '{letra_input}' no está en la palabra.")
        
    def jugar(self):
        while self.contador_intentos < self.cantidad_intentos:#mientras el contador de intentos sea menor a la cantidad de intentos
            letra_input = input("\nIngresa una letra: ").lower()#se pide al usuario que ingrese una letra y se convierte a minusculas

            if letra_input in self.palabra_correcta:#si la letra ingresada esta en la variable "palabra_correcta"
                self.comprobar_letra(letra_input, self.palabra_correcta, self.palabra_guiones_bajos)
            else:
                self.mensaje_error(letra_input)#llamo al metodo mensaje_error y le paso como argumento la letra ingresada, letra_input
                self.contador_intentos += 1#se suma 1 al contador de intentos
                print(f"Te quedan {self.cantidad_intentos - self.contador_intentos} intentos")

                
            print(' '.join(self.palabra_guiones_bajos))# se imprime la palabra con guiones bajos
       
            # Comprobando si la palabra ya fue adivinada
            if "".join(self.palabra_guiones_bajos) == self.palabra_correcta:#si la palabra con guiones bajos es igual a la palabra correcta
                print("¡FELICIDADES, GANASTE!")
                return#se termina el juego
                
        print("¡PERDISTE!")
            
                    
ahorcado = Ahorcado()
ahorcado.jugar()

        
        
        
            
        