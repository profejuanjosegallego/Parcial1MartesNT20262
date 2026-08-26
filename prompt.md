Actúa como un programador experto y profesor de Python especializado en fundamentos de programación y estructuras de datos básicas. Estoy resolviendo una evaluación práctica para un sistema de priorización de entregas de un banco de alimentos en Medellín. Necesito un programa ejecutable en Python que organice solicitudes de apoyo, calcule la vulnerabilidad del hogar, determine su prioridad de atención y gestione la entrega de paquetes alimentarios.

Tarea:

Escribe el código completo en Python creando un flujo con un programa principal (main()) y exactamente las siguientes 6 funciones:

registrar_hogares(): Solicita los datos de 12 hogares por teclado (documento, responsable, barrio, integrantes, menores, adultos mayores, ingreso mensual y entregado en False), los guarda como diccionarios dentro de una lista y la retorna.

validar_hogar(hogar): Valida que integrantes sea > 0, menores y adultos mayores no sean negativos, su suma no supere a los integrantes y el ingreso no sea negativo. Retorna True o False.

calcular_puntaje(hogar): Calcula los puntos de vulnerabilidad según ingreso, cantidad de menores (máx 3 pts), presencia de adultos mayores y tamaño del hogar. Retorna el puntaje.

clasificar_prioridad(puntaje): Retorna la prioridad ("Baja", "Media", "Alta" o "Urgente") según el rango de puntos.

registrar_entregas(hogares): Recorre los hogares y permite marcar como entregado solo a los hogares válidos. Retorna la lista actualizada.

generar_resumen(hogares): Muestra en consola el total de hogares válidos, conteo por prioridad y estado de paquetes (entregados vs. pendientes).

Presenta la respuesta únicamente con un bloque de código Python limpio, bien estructurado y comentado por secciones, seguido de una breve viñeta explicativa que confirme el cumplimiento de los requisitos.

Usar exclusivamente funciones, ciclos (for/while), condicionales (if/else), listas, diccionarios, variables y entradas/salidas básicas de consola (input/print). Todos los datos deben solicitarse por consola con input(), sin datos hardcodeados/quemados. Respetar de forma estricta los nombres exactos de las 6 funciones solicitadas.

Prohibido: No usar clases (POO), librerías externas, archivos, bases de datos, comprensión de listas (list comprehensions) ni funciones avanzadas.