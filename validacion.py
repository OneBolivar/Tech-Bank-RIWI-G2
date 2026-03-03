# VALIDACION NUMERO NEGATIVO
from retiro import retiro
from deposito import deposito

# Se crea funcion para retiro 
def validacion_retiro(saldo):
    while True:
        monto = int(input("Por favor ingrese el monto correctamente: "))
        if monto < 0:
            print("Monto negativo, vuelve a intentarlo")
        elif monto > saldo:
            print("Fondos insuficientes, vuelve a intentarlo")
        else:
            print("ingreso correctamente el monto a retirar:")
            retiro(monto,saldo)
            break

# Se crea funcion para depositar
def validacion_deposito(saldo):
    monto = int(input("Por favor ingrese el monto correctamente: "))
    while True:
        if monto < 0:
            print("Monto negativo, vuelve a intentarlo")
        else:
            print("ingreso correctamente el monto a depositar:")
            deposito(monto, saldo)
            break