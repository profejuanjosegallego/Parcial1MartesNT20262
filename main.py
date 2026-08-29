"""
ACDA 1: Sistema de Priorización de Entregas para Banco de Alimentos
Archivo: main.py
Programa principal que coordina todas las funciones
"""

# Importar las 6 funciones del archivo funciones.py
from funciones import registrar_hogares
from funciones import validar_hogar
from funciones import calcular_puntaje
from funciones import clasificar_prioridad
from funciones import registrar_entregas
from funciones import generar_resumen


# ============================================================================
# PROGRAMA PRINCIPAL
# ============================================================================

def main():
    """
    Programa principal que ejecuta el flujo completo del sistema.
    Coordina las 6 funciones en el orden correcto.
    """
    
    print("\n" + "="*70)
    print("BIENVENIDO AL SISTEMA DE ENTREGAS - BANCO DE ALIMENTOS")
    print("MEDELLÍN")
    print("="*70)
    
    # PASO 1: Registrar hogares
    # Solicita la cantidad de hogares (entre 1 y 20)
    # Ejecuta la función registrar_hogares() que retorna una lista de diccionarios
    hogares = registrar_hogares()
    
    # PASO 2: Mostrar información de cada hogar con prioridad
    # Recorre la lista y para cada hogar válido calcula puntaje y prioridad
    print("\n" + "="*70)
    print("ANÁLISIS DE HOGARES - PUNTAJES Y PRIORIDADES")
    print("="*70)
    
    for i in range(len(hogares)):
        hogar = hogares[i]
        print(f"\n--- HOGAR {i + 1}: {hogar['responsable']} ---")
        
        # Validar si el hogar cumple los criterios
        es_valido = validar_hogar(hogar)
        
        if es_valido:
            # Si es válido, calcular puntaje y clasificar prioridad
            puntaje = calcular_puntaje(hogar)
            prioridad = clasificar_prioridad(puntaje)
            
            print(f"Estado: VÁLIDO ✓")
            print(f"Barrio: {hogar['barrio']}")
            print(f"Integrantes: {hogar['integrantes']} (Menores: {hogar['menores']}, Mayores: {hogar['adultos_mayores']})")
            print(f"Ingreso mensual: ${hogar['ingreso_mensual']:,}")
            print(f"Puntaje de vulnerabilidad: {puntaje}")
            print(f"Prioridad: {prioridad}")
        else:
            # Si no es válido, mostrar que no cumple criterios
            print(f"Estado: INVÁLIDO ✗")
            print("Los datos no cumplen con los criterios requeridos.")
    
    # PASO 3: Registrar entregas
    # Llama a la función que permite marcar entregas (solo válidas)
    hogares = registrar_entregas(hogares)
    
    # PASO 4: Generar resumen final
    # Muestra estadísticas completas del proceso
    generar_resumen(hogares)
    
    # Mensaje final
    print("\n✓ Programa completado exitosamente.")
    print("Gracias por usar el sistema de entregas del Banco de Alimentos.\n")


# ============================================================================
# PUNTO DE ENTRADA DEL PROGRAMA
# ============================================================================

if __name__ == "__main__":
    main()
