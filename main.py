from retiro_diario import control_de_retiro
saldo = float(1000)
print("...: Bievenidos al cajero automatico TechBank Riwi Digital:...")

"""codigo = input("Ingrese el pin: ")

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

    """
cuenta={
     'Saldo':1000,
     'Limite_de_retiro':500,
     'retiro_diario':0
}
control_de_retiro(550,cuenta)
print(cuenta)
print("=====================")
control_de_retiro(200,cuenta)
print(cuenta)
print("=====================")
control_de_retiro(10,cuenta)
print(cuenta)
print("=====================")
control_de_retiro(600,cuenta)
print(cuenta)
print("=====================")
control_de_retiro(80,cuenta)
print(cuenta)
print("=====================")
