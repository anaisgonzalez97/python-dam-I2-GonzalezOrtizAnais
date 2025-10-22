#crea un pequeño sistema usando diccionarios:
#1. Tienda → productos y precios
#2. Biblioteca → libros y disponibilidad
#3. Gimnasio → socios y cuotas
#Cada alumno debe:
#• Insertar, modificar y eliminar registros.
#• Calcular al menos una métrica (media, suma, máximos...).
#• Usar un bucle for para recorrer las claves y valores.
#• Realizar una adaptación personalizada

# Diccionario con libros, cada libro tiene título como clave y un diccionario con autor y cantidad
biblioteca = {
    "El Quijote": {"autor": "Miguel de Cervantes", "cantidad": 3},
    "El brillo de las luciérnagas": {"autor": "Paul Pen", "cantidad": 5},
    "Novia": {"autor": "Ali Hazelwood", "cantidad": 2},
    "It": {"autor": "Stephen King", "cantidad": 5}
}

# Función para añadir un libro nuevo
def añadir_libro():
    titulo = input("Introduce el título del libro: ")
    autor = input("Introduce el autor del libro: ")
    cantidad = int(input("Introduce la cantidad disponible: "))
    biblioteca[titulo] = {"autor": autor, "cantidad": cantidad}
    print(f"Libro '{titulo}' añadido.")

# Función para modificar la cantidad de un libro
def modificar_cantidad():
    titulo = input("Introduce el título del libro que quieres modificar: ")
    if titulo in biblioteca:
        cantidad = int(input("Introduce la nueva cantidad disponible: "))
        biblioteca[titulo]["cantidad"] = cantidad #accede a "cantidad" y se actualiza el valor
        print(f"Cantidad de '{titulo}' actualizada.")
    else:
        print("Ese libro no está en la biblioteca.")

# Función para eliminar un libro
def eliminar_libro():
    titulo = input("Introduce el título del libro que quieres eliminar: ")
    if titulo in biblioteca:
        del biblioteca[titulo] #eliminar el titulo especificado
        print(f"Libro '{titulo}' eliminado.")
    else:
        print("Ese libro no está en la biblioteca.")

# Función para mostrar todos los libros con autor y cantidad
def mostrar_libros():
    print("Libros en la biblioteca:")
    for titulo, info in biblioteca.items(): #por cada iteración, devuelve los items del diccionario
        print(f"Título: {titulo}, Autor: {info['autor']}, Cantidad disponible: {info['cantidad']}")

# Función para calcular la cantidad total de libros disponibles
def total_libros():
    total = 0
    for info in biblioteca.values():
        total += info["cantidad"]
    print(f"Total de libros disponibles en la biblioteca: {total}")

# Programa principal: MENÚ
while True:
    print("\n¿Qué quieres hacer?")
    print("1 - Añadir libro")
    print("2 - Modificar cantidad de un libro")
    print("3 - Eliminar libro")
    print("4 - Mostrar libros")
    print("5 - Ver total de libros disponibles")
    print("6 - Salir")

    opcion = input("Elige una opción: ")

    if opcion == "1":
        añadir_libro()
    elif opcion == "2":
        modificar_cantidad()
    elif opcion == "3":
        eliminar_libro()
    elif opcion == "4":
        mostrar_libros()
    elif opcion == "5":
        total_libros()
    elif opcion == "6":
        print("¡Hasta luego!")
        break
    else:
        print("Opción no válida. Intenta de nuevo.")
