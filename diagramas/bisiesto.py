"""
x Pedir anio
x Leer anio
x Si Es un numero valido? entonces
x Si Es un numero entero positivo? entonces
x Si Es mayor a Cero entonces
x Si Es menor que 3000 entonces
x Si A/400 entonces imprimir Es bisiesto Sino
x Si A/100 entonces imprimir no es bisiesto sino 
x Si A/4 entonces es bisiesto Sino no es bisiesto

Fin 


"""



def esBisiesto(anio):
    A = 0
    ok = False

    if anio.isdigit():
        A = int(anio)

        if A > 0:
            if A <= 3000:
                if A % 400 == 0:                   
                    ok = True
                elif A % 100 == 0:                   
                    ok = False
                elif A % 4 == 0:                    
                    ok =  True
                else:                    
                    ok = False
            else:
                ok = False
        else:
            ok = False

    return ok



x = input("Ingrese el año: ")

if esBisiesto(x):
    print(f"El año {x} es bisiesto") 
else:
    print(f"El año {x} no es bisiesto")

