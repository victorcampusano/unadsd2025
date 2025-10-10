import math

n = int(input("Digite un numero para determinar si es primo o no: "))

rn = int(math.sqrt(n))


for x in range(3,rn + 1,2):
    
    if n % x == 0:
        print(n,"No Es primo")     
    else:
        print(n,"Es primo")


