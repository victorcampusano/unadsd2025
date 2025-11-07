""" 
Clasificación de números
 Pide al usuario tres números y determina si son todos positivos, todos negativos, mixtos o si hay ceros.
"""




def suma(numero1, numero2):
    return numero1 + numero2 


def clasificacion_numeros(numeros):
    for n in numeros:
        if n >0:
            print(f"el valor de {n} es positivo")
        elif n<0:
            print(f"el valor de {n} es negativo")
        else:
            print(f"el valor de {n} es cero")
        
