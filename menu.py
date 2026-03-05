from validacion_entrada import validar_monto
from historial import historial_operaciones


def menu(cuenta):
    print("=" * 40)
    print("                 Menu")
    print("=" * 40)
    Ejecucion = int(input("Elija una opcion"))
    print("1- Consultar Saldo")
    print("2- Retiro de saldo")
    print("3- Depositar Dinero")
    if Ejecucion == 1:
        print("Tu saldo es de: ", cuenta['Saldo'])
        historial_operaciones("consultar", 0, cuenta['Saldo'])
    elif Ejecucion == 2:
        validar_monto("Retirar", cuenta)
    elif Ejecucion == 3:
        validar_monto("Depositar", cuenta)
    else:
        print("Opcion invalida")
