
canasta = []

cantidad = int(input("Digite la cantidad de frutas que quiere llevar en su canasta: "))

cont = 1

while cont <= cantidad:
    fruta = input(f"Digite la fruta #{cont}: ")
    canasta.append(fruta) #agrego la fruta a la lista de frutas
    cont += 1

#recorrer la canasta e imprimir los valores de la misma
for f in canasta: 
    print(f)
