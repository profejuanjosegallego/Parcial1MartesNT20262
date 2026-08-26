# ==========================================
# FUNCIONES OBLIGATORIAS
# ==========================================

def registrar_hogares():
    hogares = []
    print("--- REGISTRO DE 12 HOGARES ---")
    for i in range(12):
        print(f"\n--- Hogar {i + 1} de 12 ---")
        documento = input("Documento del responsable: ")
        responsable = input("Nombre completo del responsable: ")
        barrio = input("Barrio de residencia: ")
        integrantes = int(input("Cantidad de personas en el hogar: "))
        menores = int(input("Cantidad de menores de edad: "))
        adultos_mayores = int(input("Cantidad de adultos mayores: "))
        ingreso_mensual = float(input("Ingreso mensual estimado ($): "))
        
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
        hogares.append(hogar)
    return hogares

def validar_hogar(hogar):
    if hogar["integrantes"] <= 0:
        return False
    if hogar["menores"] < 0 or hogar["adultos_mayores"] < 0:
        return False
    if (hogar["menores"] + hogar["adultos_mayores"]) > hogar["integrantes"]:
        return False
    if hogar["ingreso_mensual"] < 0:
        return False
    return True

def calcular_puntaje(hogar):
    puntaje = 0
    
    # Puntos por ingreso
    if hogar["ingreso_mensual"] < 1000000:
        puntaje += 2
    elif 1000000 <= hogar["ingreso_mensual"] <= 2000000:
        puntaje += 1
        
    # Puntos por menores (máximo 3 puntos)
    if hogar["menores"] >= 3:
        puntaje += 3
    else:
        puntaje += hogar["menores"]
        
    # Puntos por adultos mayores
    if hogar["adultos_mayores"] >= 1:
        puntaje += 2
        
    # Puntos por tamaño del hogar
    if hogar["integrantes"] >= 5:
        puntaje += 1
        
    return puntaje

def clasificar_prioridad(puntaje):
    if puntaje <= 2:
        return "Baja"
    elif puntaje <= 4:
        return "Media"
    elif puntaje <= 6:
        return "Alta"
    else:
        return "Urgente"

def registrar_entregas(hogares):
    print("\n--- CONTROL DE ENTREGAS ---")
    for hogar in hogares:
        if validar_hogar(hogar):
            print(f"\nHogar de {hogar['responsable']} (Doc: {hogar['documento']})")
            respuesta = input("¿Marcar paquete como entregado? (s/n): ")
            if respuesta.lower() == 's':
                hogar["entregado"] = True
            else:
                hogar["entregado"] = False
        else:
            print(f"\nEl hogar con documento {hogar['documento']} NO es válido. No se puede entregar paquete.")
    return hogares

def generar_resumen(hogares):
    total_validos = 0
    prioridad_baja = 0
    prioridad_media = 0
    prioridad_alta = 0
    prioridad_urgente = 0
    entregados = 0
    pendientes = 0
    
    for hogar in hogares:
        if validar_hogar(hogar):
            total_validos += 1
            
            # Clasificar prioridad
            pts = calcular_puntaje(hogar)
            prio = clasificar_prioridad(pts)
            
            if prio == "Baja":
                prioridad_baja += 1
            elif prio == "Media":
                prioridad_media += 1
            elif prio == "Alta":
                prioridad_alta += 1
            elif prio == "Urgente":
                prioridad_urgente += 1
                
            # Estado de entrega
            if hogar["entregado"]:
                entregados += 1
            else:
                pendientes += 1

    print("\n==========================================")
    print("           RESUMEN DEL SISTEMA            ")
    print("==========================================")
    print(f"Total de hogares válidos: {total_validos}")
    print("\nDistribución por Prioridad:")
    print(f"  - Baja: {prioridad_baja}")
    print(f"  - Media: {prioridad_media}")
    print(f"  - Alta: {prioridad_alta}")
    print(f"  - Urgente: {prioridad_urgente}")
    print("\nEstado de Entregas (Solo válidos):")
    print(f"  - Paquetes entregados: {entregados}")
    print(f"  - Paquetes pendientes: {pendientes}")
    print("==========================================")