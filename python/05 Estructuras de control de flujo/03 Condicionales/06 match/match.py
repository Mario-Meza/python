lenguaje = input("Qué lenguaje deseas aprender? ")

match lenguaje:
    case "JavaScript":
        print("Te puedes convertir en desarrollador web.")
    case "Python":
        print("Te puedes convertir en científico de datos.")
    case "PHP":
        print("Te puedes convertir en desarrollador backend")
    case "Solidity":
        print("Te puedes convertir en desarrollador de blockchain")
    case "Java":
        print("Te puedes convertir en desarrollador móvil.")
    case _:
        print("El lenguaje no importa. Tú puedes hacerlo!")