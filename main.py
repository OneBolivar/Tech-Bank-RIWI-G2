from retiro_diario import control_de_retiro
saldo = float(1000)
print("...: Bievenidos al cajero automatico TechBank Riwi Digital:...")

codigo = input("Ingrese el pin: ")

if codigo == "1234":
    print("Autenticado")
else:
    print(("Error"))
print("GRUPO 2")

for i in range(3):
    pin = input("Ingrese el pin ")
    if pin== "1234":
        print("¡Contraseña correcta! Acceso concedido.")
    else:
        print("Contraseña incorrecta. Inténtalo de nuevo.")
else:
    print("Has agotado tus intentos. Acceso denegado. ")




