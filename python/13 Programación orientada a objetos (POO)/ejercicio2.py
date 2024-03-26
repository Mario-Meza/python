#creame una clase del juego llamado ahorcado
class Ahorcado:
    def __init__(self):
        self.palabra_correcta = "elegante"
        self.palabra_save = []
        self.palabra_guiones_bajos = ["_"] * len(self.palabra_correcta)


    def mostrar_palabra(self):
       for letra in self.palabra_save:
            print(letra, end=" ")  
        
    def jugar(self):
        while True:
            letra_input = input("\nIngresa una letra: ")

            if letra_input in self.palabra_correcta:
                self.palabra_save.append(letra_input)
            else:
                print("¡LETRA INCORRECTA!")
            
           
            #ahorcado = self.preguntar_letras()

            for pos, val in enumerate(self.palabra_correcta):
                if letra_input == val:
                    self.palabra_guiones_bajos[pos] = letra_input
                
            print(' '.join(self.palabra_guiones_bajos))
        
            #self.mostrar_palabra()

        
ahorcado = Ahorcado()
ahorcado.jugar()

        
        
        
            
        