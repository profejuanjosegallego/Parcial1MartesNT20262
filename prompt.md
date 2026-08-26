Rol: Actúa como un desarrollador de software junior especializado en Python básico,
con buenas prácticas de organización de código y experiencia enseñando programación
estructurada (sin clases ni librerías externas).

Contexto: Un banco de alimentos de Medellín necesita un programa en Python para
organizar solicitudes de apoyo de 12 hogares, calcular su nivel de vulnerabilidad,
priorizar la atención y controlar la entrega de paquetes alimentarios. Actualmente
el proceso es manual.

Tarea: Desarrolla un programa en Python dividido en exactamente 6 funciones:

1. registrar_hogares(): pide por teclado los datos de 12 hogares (documento,
   responsable, barrio, integrantes, menores, adultos_mayores, ingreso_mensual,
   entregado=False) y los guarda como diccionarios en una lista. Retorna la lista.
2. validar_hogar(hogar): valida integrantes > 0; menores y adultos_mayores >= 0;
   (menores + adultos_mayores) <= integrantes; ingreso_mensual >= 0. Retorna
   True/False.
3. calcular_puntaje(hogar): +2 si ingreso < 1.000.000; +1 si está entre
   1.000.000 y 2.000.000; +1 por cada menor (máx. 3); +2 si hay algún adulto
   mayor; +1 si integrantes >= 5. Retorna el puntaje.
4. clasificar_prioridad(puntaje): 0-2 Baja, 3-4 Media, 5-6 Alta, 7+ Urgente.
5. registrar_entregas(hogares): recorre la lista y permite marcar 'entregado'
   solo si el hogar es válido. Retorna la lista actualizada.
6. generar_resumen(hogares): muestra total de hogares válidos, cantidad por
   cada prioridad, entregados y pendientes.

Restricciones técnicas:
- Sin clases, archivos, bases de datos, librerías externas ni comprensión de listas.
- Solo funciones, ciclos for, condicionales, listas, diccionarios y operaciones básicas.
- Datos ingresados por teclado (input()), no datos quemados.
- Nombres de variables y funciones en español, claros y descriptivos.

Resultado esperado: Dos archivos Python.
- funciones.py: contiene las 6 funciones, cada una con docstring explicando
  su responsabilidad.
- main.py: importa las funciones y ejecuta el flujo completo (registrar,
  clasificar, registrar entregas, mostrar resumen), sin lógica de negocio propia.

El código debe compilar y ejecutarse sin errores, y las salidas en consola
deben ser legibles y claras.