

def retiro(saldo):
        Validador = True
        Retiro = float(input("Ingrese monto a retirar: "))
        while Validador:
            if Retiro < 0:
                return f"Ingrese una cantidad valida"
                Retiro = float(input("Ingrese monto a retirar: "))
            if Retiro > 0:
                    Validador = False
                    if Retiro > saldo:
                        return f"Fondos insuficientes"
                    elif Retiro <= saldo:
                        return f"Retiro efectuado, su nuevo saldo es de: {(saldo - Retiro)}"
                        


