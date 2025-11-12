import datetime  # Módulo para trabajar con fechas

# Lista global para almacenar las tareas
tareas = []

def agregar_tarea(nombre, prioridad):
#Función para agregar una nueva tarea a la lista
    try:
        # Verificar que la prioridad sea un número válido
        if prioridad < 1 or prioridad > 3:
            return "Error: La prioridad debe ser 1, 2 o 3"
        
        # Crear diccionario con la tarea
        tarea = {
            "nombre": nombre,
            "prioridad": prioridad,
            "fecha": datetime.datetime.now().strftime("%Y-%m-%d %H:%M"), #"String Format Time" | fecha y hora actuales en ese formato
            "completada": False #de forma predeterminada
        }
        
        # Agregar a la lista
        tareas.append(tarea)
        return f"¡Tarea '{nombre}' agregada correctamente!"
    
    except Exception as e:
        return f"Error al agregar tarea: {e}"

def marcar_completada(numero_tarea):
    """
    Función para marcar una tarea como completada
    
    Parámetros:
    numero_tarea (int): Número de la tarea en la lista (empezando desde 1)
    
    Retorna:
    str: Mensaje confirmando la acción
    """
    try:
        # Convertir a índice (restamos 1 porque las listas empiezan en 0)
        indice = numero_tarea - 1 #para que lo que da el usuario se adapte a como lo lee el ordenador
        
        # Verificar que el índice sea válido
        if indice < 0 or indice >= len(tareas):
            return "Error: Número de tarea no válido"
        
        # Marcar como completada
        tareas[indice]["completada"] = True
        return f"¡Tarea '{tareas[indice]['nombre']}' marcada como COMPLETADA!"
    
    except ValueError:
        return "Error: Debes ingresar un número"
    except Exception as e:
        return f"Error inesperado: {e}"

def mostrar_tareas():
    """
    Función para mostrar todas las tareas en formato legible
    
    Retorna:
    str: Texto formateado con todas las tareas
    """
    try:
        if not tareas:  # Si la lista está vacía
            return "No hay tareas registradas."
        
        resultado = "\n--- LISTA DE TAREAS ---\n"
        
        for i, tarea in enumerate(tareas, 1):
            # Determinar el estado
            estado = "✓ COMPLETADA" if tarea["completada"] else "✗ PENDIENTE"
            
            # Determinar la prioridad
            if tarea["prioridad"] == 1:
                prioridad_texto = "ALTA"
            elif tarea["prioridad"] == 2:
                prioridad_texto = "MEDIA"
            else:
                prioridad_texto = "BAJA"
            
            # Formatear cada tarea
            # += -> añadir lo que ya tengo, cada vez que pasa por una tarea le añade lo nuevo
            resultado += f"{i}. {tarea['nombre']}\n" 
            resultado += f"   Prioridad: {prioridad_texto} | Estado: {estado}\n"
            resultado += f"   Fecha: {tarea['fecha']}\n\n"
        
        return resultado
    
    except Exception as e:
        return f"Error al mostrar tareas: {e}"

# PROGRAMA PRINCIPAL - Menú interactivo
def main():
    """
    Función principal que muestra el menú y maneja las opciones
    """
    print("CONTROL DE TAREAS DIARIAS ")
    print("=" * 30)
    
    while True:
        print("\n¿Qué quieres hacer?")
        print("1. Agregar tarea")
        print("2. Marcar tarea como completada")
        print("3. Ver todas las tareas")
        print("4. Salir")
        
        try:
            opcion = input("Elige una opción (1-4): ")
            
            if opcion == "1":
                # Agregar nueva tarea
                nombre = input("Nombre de la tarea: ")
                prioridad = int(input("Prioridad (1=Alta, 2=Media, 3=Baja): "))
                resultado = agregar_tarea(nombre, prioridad)
                print(resultado)
                
            elif opcion == "2":
                # Marcar tarea como completada
                if not tareas:
                    print("No hay tareas para completar.")
                else:
                    print(mostrar_tareas())
                    numero = int(input("Número de tarea a completar: "))
                    resultado = marcar_completada(numero)
                    print(resultado)
                    
            elif opcion == "3":
                # Mostrar todas las tareas
                print(mostrar_tareas())
                
            elif opcion == "4":
                # Salir del programa
                print("¡Hasta pronto!")
                break
                
            else:
                print("Opción no válida. Elige 1, 2, 3 o 4.")
                
        except ValueError:
            print("Error: Ingresa un número válido")
        except Exception as e:
            print(f"Error inesperado: {e}")

# Ejecutar el programa
if __name__ == "__main__":
    main()