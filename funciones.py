"""
ACDA 1: Funciones del Sistema de Priorización de Entregas
Archivo: funciones.py
Contiene las 6 funciones principales requeridas
"""

# ============================================================================
# FUNCIÓN 1: REGISTRAR HOGARES
# ============================================================================

def solicitar_cantidad_hogares():
    """
    Solicita la cantidad de hogares a registrar (entre 1 y 20).
    Si el número no está en rango, ajusta al rango válido.
    Retorna la cantidad validada.
    """
    print("\n¿Cuántos hogares desea registrar? (1-20): ")
    cantidad = int(input())
    
    # Validar cantidad con condicionales
    if cantidad < 1:
        cantidad = 1
    elif cantidad > 20:
        cantidad = 20
    
    return cantidad


def registrar_hogares():
    """
    Solicita y registra hogares.
    La cantidad es variable (entre 1 y 20).
    Cada hogar se almacena como un diccionario en una lista.
    Retorna la lista completa de hogares.
    """
    hogares = []
    
    print("\n" + "="*70)
    print("REGISTRO DE HOGARES - BANCO DE ALIMENTOS")
    print("="*70)
    
    # Solicitar cantidad de hogares
    cantidad_hogares = solicitar_cantidad_hogares()
    
    print(f"\nSe registrarán {cantidad_hogares} hogares.\n")
    
    for i in range(cantidad_hogares):
        print(f"\n--- HOGAR {i + 1} ---")
        
        # Solicitar datos del hogar
        documento = input("Documento del responsable: ").strip()
        responsable = input("Nombre completo del responsable: ").strip()
        barrio = input("Barrio de residencia: ").strip()
        integrantes = int(input("Cantidad total de integrantes: "))
        menores = int(input("Cantidad de menores de edad: "))
        adultos_mayores = int(input("Cantidad de adultos mayores: "))
        ingreso_mensual = int(input("Ingreso mensual estimado ($): "))
        
        # Crear diccionario del hogar
        hogar = {
            "documento": documento,
            "responsable": responsable,
            "barrio": barrio,
            "integrantes": integrantes,
            "menores": menores,
            "adultos_mayores": adultos_mayores,
            "ingreso_mensual": ingreso_mensual,
            "entregado": False
        }
        
        # Agregar hogar a la lista
        hogares.append(hogar)
        print("✓ Hogar registrado exitosamente.")
    
    return hogares


# ============================================================================
# FUNCIÓN 2: VALIDAR HOGAR
# ============================================================================

def validar_hogar(hogar):
    """
    Valida que un hogar cumpla con los criterios:
    - integrantes > 0
    - menores >= 0 y adultos_mayores >= 0
    - menores + adultos_mayores <= integrantes
    - ingreso_mensual >= 0
    
    Parámetro: hogar (diccionario)
    Retorna: True si es válido, False en caso contrario
    """
    
    # Validación 1: integrantes debe ser mayor que 0
    if hogar["integrantes"] <= 0:
        return False
    
    # Validación 2: menores y adultos_mayores no pueden ser negativos
    if hogar["menores"] < 0 or hogar["adultos_mayores"] < 0:
        return False
    
    # Validación 3: la suma de menores y adultos_mayores no puede exceder integrantes
    suma_especiales = hogar["menores"] + hogar["adultos_mayores"]
    if suma_especiales > hogar["integrantes"]:
        return False
    
    # Validación 4: ingreso mensual no puede ser negativo
    if hogar["ingreso_mensual"] < 0:
        return False
    
    return True


# ============================================================================
# FUNCIÓN 3: CALCULAR PUNTAJE
# ============================================================================

def calcular_puntaje(hogar):
    """
    Calcula el puntaje de vulnerabilidad de un hogar:
    - +2 si ingreso < $1.000.000
    - +1 si ingreso entre $1.000.000 y $2.000.000
    - +1 por cada menor (máximo 3 puntos)
    - +2 si existe al menos un adulto mayor
    - +1 si el hogar tiene 5 o más integrantes
    
    Parámetro: hogar (diccionario)
    Retorna: puntaje (entero)
    """
    puntaje = 0
    
    # Criterio 1: Ingreso mensual
    if hogar["ingreso_mensual"] < 1000000:
        puntaje = puntaje + 2
    elif hogar["ingreso_mensual"] <= 2000000:
        puntaje = puntaje + 1
    
    # Criterio 2: Menores de edad (máximo 3 puntos)
    cantidad_menores = hogar["menores"]
    if cantidad_menores > 3:
        puntaje = puntaje + 3
    else:
        puntaje = puntaje + cantidad_menores
    
    # Criterio 3: Adultos mayores
    if hogar["adultos_mayores"] > 0:
        puntaje = puntaje + 2
    
    # Criterio 4: Cantidad de integrantes
    if hogar["integrantes"] >= 5:
        puntaje = puntaje + 1
    
    return puntaje


# ============================================================================
# FUNCIÓN 4: CLASIFICAR PRIORIDAD
# ============================================================================

def clasificar_prioridad(puntaje):
    """
    Clasifica la prioridad según el puntaje:
    - 0 a 2: Baja
    - 3 a 4: Media
    - 5 a 6: Alta
    - 7 o más: Urgente
    
    Parámetro: puntaje (entero)
    Retorna: prioridad (texto)
    """
    
    if puntaje <= 2:
        prioridad = "Baja"
    elif puntaje <= 4:
        prioridad = "Media"
    elif puntaje <= 6:
        prioridad = "Alta"
    else:
        prioridad = "Urgente"
    
    return prioridad


# ============================================================================
# FUNCIÓN 5: REGISTRAR ENTREGAS
# ============================================================================

def registrar_entregas(hogares):
    """
    Recorre los hogares válidos y permite marcar si el paquete fue entregado.
    Solo se puede marcar como entregado un hogar que sea válido.
    
    Parámetro: hogares (lista de diccionarios)
    Retorna: hogares actualizada (lista de diccionarios)
    """
    
    print("\n" + "="*70)
    print("REGISTRO DE ENTREGAS")
    print("="*70)
    
    for i in range(len(hogares)):
        hogar = hogares[i]
        
        # Validar el hogar
        if validar_hogar(hogar):
            print(f"\nHogar {i + 1}: {hogar['responsable']} - {hogar['barrio']}")
            print(f"Documento: {hogar['documento']}")
            print(f"Integrantes: {hogar['integrantes']}")
            
            # Solicitar si fue entregado
            respuesta = input("¿Fue entregado el paquete? (s/n): ").strip().lower()
            
            if respuesta == 's':
                hogares[i]["entregado"] = True
                print("✓ Entrega registrada.")
            else:
                print("✗ Paquete pendiente de entrega.")
        else:
            print(f"\nHogar {i + 1}: {hogar['responsable']} - INVÁLIDO (datos incorrectos)")
            print("No se puede registrar entrega de un hogar con datos inválidos.")
    
    return hogares


# ============================================================================
# FUNCIÓN 6: GENERAR RESUMEN
# ============================================================================

def generar_resumen(hogares):
    """
    Recorre la lista de hogares y muestra:
    - Cantidad total de hogares válidos
    - Cantidad de hogares por cada prioridad
    - Paquetes entregados
    - Paquetes pendientes
    
    Parámetro: hogares (lista de diccionarios)
    Retorna: No retorna nada (solo imprime)
    """
    
    print("\n" + "="*70)
    print("RESUMEN GENERAL - BANCO DE ALIMENTOS")
    print("="*70)
    
    # Contadores
    total_validos = 0
    prioritarios_baja = 0
    prioritarios_media = 0
    prioritarios_alta = 0
    prioritarios_urgente = 0
    total_entregados = 0
    total_pendientes = 0
    
    # Recorrer todos los hogares
    for hogar in hogares:
        # Validar hogar
        if validar_hogar(hogar):
            total_validos = total_validos + 1
            
            # Calcular puntaje y prioridad
            puntaje = calcular_puntaje(hogar)
            prioridad = clasificar_prioridad(puntaje)
            
            # Contar por prioridad
            if prioridad == "Baja":
                prioritarios_baja = prioritarios_baja + 1
            elif prioridad == "Media":
                prioritarios_media = prioritarios_media + 1
            elif prioridad == "Alta":
                prioritarios_alta = prioritarios_alta + 1
            elif prioridad == "Urgente":
                prioritarios_urgente = prioritarios_urgente + 1
            
            # Contar entregas
            if hogar["entregado"]:
                total_entregados = total_entregados + 1
            else:
                total_pendientes = total_pendientes + 1
    
    # Mostrar resultados
    print(f"\n📊 HOGARES VÁLIDOS: {total_validos} de {len(hogares)}")
    print(f"\n📋 DISTRIBUCIÓN POR PRIORIDAD:")
    print(f"   • Baja:    {prioritarios_baja}")
    print(f"   • Media:   {prioritarios_media}")
    print(f"   • Alta:    {prioritarios_alta}")
    print(f"   • Urgente: {prioritarios_urgente}")
    print(f"\n🚚 ESTADO DE ENTREGAS:")
    print(f"   • Entregados:  {total_entregados}")
    print(f"   • Pendientes:  {total_pendientes}")
    print("\n" + "="*70)
