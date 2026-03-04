from historial import historial_operaciones

def retirar_dinero(valor, cuenta):
    cuenta['Saldo']-= valor
    print(f"Has retirado {valor}. Tu nuevo saldo es {cuenta['Saldo']}.")
    historial_operaciones("Retirar", valor, cuenta['Saldo'])
