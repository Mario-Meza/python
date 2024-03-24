class Cuenta:
    # Constantes de la clase
    NUMERO_CARACTERES_CUENTA = 16 
    NUMERO_CARACTERES_PIN = 4
    # Constructor de la clase y atributos de la clase
    def __init__(self, nombre_titular, saldo, tipo_cuenta):
        self.nombre_titular = nombre_titular
        self.saldo = saldo
        self.tipo_cuenta = tipo_cuenta
        self.numero_cuenta = ["5488433859170378"]
        self.pin_cuenta = 1191
        
    def validar_cuenta(self):
        print("Ingresa tu cuenta y PIN para continuar")
        while True:
            try:
                cuenta = input("Numero de cuenta: ")
                #self.numero_cuenta.append(numero_de_cuenta)
                pin = int(input("PIN numerico: "))
                #self.pin_cuenta.append(pin_cuenta)
            except ValueError as validar_cuenta_error:
                print(f"Ingresa solo numeros {validar_cuenta_error}")
                continue
            
            numero_caracteres_cuenta = len(cuenta)
            numero_caracteres_pin = len(str(pin))

            if numero_caracteres_cuenta != self.NUMERO_CARACTERES_CUENTA:        
                print("***¡ERROR!, EL NUMERO DE CUENTA DEBE TENER 16 DIGITOS***")
            elif numero_caracteres_pin != self.NUMERO_CARACTERES_PIN:
                print("***¡ERROR, EL PIN DEBE SER DE 4 DIGITOS UNICAMENTE!")
            elif cuenta in self.numero_cuenta and pin == self.pin_cuenta:
                print("¡LOS DATOS SE VALIDARON DE FORMA EXITOSA!")
                return self.mostrar_menu(0,0)
            else:
                print("****CUENTA O PIN INCORRECTO, INTENTALO DE NUEVO*****")
                
    def retirar(self, monto):
        try:
            monto_a_retirar = int(monto)
            if monto_a_retirar > self.saldo:
                print("FONDOS INSUFICIENTES, INTENTA CON UN MONTO MENOR")
            else:
                self.saldo -= monto_a_retirar
            return self.saldo
        except ValueError as retirar_error:
            print(f"¡ERROR! INGRESA SOLO VALORES NUMERICOS {retirar_error}")
        
    def depositar(self, monto):
        try:
            monto_a_depositar = int(monto)
            if monto_a_depositar < 100:
                print("EL MONTO A DEPOSITAR DEBE SER MAYOR A 100 PESOS")
            else:
                self.saldo += monto_a_depositar
            return self.saldo
        except ValueError as depositar_error:
            print(f"¡ERROR! INGRESA SOLO VALORES NUMERICOS {depositar_error}")

    def get_recibo(self):
                    print(f"""
        ----------RECIBO DE BANCO SANTANDER---------------
        **********DATOS DEL TITULAR DE LA CUENTA**********
            Nombre del titular: | {self.nombre_titular}
            Numero de cuenta:   | {self.numero_cuenta[0]}
            Tipo de cuenta:     | {self.tipo_cuenta}
            Saldo Total: $      | {self.saldo} pesos
            Pin nuevo:          | {self.pin_cuenta}
        """)
    
    def change_pin(self):
        old_pin = int(input("Ingresa tu pin actual: "))
        if old_pin == self.pin_cuenta:
            new_pin1 = int(input("Ingresa tu nuevo PIN: "))
            new_pin2 = int(input("Confirma tu nuevo PIN: "))
            
            if new_pin2 == new_pin1:
                self.pin_cuenta = new_pin2
                
                print(f"¡PIN SE CAMMBIO DE MANERA CORRECTA, POR SEGURIDAD VUELVE A INICIAR SESION!")
                
                return self.validar_cuenta()
        else:
            print("Tu pin no coincide, intentalo de nuevo")
            
            
                
    def mostrar_menu(self, monto, opcion):
        while True:
            print("""
                  ------BIENVENIDO A SANTANDER------
                  **********MENU PRINCIPAL**********
                  1- Retirar
                  2- Depositar
                  3- Consultar saldo
                  4- Imprimir recibo
                  5- Cambiar PIN
                  5- Salir
                  """)
            opciones_disponibles = [1, 2]
            
            try:
                opcion = int(input("Seleccion una opcion del menu: "))
            except ValueError as mostrar_menu_error:
                print(f"¡ERROR! INGRESA SOLO VALORES NUMERICOS {mostrar_menu_error}")
                continue
                
            if opcion in opciones_disponibles:
                monto = input("Ingresa el monto: ")
            
            match opcion:
                case 1:
                    self.retirar(monto)
                case 2:
                    self.depositar(monto)
                case 3:
                    print(f"Tu saldo actual es de ${self.saldo} pesos")
                case 4:
                    self.get_recibo()
                case 5:
                    self.change_pin()
                case 6:
                    print("FIN DEL PROGRAMA, GRACIAS POR UTILIZAR NUESTROS SERVICIOS")
                    exit()
                case _:
                    print("OPCION INCORRECTA INTENTA NUEVAMENTE")
        
           
cuenta = Cuenta("Juan Carlos", 0, "Cuenta de Ahorro")
cuenta.validar_cuenta()