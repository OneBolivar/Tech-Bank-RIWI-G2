# VALIDACION NUMERO NEGATIVO

# Se crea funcion para retiro 
def validacion_retiro(monto):
    while True:
        if monto < 0:
            print("Monto negativo")
            monto = int(input("Por favor ingrese el monto correctamente: "))
        else:
            print("ingreso correctamente el monto a retirar:", monto)
            break


    
