#Programa principal que usa las funciones básicas

from auxprecios import (
    calcular_suma, 
    calcular_promedio, 
    encontrar_mas_caro, 
    encontrar_mas_barato,
    aplicar_descuento
)

# Lista de precios de ejemplo
precios_ejemplo = [100, 50, 200, 75, 150, 80]

print("=== ANÁLISIS BÁSICO DE PRECIOS ===")
print(f"Precios originales: {precios_ejemplo}")

# Usamos las funciones básicas
suma_total = calcular_suma(precios_ejemplo)
promedio_precios = calcular_promedio(precios_ejemplo)
precio_mas_caro = encontrar_mas_caro(precios_ejemplo)
precio_mas_barato = encontrar_mas_barato(precios_ejemplo)
precios_con_descuento = aplicar_descuento(precios_ejemplo, 20)

# Mostramos resultados
print("\n--- RESULTADOS ---")
print(f"Suma total: €{suma_total}")
print(f"Precio promedio: €{promedio_precios:.2f}")
print(f"Precio más caro: €{precio_mas_caro}")
print(f"Precio más barato: €{precio_mas_barato}")
print(f"Precios con 20% de descuento: {[f'€{p:.2f}' for p in precios_con_descuento]}")
#p  cada precio de la lista
#:.2f formatea el número con 2 decimales

print("\n=== ANÁLISIS COMPLETADO ===")