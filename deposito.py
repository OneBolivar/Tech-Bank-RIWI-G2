from historial import historial_operaciones

def despositar( valor, cuenta ):
        cuenta['Saldo']+= valor
        print (" Su Deposito fue exitoso, su nuevo saldo es:", cuenta['Saldo']) 
        historial_operaciones("Depositar", valor, cuenta['Saldo'])
