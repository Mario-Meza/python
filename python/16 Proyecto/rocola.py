import random

class Rocola:
    def __init__(self):
        self.temas = [
            'Stairway to Heaven',
            'Light My Fire',
            'No me dejan salir',
            'Persiana Americana',
            'Eres',
            'Strobe',
            'Bangarang',
            'Pink Venom'
        ]
        self.queue = []

    def play(self, k):
        if len(self.queue) >= k:
            primero = self.queue.pop(0)
            self.temas.append(primero)
        indiceRandom = random.randint(0, len(self.temas) - 1)
        tema = self.temas.pop(indiceRandom)
        self.queue.append(tema)
        return tema
    
rocola = Rocola()
print(rocola.play(4), rocola.queue)
print(rocola.play(4), rocola.queue)
print(rocola.play(4), rocola.queue)
print(rocola.play(4), rocola.queue)
print(rocola.play(4), rocola.queue)
print(rocola.play(4), rocola.queue)
print(rocola.play(4), rocola.queue)
print(rocola.play(4), rocola.queue)