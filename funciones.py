# 1. Función para registrar los hogares
def registrar_hogares(cantidad_hogares=12):
    lista_hogares = []
    
    for i in range(cantidad_hogares):
        print(f"\n--- Registro del Hogar #{i + 1} ---")
        responsable = input("Nombre del responsable: ")
        integrantes = int(input("Cantidad de integrantes: "))
        menores = int(input("Cantidad de menores de edad: "))
        adultos_mayores = int(input("Cantidad de adultos mayores: "))
        ingreso_mensual = float(input("Ingreso mensual del hogar: $"))
        
        hogar = {
            "responsable": responsable,
            "integrantes": integrantes,
            "menores": menores,
            "adultos_mayores": adultos_mayores,
            "ingreso_mensual": ingreso_mensual,
            "entregado": False
        }
        lista_hogares.append(hogar)
        
    return lista_hogares


# 2. Función para validar los datos del hogar
def validar_hogar(hogar):
    integrantes = hogar["integrantes"]
    menores = hogar["menores"]
    adultos_mayores = hogar["adultos_mayores"]
    ingreso_mensual = hogar["ingreso_mensual"]
    
    if integrantes <= 0:
        return False
    if menores < 0:
        return False
    if adultos_mayores < 0:
        return False
    if (menores + adultos_mayores) > integrantes:
        return False
    if ingreso_mensual < 0:
        return False
        
    return True


# 3. Función para calcular el puntaje de vulnerabilidad
def calcular_puntaje(hogar):
    ingreso = hogar["ingreso_mensual"]
    menores = hogar["menores"]
    adultos_mayores = hogar["adultos_mayores"]
    integrantes = hogar["integrantes"]
    
    puntaje = 0
    
    # Evaluación de ingresos
    if ingreso < 1000000:
        puntaje += 2
    elif ingreso <= 2000000:
        puntaje += 1
        
    # Evaluación de menores (+1 por menor, máx 3 puntos)
    if menores >= 3:
        puntaje += 3
    elif menores > 0:
        puntaje += menores
        
    # Evaluación de adultos mayores (+2 si existe al menos uno)
    if adultos_mayores >= 1:
        puntaje += 2
        
    # Evaluación de cantidad total de integrantes (+1 si tiene 5 o más)
    if integrantes >= 5:
        puntaje += 1
        
    return puntaje


# 4. Función para clasificar la prioridad según el puntaje
def clasificar_prioridad(puntaje):
    if puntaje <= 2:
        return "Baja"
    elif puntaje <= 4:
        return "Media"
    elif puntaje <= 6:
        return "Alta"
    else:
        return "Muy Alta"


# 5. Función para registrar las entregas de paquetes
def registrar_entregas(lista_hogares):
    print("\n==============================")
    print("      GESTIÓN DE ENTREGAS     ")
    print("==============================")
    
    for hogar in lista_hogares:
        es_valido = validar_hogar(hogar)
        
        if es_valido and not hogar["entregado"]:
            print(f"\nResponsable: {hogar['responsable']}")
            print(f"Integrantes: {hogar['integrantes']} | Ingreso: ${hogar['ingreso_mensual']}")
            
            confirmacion = input("¿Desea marcar el paquete como entregado? (s/n): ").lower()
            if confirmacion == "s":
                hogar["entregado"] = True
                print("-> Entrega registrada con éxito.")
            else:
                print("-> Entrega omitida.")
                
    return lista_hogares


# 6. Función para generar el resumen general
def generar_resumen(lista_hogares):
    total_validos = 0
    total_invalidos = 0
    total_entregados = 0
    baja_prioridad = 0
    media_prioridad = 0
    alta_prioridad = 0
    muy_alta_prioridad = 0
    
    for hogar in lista_hogares:
        if validar_hogar(hogar):
            total_validos += 1
            
            puntaje = calcular_puntaje(hogar)
            prioridad = clasificar_prioridad(puntaje)
            
            if prioridad == "Baja":
                baja_prioridad += 1
            elif prioridad == "Media":
                media_prioridad += 1
            elif prioridad == "Alta":
                alta_prioridad += 1
            else:
                muy_alta_prioridad += 1
                
            if hogar["entregado"]:
                total_entregados += 1
        else:
            total_invalidos += 1
            
    print("\n==============================")
    print("      RESUMEN DEL PROGRAMA    ")
    print("==============================")
    print(f"Hogares evaluados válidos: {total_validos}")
    print(f"Hogares con datos inválidos: {total_invalidos}")
    print(f"Prioridad Baja: {baja_prioridad}")
    print(f"Prioridad Media: {media_prioridad}")
    print(f"Prioridad Alta: {alta_prioridad}")
    print(f"Prioridad Muy Alta: {muy_alta_prioridad}")
    print(f"Total paquetes entregados: {total_entregados}")