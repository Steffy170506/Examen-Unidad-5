def main():
    
    try:
        num_estudiantes = int(input("¿Cuántos estudiantes tiene el grupo? "))
        num_materias = int(input("¿Cuántas materias tiene el grupo? "))
        
        if num_estudiantes <= 0 or num_materias <= 0:
            print("Error: Los números deben ser mayores que cero.")
            return
    except ValueError:
        print("Error: Debe ingresar números enteros válidos.")
        return

    calificaciones = []
    
    print("\n--- Captura de calificaciones (0-100) ---")
    for i in range(num_estudiantes):
        print(f"\nEstudiante {i + 1}:")
        estudiante = []
        for j in range(num_materias):
            while True:
                try:
                    calif = int(input(f"  Calificación materia {j + 1}: "))
                    if 0 <= calif <= 100:
                        estudiante.append(calif)
                        break
                    else:
                        print("    Error: La calificación debe estar entre 0 y 100.")
                except ValueError:
                    print("    Error: Ingrese un número válido.")
        calificaciones.append(estudiante)

    print("\n" + "="*50)
    print("RESULTADOS")
    print("="*50)
    
    print("\n--- Promedio de cada estudiante ---")
    promedios_estudiantes = []
    for i, estudiante in enumerate(calificaciones):
        promedio = sum(estudiante) / len(estudiante)
        promedios_estudiantes.append(promedio)
        print(f"Estudiante {i + 1}: {promedio:.2f}")

    print("\n--- Promedio de cada materia ---")
    promedios_materias = []
    for j in range(num_materias):
        suma_materia = 0
        for i in range(num_estudiantes):
            suma_materia += calificaciones[i][j]
        promedio_materia = suma_materia / num_estudiantes
        promedios_materias.append(promedio_materia)
        print(f"Materia {j + 1}: {promedio_materia:.2f}")

    calificacion_maxima = calificaciones[0][0]
    calificacion_minima = calificaciones[0][0]
    
    for estudiante in calificaciones:
        for calif in estudiante:
            if calif > calificacion_maxima:
                calificacion_maxima = calif
            if calif < calificacion_minima:
                calificacion_minima = calif

    print("\n--- Resumen general ---")
    print(f"Calificación más alta del grupo: {calificacion_maxima}")
    print(f"Calificación más baja del grupo: {calificacion_minima}")
    
    todas_calificaciones = [calif for estudiante in calificaciones for calif in estudiante]
    promedio_general = sum(todas_calificaciones) / len(todas_calificaciones)
    print(f"Promedio general del grupo: {promedio_general:.2f}")

if __name__ == "__main__":
    main()