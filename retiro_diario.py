from retiro import retirar_dinero

cuenta={
     'Saldo':1000,
     'Limite_de_retiro':500,
     'retiro_diario':0
}

def control_de_retiro (monto, cuenta):

     if cuenta[ 'retiro_diario'] + monto > cuenta['Limite_de_retiro']:
          print("Se ha superado el límite máximo de retiro permitido.")
     else:
         cuenta[ 'retiro_diario'] += monto
         retirar_dinero(monto, cuenta['Saldo'])