def crear_pelicula(nombre: str, genero: str, duracion: int, anio: int, 
                  clasificacion: str, hora: int, dia: str) -> dict:
    """Crea un diccionario que representa una nueva película con toda su información 
       inicializada.
    Parámetros:
        nombre (str): Nombre de la pelicula agendada.
        genero (str): Generos de la pelicula separados por comas.
        duracion (int): Duracion en minutos de la pelicula
        anio (int): Anio de estreno de la pelicula
        clasificacion (str): Clasificacion de restriccion por edad
        hora (int): Hora a la cual se planea ver la pelicula, esta debe estar entre 
                    0 y 2359
        dia (str): Dia de la semana en el cual se planea ver la pelicula.
    Retorna:
        dict: Diccionario con los datos de la pelicula
    """    
    #TODO: completar y remplazar la siguiente línea por el resultado correcto 
     Pelicula={'nombre':nombre, 'genero':genero, 'duracion':duracion, 'anio':anio, 'clasificacion':clasificacion, 'hora':hora, 'dia':dia}

    return Pelicula
#Pelicula1 = mod.crear_pelicula("Volver al Futuro", "Infantil,Ciencia Ficcion", 116, 1985,'Todos', 1500, "Sabado")
Crear_Pelicula('Volver al Futuro','Infantil/'  'Ciencia Ficcion', 116,1985, 'Todos', 1500, 'Sabado')


def encontrar_pelicula(nombre_pelicula: str, p1: dict, p2: dict, p3: dict, p4: dict,  p5: dict) -> dict:
    """Encuentra en cual de los 5 diccionarios que se pasan por parametro esta la 
       pelicula cuyo nombre es dado por parametro.
       Si no se encuentra la pelicula se debe retornar None.
    Parametros:
        nombre_pelicula (str): El nombre de la pelicula que se desea encontrar.
        p1 (dict): Diccionario que contiene la informacion de la pelicula 1.
        p2 (dict): Diccionario que contiene la informacion de la pelicula 2.
        p3 (dict): Diccionario que contiene la informacion de la pelicula 3.
        p4 (dict): Diccionario que contiene la informacion de la pelicula 4.
        p5 (dict): Diccionario que contiene la informacion de la pelicula 5.
    Retorna:
        dict: Diccionario de la pelicula cuyo nombre fue dado por parametro. 
None si no se encuentra una pelicula con ese nombre.
    """
    #TODO: completar y remplazar la siguiente línea por el resultado correcto 
    lista_peliculas=[p1['Volver al Futuro'],p2['Jumanji'],p3['El Conjuro'], p4['Trampa en alta mar'], p5['Hombres de Negro']]
    for i in lista_peliculas:
      if i==nombre_pelicula:
        return i
    return d['nombre_pelicula']

    return None

def encontrar_pelicula_mas_larga(p1: dict, p2: dict, p3: dict, p4: dict, p5: dict) -> dict:
    """Encuentra la pelicula de mayor duracion entre las peliculas recibidas por
       parametro.
    Parametros:
        p1 (dict): Diccionario que contiene la informacion de la pelicula 1.
        p2 (dict): Diccionario que contiene la informacion de la pelicula 2.
        p3 (dict): Diccionario que contiene la informacion de la pelicula 3.
        p4 (dict): Diccionario que contiene la informacion de la pelicula 4.
        p5 (dict): Diccionario que contiene la informacion de la pelicula 5.
    Retorna:
        dict: El diccionario de la pelicula de mayor duracion
    """
    #TODO: completar y remplazar la siguiente línea por el resultado correcto 
    l=[p1['duracion'], p2['duracion'], p3['duracion'], p4['duracion'], p5['duracion']]
    peliculas=[p1,p2,p3,p4,p5]
    for pelicula in peliculas:
      if pelicula['duracion']==max(l):
        return pelicula
    print(encontrar_pelicula_mas_larga(p1, p2, p3, p4, p5))

def duracion_promedio_peliculas(p1: dict, p2: dict, p3: dict, p4: dict, p5: dict) -> str:
    """Calcula la duracion promedio de las peliculas que entran por parametro. 
       Esto es, la duración total de todas las peliculas dividida sobre el numero de peliculas. 
       Retorna la duracion promedio en una cadena de formato 'HH:MM' ignorando los posibles decimales.
    Parametros:
        p1 (dict): Diccionario que contiene la informacion de la pelicula 1.
        p2 (dict): Diccionario que contiene la informacion de la pelicula 2.
        p3 (dict): Diccionario que contiene la informacion de la pelicula 3.
        p4 (dict): Diccionario que contiene la informacion de la pelicula 4.
        p5 (dict): Diccionario que contiene la informacion de la pelicula 5.
    Retorna:
        str: la duracion promedio de las peliculas en formato 'HH:MM'
    """
    #TODO: completar y remplazar la siguiente línea por el resultado correcto 
    l=[p1['duracion'], p2['duracion'], p3['duracion'], p4['duracion'], p5['duracion']]
    prom=(sum(l)/len(l))
    horas=int(prom//60)
    minutos=int(prom%60)
    return f'{horas}:{minutos}'
print(duracion_promedio_peliculas(p1,p2,p3,p4,p5))

def encontrar_estrenos(p1: dict, p2: dict, p3: dict, p4: dict, p5: dict, anio: int) -> str:
    """Busca entre las peliculas cuales tienen como anio de estreno una fecha estrictamente
       posterior a la recibida por parametro.
    Parametros:
        p1 (dict): Diccionario que contiene la informacion de la pelicula 1.
        p2 (dict): Diccionario que contiene la informacion de la pelicula 2.
        p3 (dict): Diccionario que contiene la informacion de la pelicula 3.
        p4 (dict): Diccionario que contiene la informacion de la pelicula 4.
        p5 (dict): Diccionario que contiene la informacion de la pelicula 5.
        anio (int): Anio limite para considerar la pelicula como estreno.
    Retorna:
        str: Una cadena con el nombre de la pelicula estrenada posteriormente a la fecha recibida. 
        Si hay mas de una pelicula, entonces se retornan los nombres de todas las peliculas 
        encontradas separadas por comas. Si ninguna pelicula coincide, retorna "Ninguna".
    #TODO: completar y remplazar la siguiente línea por el resultado correcto 
      l=[p1['anio'], p2['anio'], p3['anio'], p4['anio'], p5['anio']]
    peliculas=[p1,p2,p3,p4,p5]
    nombres = [] # Initialize nombres list
    for pelicula in peliculas:
        if pelicula['anio']>=2024:
            nombres.append(pelicula['nombre']) # Indent this line to be within the if block
    return ', '.join(nombres) if nombres else 'Ninguna' # Indent this line to be outside the for loop
print(encontrar_estrenos(p1,p2,p3,p4,p5, 2024)) # Added the year 2024 as an argument

def cuantas_peliculas_18_mas(p1: dict, p2: dict, p3: dict, p4: dict, p5: dict) -> int:
    """Indica cuantas peliculas de clasificación '18+' hay entre los diccionarios recibidos.
    Parametros:
        p1 (dict): Diccionario que contiene la informacion de la pelicula 1.
        p2 (dict): Diccionario que contiene la informacion de la pelicula 2.
        p3 (dict): Diccionario que contiene la informacion de la pelicula 3.
        p4 (dict): Diccionario que contiene la informacion de la pelicula 4.
        p5 (dict): Diccionario que contiene la informacion de la pelicula 5.
    Retorna:
        int: Numero de peliculas con clasificacion '18+'
    """
    #TODO: completar y remplazar la siguiente línea por el resultado correcto 
   l=[p1['clasificacion'], p2['clasificacion'], p3['clasificacion'], p4['clasificacion'], p5['clasificacion']]
    contador=0
    for clasificacion in l:
      if clasificacion=='+18':
       cont=+1
       return contador
print(cuantas_peliculas_18_mas(p1,p2,p3,p4,p5))

def reagendar_pelicula(peli:dict, nueva_hora: int, nuevo_dia: str, 
                       control_horario: bool, p1: dict, p2: dict, p3: dict, p4: dict, p5: dict)->bool: 
    """Verifica si es posible reagendar la pelicula que entra por parametro. Para esto verifica
       si la nueva hora y el nuevo dia no entran en conflicto con ninguna otra pelicula, 
       y en caso de que el usuario haya pedido control horario verifica que se cumplan 
       las restricciones correspondientes.
    Parametros:
        peli (dict): Pelicula a reagendar
        nueva_hora (int): Nueva hora a la cual se quiere ver la pelicula
        nuevo_dia (str): Nuevo dia en el cual se quiere ver la pelicula
        control_horario (bool): Representa si el usuario quiere o no controlar
                                el horario de las peliculas.
        p1 (dict): Diccionario que contiene la informacion de la pelicula 1.
        p2 (dict): Diccionario que contiene la informacion de la pelicula 2.
        p3 (dict): Diccionario que contiene la informacion de la pelicula 3.
        p4 (dict): Diccionario que contiene la informacion de la pelicula 4.
        p5 (dict): Diccionario que contiene la informacion de la pelicula 5.
    Retorna:
        bool: True en caso de que se haya podido reagendar la pelicula, False de lo contrario.
    """
    #TODO: completar y remplazar la siguiente línea por el resultado correcto 
    peliculas=[p1,p2,p3,p4,p5]
    nombres=[]
    horas=[]
    dias=[]
    for pelicula in peliculas:
      nombres.append(pelicula['nombre'])
      horas.append(pelicula['hora'])
      dias.append(pelicula['dia'])
    if control_horario==True:
      if (nueva_hora in horas) and (nuevo_dia in dias):
        return False
    else:
      return False
print(reagendar_pelicula(p1, 2100, 'Viernes', True, p1, p2, p3, p4, p5))
def decidir_invitar(peli: dict, edad_invitado: int, autorizacion_padres: bool)->bool:
    """Verifica si es posible invitar a la persona cuya edad entra por parametro a ver la 
       pelicula que entra igualmente por parametro. 
       Para esto verifica el cumplimiento de las restricciones correspondientes.
    Parametros:
        peli (dict): Pelicula que se desea ver con el invitado
        edad_invitado (int): Edad del invitado con quien se desea ver la pelicula
        autorizacion_padres (bool): Indica si el invitado cuenta con la autorizacion de sus padres 
        para ver la pelicula
    Retorna:
        bool: True en caso de que se pueda invitar a la persona, False de lo contrario.
    """
    #TODO: completar y remplazar la siguiente línea por el resultado correcto 
     clasificacion = peli['clasificacion'] # Assign the value of peli['clasificacion'] to the variable clasificacion
    # Convert clasificacion to integer based on its value
    if clasificacion == 'Todos':
        clasificacion_int = 0
    elif clasificacion == '7+':
        clasificacion_int = 7
    elif clasificacion == '12+':
        clasificacion_int = 12
    elif clasificacion == '17+':
        clasificacion_int = 17
    else:
        clasificacion_int = 18 # Default to 18 if not recognized

    if (edad_invitado>=clasificacion_int) and (autorizacion_padres==True): # Use clasificacion_int for comparison
      return True
    else:
      return False
print(decidir_invitar(p3,20,True))
