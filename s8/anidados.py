#lista de diccionarios-> biblioteca completa
#diccionarios-> cada uno de los libros
#claves-> elementos de los libros: titulo, autor, año, estado

# Lista de diccionarios principal que almacenará todos los registros de libros
biblioteca = []

# Función para añadir nuevos registros
def agregar_libro(biblioteca):
    try:
        print("\n--- AGREGAR NUEVO LIBRO ---")
        
        # Solicitar datos con validación
        titulo = input("Título del libro: ").strip() #quitar espacio blanco
        if not titulo:
            print("Error: El título no puede estar vacío")
            return biblioteca
        
        autor = input("Autor: ").strip()
        if not autor:
            print("Error: El autor no puede estar vacío")
            return biblioteca
        
        # Validar que el año sea un número
        try:
            año = int(input("Año de publicación: "))
            if año < 0 or año > 2025:
                print("Error: El año debe ser válido")
                return biblioteca
        except ValueError:
            print("Error: El año debe ser un número")
            return biblioteca
        
        # Validar que el estado sea correcto
        estado = input("Estado (leído/por leer): ").strip().lower()
        if estado not in ["leído", "por leer"]:
            print("Error: El estado debe ser 'leído' o 'por leer'")
            return biblioteca
        
        # Verificar duplicados (mismo título y autor)
        for libro in biblioteca:
            if libro["titulo"].lower() == titulo.lower() and libro["autor"].lower() == autor.lower():
                print("Error: Este libro ya existe en la biblioteca")
                return biblioteca
        
        # Crear el nuevo registro (diccionario)
        nuevo_libro = {
            "titulo": titulo,
            "autor": autor,
            "año": año,
            "estado": estado
        }
        
        # Añadir a la lista
        biblioteca.append(nuevo_libro)
        print(f"Libro '{titulo}' agregado exitosamente!")
        
    except Exception as e:
        print(f"Error inesperado: {e}")

# Función para buscar libros
def buscar_libro(biblioteca):
    print("\n--- BUSCAR LIBRO ---")
    print("1. Buscar por título")
    print("2. Buscar por autor")
    print("3. Buscar por estado")
    
    try:
        opcion = int(input("Selecciona una opción: "))
        
        if opcion == 1:
            criterio = "titulo"
            valor = input("Ingresa el título a buscar: ").strip().lower()
        elif opcion == 2:
            criterio = "autor" 
            valor = input("Ingresa el autor a buscar: ").strip().lower()
        elif opcion == 3:
            criterio = "estado"
            valor = input("Ingresa el estado (leído/por leer): ").strip().lower()
        else:
            print("Opción no válida")
            return biblioteca
        
        # Buscar coincidencias
        resultados = []
        for libro in biblioteca:
            if valor in libro[criterio].lower():
                resultados.append(libro)
        
        # Mostrar resultados
        if resultados:
            print(f"\nSe encontraron {len(resultados)} libro(s):")
            for libro in resultados:
                print(f"'{libro['titulo']}' - {libro['autor']} ({libro['año']}) - {libro['estado']}")
        else:
            print("No se encontraron libros con ese criterio")
            
    except ValueError:
        print("Error: Debes ingresar un número válido")
    except KeyError:
        print("Error en el criterio de búsqueda")

# Función para calcular estadísticas
def calcular_estadisticas(biblioteca):
    if not biblioteca:
        print("No hay libros en la biblioteca")
        return biblioteca
    
    print("\n--- ESTADÍSTICAS ---")
    
    # Calcular promedio de años
    años = [libro["año"] for libro in biblioteca]
    promedio_año = sum(años) / len(años)
    
    # Libro más antiguo y más reciente
    año_mas_antiguo = min(años)
    año_mas_reciente = max(años)
    
    # Contar por estado
    libros_leidos = sum(1 for libro in biblioteca if libro["estado"] == "leído")
    libros_por_leer = sum(1 for libro in biblioteca if libro["estado"] == "por leer")
    
    # Mostrar resultados
    print(f"Total de libros: {len(biblioteca)}")
    print(f"Año promedio de publicación: {promedio_año:.0f}") #numero con 0 decimales
    print(f"Libro más antiguo: {año_mas_antiguo}")
    print(f"Libro más reciente: {año_mas_reciente}")
    print(f"Libros leídos: {libros_leidos}")
    print(f"Libros por leer: {libros_por_leer}")

# Función para mostrar todos los libros
def mostrar_biblioteca(biblioteca):
    if not biblioteca:
        print("La biblioteca está vacía")
        return biblioteca
    
    print("\n--- BIBLIOTECA COMPLETA ---")
    for i, libro in enumerate(biblioteca, 1):
        print(f"{i}. '{libro['titulo']}' - {libro['autor']} ({libro['año']}) - {libro['estado']}")

# NUEVA FUNCIÓN: Marcar libro como leído
def marcar_leido(biblioteca):
    if not biblioteca:
        print("No hay libros en la biblioteca")
        return biblioteca
    
    print("\n--- LIBROS POR LEER ---")
    # Mostrar solo libros por leer
    por_leer = [libro for libro in biblioteca if libro["estado"] == "por leer"] #CREAR LISTA NUEVA "por_leer"
    
    if not por_leer:
        print("¡Todos los libros están leídos!")
        return biblioteca
    
    for i, libro in enumerate(por_leer, 1): #recorre la lista
        print(f"{i}. {libro['titulo']} - {libro['autor']}")
    
    try:
        opcion = int(input("\nNúmero del libro a marcar como leído: ")) - 1 #para que quede en 0
        if 0 <= opcion < len(por_leer): # SI opcion está entre 0 y el total de libros - 1
            # Encontrar el libro en la lista principal y cambiar estado
            libro_a_marcar = por_leer[opcion]
            for libro in biblioteca:
                if libro["titulo"] == libro_a_marcar["titulo"]:
                    libro["estado"] = "leído"
                    print(f"¡'{libro['titulo']}' marcado como leído!")
                    break
        else:
            print("Número inválido")
    except ValueError:
        print("Debes ingresar un número")        

# Menú principal
def menu_principal():
    # La lista de diccionarios "biblioteca" se crea DENTRO de la función principal
    biblioteca = [
        {"titulo": "Cien años de soledad", "autor": "Gabriel García Márquez", "año": 1967, "estado": "leído"},
        {"titulo": "1984", "autor": "George Orwell", "año": 1949, "estado": "por leer"},
        {"titulo": "El principito", "autor": "Antoine de Saint-Exupéry", "año": 1943, "estado": "leído"},
        {"titulo": "El brillo de las luciérnagas", "autor": "Paul Pen", "año": 2019, "estado": "leído"}
    ]
    
    while True:
        print("\n" + "="*50)
        print("MI BIBLIOTECA PERSONAL")
        print("="*50)
        print("1. Agregar libro")
        print("2. Buscar libro") 
        print("3. Ver estadísticas")
        print("4. Mostrar todos los libros")
        print("5. Marcar un libro como leído")
        print("6. Salir")
        
        try:
            opcion = int(input("Selecciona una opción: "))
            
            if opcion == 1:
                biblioteca = agregar_libro(biblioteca)  # Pasa y recibe la lista
            elif opcion == 2:
                buscar_libro(biblioteca)  # Solo pasa la lista
            elif opcion == 3:
                calcular_estadisticas(biblioteca)  # Solo pasa la lista
            elif opcion == 4:
                mostrar_biblioteca(biblioteca)  # Solo pasa la lista
            elif opcion == 5:
                biblioteca = marcar_leido(biblioteca)  # Pasa y recibe la lista
            elif opcion == 6:
                print("¡Hasta pronto!")
                break
            else:
                print("Opción no válida")
                
        except ValueError:
            print("Error: Debes ingresar un número")

# Ejecutar el programa
if __name__ == "__main__":
    menu_principal()