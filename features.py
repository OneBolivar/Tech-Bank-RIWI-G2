
def autenticacion():
     for i in range(3):
        pin = input("Ingrese el pin ")
        if pin== "1234":
            print("¡Contraseña correcta! Acceso concedido.")
        elif pin != ("1234"):
            print("Contraseña incorrecta. Inténtalo de nuevo.")
     else:
            print("Has agotado tus intentos. Acceso denegado. ")
     
    

def retiro(saldo):
        Validador = True
        Retiro = float(input("Ingrese monto a retirar: "))
        while Validador:
            if Retiro < 0:
                print("Ingrese una cantidad valida")
                Retiro = float(input("Ingrese monto a retirar: "))
            if Retiro > 0:
                    if Retiro > saldo:
                        return f"Fondos insuficientes"
                    elif Retiro <= saldo:
                        return f"Retiro efectuado, su nuevo saldo es de: {(saldo - Retiro)}"
                    Validador = False
                        

def deposito(saldo):
    Validador = True
    while Validador:
        Deposito = float(input("Ingrese monto a depositar: "))
        if Deposito < 0:
            print("Ingrese una cantidad valida")
            Deposito = float(input("Ingrese monto a depositar: "))
        if Deposito >= 0:
            Validador = False
            return f"Su saldo total es de: {(Deposito + saldo)}"

