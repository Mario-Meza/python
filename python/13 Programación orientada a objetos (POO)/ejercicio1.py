class Motocicleta:
    estado = "nueva"
    motor = False
    precio = 0
    def __init__(self, color, cobsutible_litros, numero_ruedas, marca, modelo, fecha_fabricacion, velocidad_punta, peso):
        self.color = color
        self.cobsutible_litros = cobsutible_litros
        self.numero_ruedas = numero_ruedas
        self.marca = marca
        self.modelo = modelo
        self.fecha_fabricacion = fecha_fabricacion
        self.velocidad_punta = velocidad_punta
        self.peso = peso
        
    def arrancar(self):
        self.precio = 20700
        if self.motor == False:
            print("Arrancando motor")
        elif self.motor == True:
            print("El motor ya está encendido")
            
    
    def detener(self):
        self.precio = 30000
        if self.motor == True:
            print("Motor detenido")
        elif self.motor == False:
            print("El motor ya está apagado")
            
    def consultar_precio(self):
        print(f"EL precio de la motocicleta modelo {self.marca} es de ${self.precio} pesos")

        
            
motocicleta1 = Motocicleta("Rojo", 10, 2, "Italika",2021, 2021, 120, 150)
motocicleta1.arrancar()
motocicleta1.consultar_precio()
#print(f"EL precio de la motocicleta modelo {motocicleta1.marca} es de ${motocicleta1.precio} pesos")

motocicleta2 = Motocicleta(color="Amarilla",cobsutible_litros=11,numero_ruedas=4,marca="Honda",modelo=2020,fecha_fabricacion=2021,velocidad_punta=250,peso=150)
motocicleta2.detener()
motocicleta2.consultar_precio()

    
    