# precioserror.py - Programa con manejo completo de errores

from auxprecioserror import (
    calcular_suma_segura,
    calcular_promedio_seguro,
    encontrar_extremos_seguro,
    aplicar_descuento_seguro,
    validar_precios
)

def analizar_precios_con_errores(precios, descuento=10): #si no se da decuento, se pone automaticamente 10
    """Analiza precios con manejo completo de errores"""
    
    print(f"\n{'='*50}")
    print(f"ANALIZANDO: {precios}")
    print(f"{'='*50}")
    
    resultados = {}
    
    # BLOQUE PRINCIPAL con try
    try:
        print("1️. Validando precios...")
        validar_precios(precios)
        print("Validación exitosa")
        
    except (TypeError, ValueError) as error:
        print(f"Error en validación: {error}")
        resultados['error'] = str(error)
        return resultados
    
    else:
        # Si la validación sale bien, hacemos cálculos
        try:
            print("2️. Calculando suma...")
            suma = calcular_suma_segura(precios)
            print(f"Suma: €{suma}")
            resultados['suma'] = suma
            
        except Exception as error:
            print(f"Error en suma: {error}")
            resultados['error_suma'] = str(error)
    
    # Bloque FINALLY - siempre se ejecuta
    finally:
        print("Paso de validación terminado")
    
    # Más cálculos con su propio manejo de errores
    try:
        print("3️. Calculando promedio...")
        promedio = calcular_promedio_seguro(precios)
        print(f"Promedio: €{promedio:.2f}")
        resultados['promedio'] = promedio
        
    except Exception as error:
        print(f"Error en promedio: {error}")
        resultados['error_promedio'] = str(error)
    
    try:
        print("4️. Buscando precios extremos...")
        maximo, minimo = encontrar_extremos_seguro(precios)
        print(f"Más caro: €{maximo}, Más barato: ${minimo}")
        resultados['maximo'] = maximo
        resultados['minimo'] = minimo
        
    except Exception as error:
        print(f"Error buscando extremos: {error}")
        resultados['error_extremos'] = str(error)
    
    try:
        print(f"5. Aplicando {descuento}% de descuento...")
        precios_con_descuento = aplicar_descuento_seguro(precios, descuento)
        print(f"Precios con descuento: {[f'€{p:.2f}' for p in precios_con_descuento]}")
        resultados['precios_con_descuento'] = precios_con_descuento
        
    except Exception as error:
        print(f"Error aplicando descuento: {error}")
        resultados['error_descuento'] = str(error)
    
    return resultados

def ejecutar_pruebas():
    """Ejecuta diferentes casos de prueba"""
    
    print("INICIANDO PRUEBAS CON MANEJO DE ERRORES")
    
    # PRUEBA 1: Lista normal (debería funcionar)
    print("\n" + "PRUEBA 1: Lista normal")
    precios_buenos = [100, 50, 200, 75, 150]
    resultado1 = analizar_precios_con_errores(precios_buenos, 15)
    
    # PRUEBA 2: Lista vacía (debería fallar)
    print("\n" + "PRUEBA 2: Lista vacía (Caso de error)")
    precios_vacios = []
    resultado2 = analizar_precios_con_errores(precios_vacios)
    
    # PRUEBA 3: Lista con texto (debería fallar)
    print("\n" + "PRUEBA 3: Lista con texto (Caso de error)")
    precios_malos = [100, "cincuenta", 200, "barato"]
    resultado3 = analizar_precios_con_errores(precios_malos)
    
    # PRUEBA 4: Descuento inválido
    print("\n" + "PRUEBA 4: Descuento inválido (Caso de error)")
    precios_normales = [100, 200, 300]
    resultado4 = analizar_precios_con_errores(precios_normales, -10)  # Descuento negativo
    
    print("\n" + "="*60)
    print("TODAS LAS PRUEBAS COMPLETADAS")
    print("="*60)

if __name__ == "__main__":
    ejecutar_pruebas()