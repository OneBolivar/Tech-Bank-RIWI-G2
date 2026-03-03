from features import retiro, deposito
def menu(saldo):
    Ejecucion = int(input("Elija una opcion: 1. Consultar saldo|| 2. Retirar dinero || 3. Depositar dinero: "))
    if Ejecucion == 1:
        return f"Su saldo actual es de: {saldo}"
    elif Ejecucion == 2:
        return retiro(saldo)           
    elif Ejecucion == 3: 
        return deposito(saldo)
    else:
         print("Opcion invalida")
prueba = menu(1000)
print(prueba)
         