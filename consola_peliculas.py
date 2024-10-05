import modulo_peliculas as mod

def mostrar_informacion_pelicula(pelicula: dict) -> None:
    """Imprime los detalles de la película."""
    nombre = pelicula["nombre"]
    genero = pelicula["genero"]
    duracion = pelicula["duracion"]
    anio = pelicula["anio"]
    clasificacion = pelicula["clasificacion"]
    hora = pelicula["hora"]
    dia = pelicula["dia"]
    
    print(f"Nombre: {nombre} - Año: {anio} - Duración: {duracion} mins")
    print(f"Género: {genero} - Clasificación: {clasificacion}")
    
    # Formatea la hora y los minutos
    hora_formato = f"{hora // 100:02d}"
    min_formato = f"{hora % 100:02d}"
    
    print(f"Día: {dia} Hora: {hora_formato}:{min_formato}")

def ejecutar_encontrar_pelicula_mas_larga(p1: dict, p2: dict, p3: dict, p4: dict, p5: dict) -> None:
    """Ejecuta la opción de encontrar la película más larga."""
    peliculas = [p1, p2, p3, p4, p5]
    pelicula_mas_larga = max(peliculas, key=lambda p: p["duracion"])
    
    print("La película más larga es:")
    mostrar_informacion_pelicula(pelicula_mas_larga)

def ejecutar_consultar_duracion_promedio_peliculas(p1: dict, p2: dict, p3: dict, p4: dict, p5: dict) -> None:
    """Ejecuta la opción de consultar la duración promedio de las películas."""
    peliculas = [p1, p2, p3, p4, p5]
    total_duracion = sum(pelicula["duracion"] for pelicula in peliculas)
    duracion_promedio = total_duracion / len(peliculas)
    
    print(f"La duración promedio de las películas es: {duracion_promedio:.2f} minutos.")

def ejecutar_encontrar_estrenos(p1: dict, p2: dict, p3: dict, p4: dict, p5: dict) -> None:
    """Ejecuta la opción de buscar películas de estreno (más recientes que un año dado)."""
    anio_actual = 2024  # Suponiendo que estamos en 2024
    peliculas = [p1, p2, p3, p4, p5]
    estrenos = [pelicula for pelicula in peliculas if pelicula["anio"] >= anio_actual]
    
    if estrenos:
        print("Películas de estreno:")
        for pelicula in estrenos:
            mostrar_informacion_pelicula(pelicula)
    else:
        print("No hay películas de estreno.")

def ejecutar_cuantas_peliculas_18_mas(p1: dict, p2: dict, p3: dict, p4: dict, p5: dict) -> None:
    """Ejecuta la opción de consultar cuántas películas tienen clasificación 18+."""
    peliculas = [p1, p2, p3, p4, p5]
    peliculas_18 = [pelicula for pelicula in peliculas if pelicula["clasificacion"] == "18+"]
    
    print(f"Hay {len(peliculas_18)} películas con clasificación 18+.")

def ejecutar_reagendar_pelicula(p1: dict, p2: dict, p3: dict, p4: dict, p5: dict) -> None:
    """Ejecuta la opción de reagendar una película."""
    print("Reagendar una película de la agenda")

    nombre = input("Ingrese el nombre de la película que desea reagendar: ")
    pelicula = mod.encontrar_pelicula(nombre, p1, p2, p3, p4, p5)
    
    if pelicula is None:
        print("No hay ninguna película con este nombre")
        return

    nuevo_dia = input(f"Ingrese el nuevo día para la película '{nombre}': ")
    nuevo_hora = input("Ingrese la nueva hora para la película (en formato 24h, ej. 1530): ")

    pelicula["dia"] = nuevo_dia
    pelicula["hora"] = int(nuevo_hora)
    
    print(f"Película '{nombre}' re-agendada a {nuevo_dia} a las {nuevo_hora}.")

def ejecutar_decidir_invitar(p1: dict, p2: dict, p3: dict, p4: dict, p5: dict) -> None:
    """Ejecuta la opción de decidir si se puede invitar a alguien a ver una película."""
    print("Decidir si se puede invitar a alguien a ver una película")

    nom_peli = input("Ingrese el nombre de la película: ")
    pelicula = mod.encontrar_pelicula(nom_peli, p1, p2, p3, p4, p5)

    if pelicula is None:
        print("No hay ninguna película con este nombre.")
        return

    clasificacion = pelicula["clasificacion"]
    if clasificacion == "Todos" or clasificacion == "7+" or clasificacion == "12+":
        print(f"Puedes invitar a alguien a ver '{nom_peli}'.")
    else:
        print(f"No puedes invitar a alguien a ver '{nom_peli}' debido a la clasificación {clasificacion}.")

def iniciar_aplicacion():
    """Inicia la ejecución de la aplicación por consola."""
    # Creación de películas
    p1 = mod.crear_pelicula('Volver al Futuro', 'Infantil/Ciencia Ficcion', 116, 1985, 'Todos', 1500, 'Sábado')
    p2 = mod.crear_pelicula('Jumanji', 'Infantil/Aventura', 100, 1995, 'Todos', 1700, 'Domingo')
    p3 = mod.crear_pelicula('El Conjuro', 'Terror/Misterio', 112, 2013, '17+', 2100, 'Viernes')
    p4 = mod.crear_pelicula('Trampa en alta mar', 'Suspenso/Crimen', 88, 2024, '12+', 1930, 'Miércoles')
    p5 = mod.crear_pelicula('Hombres de Negro', 'Acción/Ciencia Ficcion Humorística', 98, 1997, '7+', 1340, 'Martes')

    ejecutando = True
    while ejecutando:
        # Mostrar las películas en la agenda
        print("\n\nMi agenda de películas para la semana de receso" + "\n" + ("-" * 50))
        mostrar_informacion_pelicula(p1)
        print("-" * 50)
        mostrar_informacion_pelicula(p2)
        print("-" * 50)
        mostrar_informacion_pelicula(p3)
        print("-" * 50)
        mostrar_informacion_pelicula(p4)
        print("-" * 50)
        mostrar_informacion_pelicula(p5)
        print("-" * 50)

        # Mostrar menú de opciones
        ejecutando = mostrar_menu_aplicacion(p1, p2, p3, p4, p5)

        if ejecutando:
            input("Presione cualquier tecla para continuar ... ")

def mostrar_menu_aplicacion(p1: dict, p2: dict, p3: dict, p4: dict, p5: dict) -> bool:
    """Muestra el menú de opciones al usuario."""
    print("Menu de opciones")
    print(" 1 - Consultar película más larga")
    print(" 2 - Consultar duración promedio de las películas")
    print(" 3 - Consultar películas de estreno")
    print(" 4 - Consultar cuántas películas tienen clasificación 18+")
    print(" 5 - Reagendar película")
    print(" 6 - Verificar si se puede invitar a alguien")    
    print(" 7 - Salir de la aplicación")

    opcion_elegida = input("Ingrese la opción que desea ejecutar: ").strip()
    
    continuar_ejecutando = True

    if opcion_elegida == "1":
        ejecutar_encontrar_pelicula_mas_larga(p1, p2, p3, p4, p5)
    elif opcion_elegida == "2":
        ejecutar_consultar_duracion_promedio_peliculas(p1, p2, p3, p4, p5)
    elif opcion_elegida == "3":
        ejecutar_encontrar_estrenos(p1, p2, p3, p4, p5)
    elif opcion_elegida == "4":
        ejecutar_cuantas_peliculas_18_mas(p1, p2, p3, p4, p5)
    elif opcion_elegida == "5":
        ejecutar_reagendar_pelicula(p1, p2, p3, p4, p5)
    elif opcion_elegida == "6":
        ejecutar_decidir_invitar(p1, p2, p3, p4, p5)
    elif opcion_elegida == "7":
        print("Saliendo de la aplicación...")
        continuar_ejecutando = False
    else:
        print("Opción no válida. Intente de nuevo.")

    return continuar_ejecutando

# Iniciar la aplicación
iniciar_aplicacion()
