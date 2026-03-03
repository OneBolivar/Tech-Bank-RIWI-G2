limiteDiario=500
retiro_diario=0

def control_de_retiro (monto):
    retiro_diario+=monto
    if (retiro_diario==500 or monto>500):
          print("Ya se ha excedido el límite de retiro permitido.")
    else:
         retiro_diario+=monto
         