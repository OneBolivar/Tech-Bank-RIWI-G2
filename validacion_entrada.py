from validacion_reglas_negocio import validacion_limite_retiro
from deposito import despositar
from retiro_diario import control_de_retiro
# VALIDACION NUMERO NEGATIVO

def validar_monto(tipo_operacion, cuenta):
    while True:
        monto = float(input(f"Ingrese el monto a {tipo_operacion}: "))
        if monto <= 0:
            print("El monto debe ser mayor que cero.")
        else:
            if(tipo_operacion=="Retirar"):
                if(validacion_limite_retiro(monto, cuenta)): control_de_retiro(monto, cuenta)
            else:
                despositar(monto, cuenta)
                break