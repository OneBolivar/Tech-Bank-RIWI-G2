Ejecucion = int(input("Elija una opcion: 1. Consultar saldo|| 2. Retirar dinero || 3. Depositar dinero: "))
if Ejecucion == 1:
    print("Su saldo actual es de: ", SaldoInicial) 
elif Ejecucion == 2:
        Retiro = float(input("Ingrese monto a retirar: "))
        while Validador:
            if Retiro < 0:
                print("Ingrese una cantidad valida")
                Retiro = float(input("Ingrese monto a retirar: "))
                if Retiro > 0:
                    Validador = False
                if Retiro > SaldoInicial:
                        print("Fondos insuficientes")
                elif Retiro <= SaldoInicial:
                        print("Retiro efectuado, su nuevo saldo es de: ", (SaldoInicial - Retiro))                   
elif Ejecucion == 3: 
                    while Validador:
                        Deposito = float(input("Ingrese monto a depositar: "))
                    if Deposito < 0:
                             print("Ingrese una cantidad valida")
                             Deposito = float(input("Ingrese monto a depositar: "))  
                    if Deposito >= 0:
                                print("Su saldo total es de: ", (Deposito + SaldoInicial))
                                Validador = False
else: