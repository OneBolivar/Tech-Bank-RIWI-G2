
historial=[]

def autenticacion(saldo):
     for i in range(3):
        pin = input("Ingrese el pin ")
        if pin== "1234":
            print("¡Contraseña correcta! Acceso concedido.")
            intentos= int(input("cuantas operaciones quieres realizar?"))
            
            for i in range (intentos):
                  menu(saldo)
                  continuacion = int(input("Quieres continuar con las operaciones, 1 si o 2 no"))
                  if (continuacion==2):
                       break
               

                
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
        


def historial_operaciones (tipo, monto, saldo):
    historial.append({
        'Tipo':tipo,
        'Monto':monto,
        'Saldo':saldo
    })

def mostrar_historial ():
    print("HISTORIAL DE OPERACIONES")
    for i , operacion in enumerate(historial,1):
        print(f" Operacion {i}---- {operacion['Tipo']}")
        print(f"  Monto:     ${operacion['Monto']:>10,.2f}")
        print(f"  Saldo:     ${operacion['Saldo']:>10,.2f}")





