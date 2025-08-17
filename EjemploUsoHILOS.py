import threading
import time
from colorama import init, Fore

"""
Ejemplo: Dos tareas a la vez con hilos
Supón que quieres mostrar un mensaje animado (como un reloj) mientras el usuario puede escribir su nombre.
Sin hilos, solo podrías hacer una cosa a la vez.
Con hilos, puedes hacer ambas cosas al mismo tiempo.

¿Qué pasa aquí?
El hilo animado (animacion_reloj) imprime un símbolo diferente cada 0.2 segundos, simulando un reloj girando.
El hilo principal espera a que el usuario escriba su nombre.
Ambos ocurren a la vez: puedes ver la animación mientras escribes.
Cuando terminas de escribir, el hilo animado se detiene.
¿Por qué es útil?
Puedes mostrar animaciones, cargar datos, escuchar música, etc., mientras el usuario hace otra cosa.
Así tu programa es más interactivo y no se queda "parado" esperando.

"""

init(autoreset=True)

# Variable global para controlar la animación
animar = True

# Esta función será el "hilo animado"
def animacion_reloj():
    simbolos = ["|", "/", "-", "\\"]
    i = 0
    while animar:
        print(f"\r{Fore.YELLOW}Esperando tu nombre... {simbolos[i % len(simbolos)]}", end="")
        time.sleep(0.2)
        i += 1
    print("\r" + " " * 40, end="\r")  # Limpia la línea al terminar

# Inicia el hilo animado
hilo = threading.Thread(target=animacion_reloj, daemon=True)
hilo.start()

# Mientras el hilo está animando, el usuario puede escribir
nombre = input(Fore.CYAN + "\nEscribe tu nombre y pulsa ENTER: ")

# Cuando el usuario termina, detenemos la animación
animar = False
time.sleep(0.3)  # Da tiempo a que el hilo limpie la línea

print(Fore.GREEN + f"\n¡Hola, {nombre}! Has visto la animación mientras escribías.")