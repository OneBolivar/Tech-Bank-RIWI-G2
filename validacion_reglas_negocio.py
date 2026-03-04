# Creando validacion de reglas de negocio
# REGLA: El monto ingresado no debe ser mayor al saldo 
def validacion_limite_retiro (monto, cuenta):
    while True:
        if monto > cuenta['Saldo']:
            print("Monto excede el saldo en cuenta")
            return False
        else: 
            return True
            


