"""
Script que imprime los 10 puertos más comunes en ciberseguridad
Usando conceptos de la Semana 2 de CS50P: Listas, Bucles for y Funciones
"""

import socket
import sys

# Intentamos importar colorama, si no está disponible, usamos None
try:
    import colorama  # type: ignore
    COLORAMA_DISPONIBLE = True
except ImportError:
    colorama = None  # type: ignore
    COLORAMA_DISPONIBLE = False

def mostrar_puertos(lista_puertos):
    """
    Función que recibe una lista de puertos y los imprime usando un bucle for.
    
    Args:
        lista_puertos: Una lista con números de puertos
    """
    # Imprimimos un encabezado
    print("Quieres ver que puertos estan abiertos? ")
    print("-" * 50)
    
    # Usamos un bucle for para iterar sobre cada elemento de la lista
    # El bucle for toma cada elemento de la lista 'lista_puertos' uno por uno
    # y lo asigna a la variable 'puerto' en cada iteración
    for puerto in lista_puertos:
        # En cada iteración, imprimimos el puerto actual
        print(f"Puerto {puerto}")
    
    print("-" * 50)
    print(f"Total de puertos: {len(lista_puertos)}")


def puerto_abierto(host, puerto, timeout=0.5):
    """
    Intenta conectarse a (host, puerto). Si logra conectar, asumimos "abierto".
    Usamos TCP (SOCK_STREAM), típico para muchos servicios.

    Retorna:
        True si parece abierto, False si parece cerrado / filtrado.
    """
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(timeout)
        # connect_ex devuelve 0 si conectó; si no, devuelve un código de error.
        return s.connect_ex((host, puerto)) == 0


def mostrar_estado_puertos(host, lista_puertos):
    """
    Recorre una lista de puertos e imprime si están abiertos o cerrados en un host.
    Usa colorama para colorear: verde para abiertos, rojo para cerrados.
    """
    print(f"\nProbando puertos en {host} (TCP):")
    print("-" * 50)
    for puerto in lista_puertos:
        esta_abierto = puerto_abierto(host, puerto)
        if esta_abierto:
            # Puerto abierto: color verde
            # Con autoreset=True, el color se resetea automáticamente después del print
            if COLORAMA_DISPONIBLE:
                print(f"Puerto {puerto}: {colorama.Fore.GREEN}ABIERTO{colorama.Style.RESET_ALL}")
            else:
                print(f"Puerto {puerto}: ABIERTO")
        else:
            # Puerto cerrado: color rojo
            if COLORAMA_DISPONIBLE:
                print(f"Puerto {puerto}: {colorama.Fore.RED}CERRADO{colorama.Style.RESET_ALL}")
            else:
                print(f"Puerto {puerto}: CERRADO")
    print("-" * 50)


def main():
    """
    Función principal que define la lista de puertos y llama a mostrar_puertos.
    Esta es la función que contiene la lógica principal del programa.
    """
    # Inicializamos colorama para que los colores funcionen correctamente
    # autoreset=True hace que los colores se reseteen automáticamente después de cada print
    if COLORAMA_DISPONIBLE:
        colorama.init(autoreset=True)
    
    # Definimos una lista con los puertos más comunes en ciberseguridad
    # Una lista es una colección ordenada de elementos en Python
    puertos = range(1, 1025)
    
    # Llamamos a la función mostrar_puertos pasándole la lista como argumento
    mostrar_puertos(puertos)

    # Opcional: probar puertos con socket.
    # Si pasas un host por consola, lo usamos. Si no, probamos localhost.
    # Ejemplo: python3 puertos_ciberseguridad.py 192.168.1.10
    host = input("ingresa el host que quieres escanear: ").strip()
    if len(sys.argv) == 2:
        host = sys.argv[1]
    mostrar_estado_puertos(host, puertos)


# Convención de CS50P: solo ejecutar main() si el script se ejecuta directamente
# Esto permite que el módulo pueda ser importado sin ejecutar el código automáticamente
if __name__ == "__main__":
    main()
