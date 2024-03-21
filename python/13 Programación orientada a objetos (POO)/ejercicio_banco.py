class Cuenta:
    def __init__(self, nombre_titular, saldo, tipo_cuenta):# Metodo constructor
        self.nombre_titular = nombre_titular# Atributo para almacenar el nombre del titular de la cuenta
        self.saldo = saldo# Atributo para almacenar el saldo de la cuenta
        self.tipo_cuenta = tipo_cuenta# Atributo para almacenar el tipo de cuenta
        
    def retirar(self, monto):
        try:
            monto_a_retirar = int(monto)# Convertir el monto de string a entero
            if monto_a_retirar > self.saldo:# Validar si el monto a retirar es mayor al saldo
                print("FONDOS INSUFICIENTES, INTENTA CON UN MONTO MENOR")
            else:
                self.saldo -= monto_a_retirar# Restar el as_monto a retirar al saldo
            return self.saldo # Retornar el saldo de la cuenta
        except ValueError as retirar_error:
            print(f"¡ERROR! INGRESA SOLO VALORES NUMERICOS {retirar_error}")
        
    def depositar(self, monto):
        try:
            monto_a_depositar = int(monto)# # Convertir el monto de string a entero
            if monto_a_depositar < 100:# Validar si el monto a depositar es menor a 100
                print("EL MONTO A DEPOSITAR DEBE SER MAYOR A 100 PESOS")
            else:
                self.saldo += monto_a_depositar# Sumar el as_monto a depositar al saldo
            return self.saldo# Retornar el saldo de la cuenta
        except ValueError as depositar_error:
            print(f"¡ERROR! INGRESA SOLO VALORES NUMERICOS {depositar_error}")
        
    def consultar_saldo(self):
        return self.saldo# Retornar el saldo de la cuenta
    
    def obtener_recibo(self, cuenta):
                    print(f"""
        ------RECIBO DE BANCO SANTANDER------
        **********DATOS DEL TITULAR DE LA CUENTA**********
            Nombre del titular: {self.nombre_titular}
            Numero de cuenta: {cuenta}
            Tipo de cuenta: {self.tipo_cuenta}
            Saldo actual: {self.saldo}
            
        """)
    
# Clase Banco hereda de la clase Cuenta    
class Banco(Cuenta):
    def __init__(self, nombre_titular, saldo, tipo_cuenta):
        super().__init__(nombre_titular, saldo, tipo_cuenta)
        self.cliente = []# Lista para almacenar los clientes
        self.numero_cuenta = ["5488433859170378"]# Lista para almacenar los numeros de cuenta
        self.pin_cuenta = [1191]# Lista para almacenar los PIN de las cuentas
    
    def get_numero_cuenta(self):# Metodo para obtener el numero de cuenta
        return self.numero_cuenta[0]
    
    def validar_cuenta(self, numero_de_cuenta, pin_cuenta):
        print("Ingresa tu cuenta y PIN para continuar")
        while True:
            try:
                numero_de_cuenta = input("Numero de cuenta: ")
                #self.numero_cuenta.append(numero_de_cuenta)# Añadimos numero_de_cuenta como elemento al final de la lista de self.numero_cuenta
                pin_cuenta = int(input("PIN numerico: "))
                #self.pin_cuenta.append(pin_cuenta)#Añadimos pin_cuenta como elemento al final de la lista de self.pin_cuenta
            except ValueError as validar_cuenta_error:
                print(f"Ingresa solo numeros {validar_cuenta_error}")
                continue# Hace que el bucle While se ejecute nuevamente, sin ejecutar el resto del codigo
            
            numero_caracteres_cuenta = len(numero_de_cuenta)# contamos el numero de caracteres que tiene el numero de caracteres que tiene "numero_de_cuenta" y lo guardamos en "numero_caracteres_cuenta"
            if numero_caracteres_cuenta != 16:# Validamos si el "numero_caracteres_cuenta" tiene 16 caracteres        
                print("***¡ERROR!, EL NUMERO DE CUENTA DEBE TENER 16 DIGITOS***")
            # Validamos si numero_de_cuenta y pin_cuenta estan en la lista de self.numero_cuenta y self.pin_cuenta
            if numero_de_cuenta in self.numero_cuenta and pin_cuenta in self.pin_cuenta:
                print("¡LOS DATOS SE VALIDARON DE FORMA EXITOSA!")
                return self.mostrar_menu(0)
            else:
                print("****CUENTA O PIN INCORRECTO, INTENTALO DE NUEVO*****")
                
    def mostrar_menu(self, monto):
        while True:
            print("""
        ------BIENVENIDO A SANTANDER------
        **********MENU PRINCIPAL**********
            1- Retirar
            2- Depositar
            3- Consultar saldo
            4- Consultar saldo
            5- Salir
        """)
            
            opciones_disponibles = [1, 2]# Lista de opciones disponibles
            try:# Validar si la opcion ingresada es un numero
                opcion = int(input("Seleccion una opcion del menu: "))
            except ValueError as mostrar_menu_error:# Mensaje de error
                print(f"¡ERROR! INGRESA SOLO VALORES NUMERICOS {mostrar_menu_error}")
                continue# Hace que el bucle While se ejecute nuevamente, sin ejecutar el resto del codigo
                
            if opcion in opciones_disponibles:# Validar si la opcion seleccionada esta en la lista "opciones_disponibles"
                monto = input("Ingresa el monto: ")# Solicitar el monto
            
            # con match opcion validamos si la opcion seleccionada es igual a 1, 2, 3 o 4
            match opcion:
                case 1:
                    resultado = self.retirar(monto)# Llamando al metodo retirar() pasando el "monto" como argumento
                case 2:
                    resultado = self.depositar(monto)# Llamando al metodo depositar() pasando el "monto" como argumento
                case 3:
                    resultado = self.consultar_saldo()# Llamando al metodo consultar_saldo() que muestra el saldo total de la cuenta
                    print(f"Tu saldo actual es de ${resultado} pesos")
                case 4:
                    #get_numero_cuenta = self.numero_cuenta[0]# Obtenemos el numero de cuenta
                    self.obtener_recibo(self.get_numero_cuenta())# Llamamos al metodo obtener_recibo() pasando como argumento el metodo get_numero_cuenta() que retorna(obtiene) el numero de cuenta
                case 5:
                    print("FIN DEL PROGRAMA, GRACIAS POR UTILIZAR NUESTROS SERVICIOS")
                    exit()#Terminar el programa
                case _:
                    print("OPCION INCORRECTA INTENTA NUEVAMENTE")#Mensaje de error
                                      
#crando instancias de la clase Banco
banco = Banco("Juan", 0, "Ahorro")
banco.validar_cuenta(0, 0)# llamamos al metodo validar_cuenta() pasando 0, 0 como argumentos

# crando instancias de la clase Cuenta
cuenta = Cuenta("Juan", 0, "Ahorro")