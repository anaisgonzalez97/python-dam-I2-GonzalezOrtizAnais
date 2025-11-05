#Funciones básicas para trabajar con precios

def calcular_suma(precios):
    """Suma todos los precios de la lista"""
    return sum(precios)

def calcular_promedio(precios):
    """Calcula el precio promedio"""
    total = sum(precios)
    cantidad = len(precios)
    return total / cantidad

def encontrar_mas_caro(precios):
    """Encuentra el precio más alto"""
    return max(precios)

def encontrar_mas_barato(precios):
    """Encuentra el precio más bajo"""
    return min(precios)

def aplicar_descuento(precios, descuento_porcentaje):
    """Aplica un descuento a todos los precios"""
    factor_descuento = 1 - (descuento_porcentaje / 100)
    precios_con_descuento = [precio * factor_descuento for precio in precios]
    return precios_con_descuento
