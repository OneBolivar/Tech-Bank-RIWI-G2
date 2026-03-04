from menu import menu

def autenticacion(cuenta):
     for i in range(3):
        pin = input("Ingrese el pin ")
        if pin==cuenta['Pin']:
            print("¡Contraseña correcta! Acceso concedido.")
            print("*" * 40,"\n")
            intentos= int(input("cuantas operaciones quieres realizar?: "))
            for i in range (intentos):
                  menu(cuenta)
                  continuacion = int(input("Quieres continuar con las operaciones, 1 si o 2 no: "))
                  if (continuacion==2): break
            break
        elif pin !=cuenta['Pin']:
            print("Contraseña incorrecta. Inténtalo de nuevo.")
     else:
            print("Has agotado tus intentos. Acceso denegado. ")