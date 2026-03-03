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
        