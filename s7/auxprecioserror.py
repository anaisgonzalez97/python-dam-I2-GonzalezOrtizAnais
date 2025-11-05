# Módulo con manejo  de errores

def validar_precios(precios):
    """Valida que la lista de precios sea correcta"""
    if not isinstance(precios, list): #insnstance valida que sean de ese tipo
        raise TypeError("ERROR: Los precios deben estar en una lista")
    
    if len(precios) == 0:
        raise ValueError("ERROR: La lista de precios está vacía")
    
    for precio in precios:
        if not isinstance(precio, (int, float)):
            raise TypeError(f"ERROR: '{precio}' no es un número válido")
        if precio < 0:
            raise ValueError(f"ERROR: El precio ${precio} no puede ser negativo")
    
    return True

def calcular_suma_segura(precios):
    """Calcula la suma con manejo de errores"""
    try:
        validar_precios(precios)
        return sum(precios)
    except (TypeError, ValueError) as e: #si hay un error de este tipo, llamarlo a y lanzarlo
        raise e

def calcular_promedio_seguro(precios):
    """Calcula el promedio con manejo de errores"""
    try:
        validar_precios(precios)
        total = sum(precios)
        return total / len(precios)
    except ZeroDivisionError: #si se intenta dividir entre 0
        raise ValueError("ERROR: No se puede calcular promedio de lista vacía")
    except (TypeError, ValueError) as e:
        raise e

def encontrar_extremos_seguro(precios):
    """Encuentra precio máximo y mínimo con manejo de errores"""
    try:
        validar_precios(precios)
        maximo = max(precios)
        minimo = min(precios)
        return maximo, minimo
    except (TypeError, ValueError) as e:
        raise e

def aplicar_descuento_seguro(precios, descuento_porcentaje):
    """Aplica descuento con validación"""
    try:
        validar_precios(precios)
        
        if not isinstance(descuento_porcentaje, (int, float)):
            raise TypeError("ERROR: El descuento debe ser un número")
        
        if descuento_porcentaje < 0 or descuento_porcentaje > 100:
            raise ValueError("ERROR: El descuento debe estar entre 0% y 100%")
        
        factor_descuento = 1 - (descuento_porcentaje / 100) #1 = 100; una "pieza" de la qie se descuenta algo
        precios_con_descuento = [precio * factor_descuento for precio in precios]
        
        return precios_con_descuento
        
    except (TypeError, ValueError) as e:
        raise e