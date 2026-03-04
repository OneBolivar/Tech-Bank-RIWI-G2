from retiro import retirar_dinero

def control_de_retiro (monto, cuenta):

     if cuenta[ 'Retiro_diario'] + monto > cuenta['Limite_de_retiro']:
          print("Se ha superado el límite máximo de retiro permitido.")
     else:
         cuenta[ 'Retiro_diario'] += monto
         retirar_dinero(monto, cuenta)