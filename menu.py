from validacion import validacion_deposito, validacion_retiro

def menu(saldo):
    Ejecucion = int(input("Elija una opcion: 1. Consultar saldo|| 2. Retirar dinero || 3. Depositar dinero: || 4. salir"))
    if Ejecucion == 1:
        return f"Su saldo actual es de: {saldo}"
    elif Ejecucion == 2:
        validacion_retiro(saldo)                
    elif Ejecucion == 3: 
         validacion_deposito(saldo)
    elif Ejecucion == 4:
        return False
    else:
         print("Opcion invalida")
         