print("GRUPO 2")

for i in range(3):
    pin = input("Ingrese el pin ")
    if pin== "1234":
        print("¡Contraseña correcta! Acceso concedido.")
    else:
        print("Contraseña incorrecta. Inténtalo de nuevo.")
else:
    print("Has agotado tus intentos. Acceso denegado. ")