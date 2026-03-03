def menu(saldo):
    Ejecucion = int(input("Elija una opcion: 1. Consultar saldo|| 2. Retirar dinero || 3. Depositar dinero: "))
    if Ejecucion == 1:
        return f"Su saldo actual es de: {saldo}"
    elif Ejecucion == 2:
        print("bloque 2")             
    elif Ejecucion == 3: 
        print("bloque 3")
    else:
         print("Opcion invalida")
         