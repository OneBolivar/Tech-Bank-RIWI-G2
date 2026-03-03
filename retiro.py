def retiro(Retiro,saldo):
       
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