from autenticacion import autenticacion 
from historial import mostrar_historial

cuenta={
     'Saldo':1000,
     'Limite_de_retiro':500,
     'Retiro_diario':0,
     'Pin':"1234"
}

print("...: Bievenidos al cajero automatico TechBank Riwi Digital:...")

autenticacion(cuenta)
mostrar_historial()
