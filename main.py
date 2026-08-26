"""
Sistema de Priorización de Entregas para un Banco de Alimentos
Programa principal - Parcial 1

Este archivo solo orquesta el flujo del programa.
Toda la lógica de negocio vive en funciones.py
"""

from funciones import (
    registrar_hogares,
    validar_hogar,
    calcular_puntaje,
    clasificar_prioridad,
    registrar_entregas,
    generar_resumen
)


print("===== SISTEMA DE PRIORIZACIÓN DE ENTREGAS - BANCO DE ALIMENTOS =====")

# 1. Registro de los 12 hogares
hogares = registrar_hogares()

# 2. Validación y clasificación de cada hogar
print("\n===== VALIDACIÓN Y CLASIFICACIÓN DE HOGARES =====")

for hogar in hogares:
    if validar_hogar(hogar) == True:
        puntaje = calcular_puntaje(hogar)
        prioridad = clasificar_prioridad(puntaje)

        print(f"\nResponsable: {hogar['responsable']}")
        print(f"Barrio: {hogar['barrio']}")
        print(f"Puntaje de vulnerabilidad: {puntaje}")
        print(f"Prioridad: {prioridad}")
    else:
        print(f"\nResponsable: {hogar['responsable']} - Hogar inválido, no se puede clasificar.")

# 3. Registro de entregas
print("\n===== REGISTRO DE ENTREGAS =====")
hogares = registrar_entregas(hogares)

# 4. Resumen final
generar_resumen(hogares)
