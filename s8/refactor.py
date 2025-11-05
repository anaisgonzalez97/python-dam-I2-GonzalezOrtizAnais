"""Analiza qué errores contiene el código, refactoriza con
funciones y controla errores de entrada y división por cero (o cualquier
otro que creas que puedes encontrar). Apóyate en la IA pero documenta y
explica las decisiones que tú has tomado."""


def programa():
    alumnos = []
    
    # Controlar número de alumnos
    while True:
        n = input("¿Cuántos alumnos? ")
        if n.isdigit() and int(n) > 0:
            n = int(n)
            break
        else:
            print("Error: Debe ser un número positivo")
    
    # Ingresar notas
    for i in range(n):
        while True:
            nota = input(f"Nota alumno {i+1}: ")
            if nota.isdigit() and 0 <= int(nota) <= 10:
                alumnos.append(int(nota))
                break
            else:
                print("Error: La nota debe ser 0-10")
    
    # Calcular y mostrar resultados
    if alumnos:  # Evitar división por cero
        media = sum(alumnos) / len(alumnos)
        print(f"\nMedia: {media:.1f}")
        
        print("Aprobados:")
        for nota in alumnos:
            if nota >= 5:
                print(f"- {nota}")

# Ejecutar
programa()