#Tabla de multiplicar hasta N: Pide un numero por teclado y luego pide el limite de la tabla. Crea la tabla de multiplicar desde 1 hasta N para el numero en cuestión.

print("*"*50)
print("Calculadora de un Numero por teclado hasta N")
print("-"*50)

num = int(input("Digite un numero\n"))
hasta = int(input("Digite el numero limite de la tabla\n"))

print(f"el numero a multiplicar es {num}")

inicial = 1
while(inicial <= hasta):
    if inicial * num > 100:
        break
    print(f"{num} x {inicial} = {num*inicial}")
    inicial = inicial + 1


