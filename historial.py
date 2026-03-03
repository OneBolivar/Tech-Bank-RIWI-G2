historial=[]

def historial_operaciones (tipo, monto, saldo):
    historial.append({
        'Tipo':tipo,
        'Monto':monto,
        'Saldo':saldo
    })

def mostrar_historial ():
    print("HISTORIAL DE OPERACIONES")
    for i , operacion in enumerate(historial,1):
        print(f" Operacion {i}---- {operacion['Tipo']}")
        print(f"  Monto:     ${operacion['Monto']:>10,.2f}")
        print(f"  Saldo:     ${operacion['Saldo']:>10,.2f}")
