from menu import menu_de_opciones
saldo = float(1000)
print("...: Bievenidos al cajero automatico TechBank Riwi Digital:...")

for i in range(3):
    pin = input("Ingrese el pin ")
    if pin== "1234":
        print("¡Contraseña correcta! Acceso concedido.")
        menu_de_opciones()
    else:
        print("Contraseña incorrecta. Inténtalo de nuevo.")
else:
    print("Has agotado tus intentos. Acceso denegado. ")


