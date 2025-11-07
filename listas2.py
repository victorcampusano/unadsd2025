msg = "Programa para calcular calificaciones por estudiante"
print("-" * 60)
print(msg)
#print("*" * 40)
print("-" * 60)



#funcion para capturar valores

def entradaDatos(txt,tipo):
    """
    Devuelve la @entrada en el formato escogido (S: string, B: booleano, E: entero)

    Parameters
    ----------
    entrada : string
        el texto a devolver
    tipo : string
        el tipo de dato que quieres devolver (S: string, B: booleano, E: entero)

    Returns
    -------
    indefinido
        Segun el tipo de dato retorna string, boolean o entero
    """

    if str.upper(tipo) == 'S':
        return txt 
    elif str.upper(tipo) == 'B':
        return bool(txt)
    elif str.upper(tipo) == 'E':
        if txt.isdigit():
            return int(txt)
        else:
            return "Error"

estudiantes = [ ]
cant = 0 
calificaciones = [[],[],[],[]]
maxCalificaciones = 4
#tupla1 = ()
#diccionario = { }

entrada = input("Digite la cantidad de estudiantes:\n")

cant = entradaDatos(entrada,'e')


for est in range(0,cant):
    estudiantes.append(est)
    for contador in range(0,maxCalificaciones):
        i = input(f"Digite la calificacion: {contador+1}")
        cal = entradaDatos(i,'e')
        calificaciones[est].append(cal)
        #calificaciones.append
    print(f"Estudiante : {est+1}",calificaciones[est])







