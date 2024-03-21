def saludo(palabra):
    if palabra.startswith("Hola"):
        return "Hola"
    elif palabra.startswith("Adios"):
        return "Adios"
    else:
        return "No inicia con Hola ni Adios"

resultado_busqueda = saludo("Adios amigo como estas")
print(resultado_busqueda) 






 
  
  