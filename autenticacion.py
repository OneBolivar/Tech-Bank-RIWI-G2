from menu import menu

def autenticacion(saldo):
     for i in range(3):
        pin = input("Ingrese el pin ")
        if pin== "1234":
            print("¡Contraseña correcta! Acceso concedido.")
            intentos= int(input("cuantas operaciones quieres realizar?"))
            
            for i in range (intentos):
                  menu(saldo)
                  continuacion = int(input("Quieres continuar con las operaciones, 1 si o 2 no"))
                  if (continuacion==2):
                       break
                               
        elif pin != ("1234"):
            print("Contraseña incorrecta. Inténtalo de nuevo.")
     else:
            print("Has agotado tus intentos. Acceso denegado. ")
     
    