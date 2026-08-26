# ==========================================
# PROGRAMA PRINCIPAL
# ==========================================

from funciones import generar_resumen, registrar_entregas, registrar_hogares


def main():
    # 1. Registrar los 12 hogares
    lista_hogares = registrar_hogares()
    
    # 2. Control de entregas
    lista_hogares = registrar_entregas(lista_hogares)
    
    # 3. Mostrar resumen general
    generar_resumen(lista_hogares)

# Ejecución del programa
if __name__ == "__main__":
    main()