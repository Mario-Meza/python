class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, otro):
        return Vector2D(self.x + otro.x, self.y + otro.y)
    
v1 = Vector2D(1,2)
v2 = Vector2D(3,4)
v3 = v1 + v2
print(v3.x, v3.y)

print([1,2].__add__([3,4]))