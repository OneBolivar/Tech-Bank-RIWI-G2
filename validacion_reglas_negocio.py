# Creando validacion de reglas de negocio
# REGLA: El monto ingresado no debe ser mayor al saldo 
def validacion_limite_retiro (monto, saldo):
    while True:
        if monto > saldo:
            print("Monto excede el saldo en cuenta")
