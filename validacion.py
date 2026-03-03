# VALIDACION NUMERO NEGATIVO
from retiro import retiro
from deposito import deposito

# Se crea funcion para retiro 
def validacion_retiro(monto):
    while True:
        if monto < 0:
            print("Monto negativo")
            monto = int(input("Por favor ingrese el monto correctamente: "))
        else:
            print("ingreso correctamente el monto a retirar:")
            retiro()
            break

# Se crea funcion para depositar
def validacion_deposito(monto):
    while True:
        if monto < 0:
            print("Monto negativo")
            monto = int(input("Por favor ingrese el monto correctamente: "))
        else:
            print("ingreso correctamente el monto a depositar:")
            deposito()
            break