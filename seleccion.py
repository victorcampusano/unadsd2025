"""
Cálculo de impuestos
 Pide al usuario su salario mensual y aplica los siguientes impuestos:
Menos de 10,000: 0%
Entre 10,000 y 30,000: 10% del excedente de 10,000
Más de 30,000: 20% (excedente de 10,000 + 20% del excedente de 30,000)

"""

salario = float(input("Digita tu salario mensual"))
descuento = 0
excedente_10mil = (30000 - 10000) * 0.1

if salario <= 10000:
    print("No tienes impuesto para pagar")
elif salario <= 30000:
    descuento = (salario - 10000) * 0.10
    print(f"Tu salario es {salario} y tu descuento es {descuento}")
else:
    descuento = (salario - 30000) * .20 + excedente_10mil
    print(f"Tu salario es {salario} y tu descuento es {descuento}")

print("\n\nGracias por utilizar nuestros servicios")


