"""
Sistema de Priorización de Entregas para un Banco de Alimentos
Autores: Andrés Felipe Orozco Loaiza - Santiago Rodríguez Fernández

Este módulo contiene las 6 funciones principales solicitadas en el parcial.
No se utilizan clases, archivos, librerías externas ni comprensión de listas.
"""


def registrar_hogares():
    """
    Solicita por teclado la información de 12 hogares y los almacena
    como diccionarios dentro de una lista.
    Retorna la lista completa de hogares.
    """
    hogares = []

    for i in range(12):
        print(f"\n--- Registro del hogar {i + 1} de 12 ---")
        documento = input("Documento del responsable: ")
        responsable = input("Nombre completo del responsable: ")
        barrio = input("Barrio de residencia: ")
        integrantes = int(input("Cantidad de integrantes del hogar: "))
        menores = int(input("Cantidad de menores de edad: "))
        adultos_mayores = int(input("Cantidad de adultos mayores: "))
        ingreso_mensual = float(input("Ingreso mensual estimado del hogar: "))

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
    """
    Valida que un hogar cumpla con las siguientes reglas:
    - integrantes debe ser mayor que 0
    - menores y adultos_mayores no deben ser negativos
    - la suma de menores y adultos_mayores no debe superar integrantes
    - ingreso_mensual no debe ser negativo
    Retorna True si todo se cumple, False en caso contrario.
    """
    integrantes = hogar["integrantes"]
    menores = hogar["menores"]
    adultos_mayores = hogar["adultos_mayores"]
    ingreso_mensual = hogar["ingreso_mensual"]

    if (integrantes > 0 and
            menores >= 0 and
            adultos_mayores >= 0 and
            (menores + adultos_mayores) <= integrantes and
            ingreso_mensual >= 0):
        return True
    else:
        return False


def calcular_puntaje(hogar):
    """
    Calcula el puntaje de vulnerabilidad de un hogar según las reglas:
    - +2 puntos si el ingreso es menor a 1.000.000
    - +1 punto si el ingreso está entre 1.000.000 y 2.000.000
    - +1 punto por cada menor, máximo 3 puntos
    - +2 puntos si existe al menos un adulto mayor
    - +1 punto si el hogar tiene 5 o más integrantes
    Retorna el puntaje total (entero).
    """
    puntaje = 0

    ingreso = hogar["ingreso_mensual"]
    menores = hogar["menores"]
    adultos_mayores = hogar["adultos_mayores"]
    integrantes = hogar["integrantes"]

    if ingreso < 1000000:
        puntaje = puntaje + 2
    elif ingreso >= 1000000 and ingreso < 2000000:
        puntaje = puntaje + 1

    if menores >= 3:
        puntaje = puntaje + 3
    else:
        puntaje = puntaje + menores

    if adultos_mayores > 0:
        puntaje = puntaje + 2

    if integrantes >= 5:
        puntaje = puntaje + 1

    return puntaje


def clasificar_prioridad(puntaje):
    """
    Clasifica el puntaje recibido en un nivel de prioridad:
    0-2 = Baja, 3-4 = Media, 5-6 = Alta, 7 o más = Urgente.
    Retorna el texto de la prioridad.
    """
    if puntaje <= 2:
        return "Baja"
    elif puntaje == 3 or puntaje == 4:
        return "Media"
    elif puntaje == 5 or puntaje == 6:
        return "Alta"
    else:
        return "Urgente"


def registrar_entregas(hogares):
    """
    Recorre la lista de hogares y permite marcar si el paquete fue entregado.
    Solo se puede marcar como entregado un hogar que sea válido.
    Retorna la lista de hogares con el campo 'entregado' actualizado.
    """
    for hogar in hogares:
        print(f"\nHogar de: {hogar['responsable']} - Barrio: {hogar['barrio']}")

        if validar_hogar(hogar) == True:
            respuesta = input("¿Se entregó el paquete a este hogar? (si/no): ")
            respuesta = respuesta.strip().lower()

            if respuesta == "si":
                hogar["entregado"] = True
            else:
                hogar["entregado"] = False
        else:
            print("Este hogar no es válido, no se puede registrar la entrega.")

    return hogares


def generar_resumen(hogares):
    """
    Recorre la lista de hogares y muestra en consola:
    - cantidad total de hogares válidos
    - cuántos hogares quedaron en cada nivel de prioridad
    - cuántos paquetes fueron entregados
    - cuántos paquetes están pendientes
    """
    contador_validos = 0
    contador_prioridad_baja = 0
    contador_prioridad_media = 0
    contador_prioridad_alta = 0
    contador_prioridad_urgente = 0
    contador_entregados = 0
    contador_pendientes = 0

    for hogar in hogares:
        if validar_hogar(hogar) == True:
            contador_validos = contador_validos + 1

            puntaje = calcular_puntaje(hogar)
            prioridad = clasificar_prioridad(puntaje)

            if prioridad == "Baja":
                contador_prioridad_baja = contador_prioridad_baja + 1
            elif prioridad == "Media":
                contador_prioridad_media = contador_prioridad_media + 1
            elif prioridad == "Alta":
                contador_prioridad_alta = contador_prioridad_alta + 1
            else:
                contador_prioridad_urgente = contador_prioridad_urgente + 1

            if hogar["entregado"] == True:
                contador_entregados = contador_entregados + 1
            else:
                contador_pendientes = contador_pendientes + 1

    print("\n===== RESUMEN GENERAL =====")
    print(f"Total de hogares válidos: {contador_validos}")
    print(f"Prioridad Baja: {contador_prioridad_baja}")
    print(f"Prioridad Media: {contador_prioridad_media}")
    print(f"Prioridad Alta: {contador_prioridad_alta}")
    print(f"Prioridad Urgente: {contador_prioridad_urgente}")
    print(f"Paquetes entregados: {contador_entregados}")
    print(f"Paquetes pendientes: {contador_pendientes}")
