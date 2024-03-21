
"""
    - nonelocal se utiliza para para hacer referencia a una variable en el ambito que lo envuelve (enclosing) es decir un ambito superior que no es el ambito global.
      Cuando se declara una variable dentro de una funcion esta se considera una variable local y solo esta disponible dentro de la funcion.
      Sin enbargo si se necesita acceder a una variable en un ambito que lo envuelve(aenclosing) desde dentro de una funcion anidada, es necesario declarar esa variable como no local
      usando la palabra clave "nonlocal".De lo contrario Python creara una variable local con el mismo nombre en lugar de acceder a la variable no local.
"""
variableGlobal = 5

def functionPadre():
    variableGlobal = 10

    def functionAnidada():

        variableGlobal = 15
        print(f'function anidada {variableGlobal}')
    
    functionAnidada()
    print("funcion externa",variableGlobal)

functionPadre()
print("Global", variableGlobal)
    

    
    
    