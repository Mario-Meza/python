class Persona:
    """
        Una clase que representa a una persona.
    """
    def __init__(self, nombre, edad, estado, sexo):
        """__summary__
            Constructor de la clase Persona.

        Args:
            nombre (str): Nombre de la persona.
            edad (int): Edad de la persona.
            estado (str): Estado de residencia de la persona.
            sexo (str): Sexo de la persona.
        """
        self.nombre = nombre
        self.edad = edad
        self.estado = estado
        self.sexo = sexo

    def saludar(self):
        """_summary_
            Metodo que retorna un saludo personalizado
        
        Args:
            None
        Returns:
            str: Un saludo que incluye el nombre y la edad de la persona
        """
        return f'Hola mi nombre es {self.nombre} y tengo {self.edad} años de edad'
    
    def hablar(self, otra_persona):
        """_summary_
            Metodo que simula la conversacion con otra persona
        Args:
            otra_persona (Persona): El objeto Persona con el que se va a tener la conversación.

        Returns:
            str: Un texto que simula la conversación.
        """
        return f'Mi nombre es {self.nombre} y estoy habalndo con {otra_persona.nombre}'
    
# Creando instancias de la clase Persona    
persona_l = Persona("Juan",23,"Hidalgo","Masculino")
persona_2 = Persona("Andres", 27, "Mexico","Masculino")

# Llamando a los métodos de las instancias
pintar_persona1 = persona_l.saludar()
pintar_persona2 = persona_2.hablar(persona_l)

print(pintar_persona1)
print(pintar_persona2)
