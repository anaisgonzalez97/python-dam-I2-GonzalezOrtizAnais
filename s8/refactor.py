


def programa():
    alumnos = []
    
    # Controlar número de alumnos
    while True:
        n = input("¿Cuántos alumnos hay? ")
        if n.isdigit() and int(n) > 0:
            n = int(n)
            break
        else:
            print("Error: Debe ser un número positivo")
    
    # Ingresar notas
    for i in range(n):
        while True:
            nota = input(f"Nota alumno {i+1}: ") #para que no empiece en 0
            if nota.isdigit() and 0 <= int(nota) <= 10: #nota entre 0 y 10, incluye ambos numeros
                alumnos.append(int(nota))
                break
            else:
                print("Error: La nota debe ser 0-10")
    
    # Calcular y mostrar resultados
    if alumnos:  # Evitar división por cero
        media = sum(alumnos) / len(alumnos)
        print(f"\nMedia: {media:.1f}") #redondea a un decimal
        
        print("Aprobados:")
        for nota in alumnos:
            if nota >= 5:
                print(f"- {nota}")

# Ejecutar
programa()