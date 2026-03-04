from validacion_entrada import validar_monto

def menu(cuenta):
    print("=" * 40)
    print("                 Menu")
    print("=" * 40)
    Ejecucion = int(input("Elija una opcion: 1. Consultar saldo|| 2. Retirar dinero || 3. Depositar dinero: "))
    if Ejecucion == 1:
        print("Tu saldo es de: ", cuenta['Saldo'])
    elif Ejecucion == 2:
        validar_monto("Retirar",cuenta)
    elif Ejecucion == 3: 
        validar_monto("Depositar",cuenta)
    else:
         print("Opcion invalida")

         