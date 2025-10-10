#codigo para crear una calculadora simple con python
""" 
Crear un algoritmo que permita seleccionar el tipo de operación (suma, resta, multiplicación, división, raid cuadrada y residuo o resto), solicitar 2 números y de acuerdo a la operación seleccionada mostrar el resultado
"""

operacion = input("Indique el tipo de operacion a realizar: \n 1. Sumar \n2. Resta \n3.Multiplicacion \n4.Division \n5. Raiz  Cuadrada \n6.Residuo \n0.Salir")

print("El valor seleccionado es?: ",operacion)

op = int(operacion)

valor1 = int(input("Digite el valor 1:\n"))
valor2 = int(input("Digite el valor 2:\n"))

if op == 1:
    print("La suma de los valores es: ",valor1 + valor2)
elif op ==2:
    print("La res de los valores es: ",valor1 - valor2)
elif op==0:
    exit()




