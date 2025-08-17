"""
El objetivo de este script es proporcionar un menú de mantenimiento del sistema, son comandos
básicos para realizar tareas comunes de mantenimiento en un sistema operativo Windows.
Estas tareas incluyen la actualización de programas, limpieza de la papelera de reciclaje,
comprobación de errores en el disco duro, desfragmentación del disco duro y finalización de
procesos innecesarios. El script utiliza la biblioteca os para ejecutar comandos del sistema.

 Los pasos para pasar un script de Python a un ejecutable son:
1. Instalar PyInstaller: `pip install pyinstaller`
2. Ejecutar el comando: `python -m PyInstaller --onefile mantenimientoSistema.py`
3. Esto generará un archivo ejecutable en la carpeta `dist`.
4. Puedes ejecutar el archivo .exe generado para realizar las tareas de mantenimiento.
5. Para mejorar la experiencia del usuario, se ha añadido color a la salida del terminal
   utilizando la biblioteca `colorama`. Asegúrate de instalarla con `pip install colorama`.

"""
import os
import sys
import time #Time se utiliza para manejar el tiempo, como pausas o temporizadores.
import threading # Threading sirve para crear hilos en Python, esto nos permite ejecutar tareas en paralelo.
from colorama import init, Fore, Style #colorama es una biblioteca que permite imprimir texto en colores en la terminal, mejorando la legibilidad y estética de la salida del programa.
# Inicializa colorama para que los colores se reseteen automáticamente al final de cada impresión


init(autoreset=True)

animar = True

def titulo_animado(texto):
    colores = [Fore.RED, Fore.YELLOW, Fore.GREEN, Fore.CYAN, Fore.BLUE, Fore.MAGENTA, Fore.WHITE]
    i = 0
    while animar:
        color = colores[i % len(colores)]
        print(f"\r{color}{Style.BRIGHT}{texto}{Style.RESET_ALL}", end="")
        time.sleep(0.2)
        i += 1

while True:
    os.system("cls")
    animar = True
    hilo = threading.Thread(target=titulo_animado, args=("**MANTENIMIENTO DEL SISTEMA**",), daemon=True)
    hilo.start()

    # Espera un poco para que el título se vea antes de imprimir el menú
    time.sleep(0.5)
    print()  # Baja a la siguiente línea para el menú

    print(Fore.CYAN + "#" * 48)
    print(Fore.RED + "   \n   NOTA.- Recuerda que debes ejecutar este script\n   como ADMINISTRADOR ya que ALGUNOS COMANDOS\n"
          "   requieren permisos elevados.\n")
    print(Fore.CYAN + "#" * 48 + "\n")
    print(Fore.GREEN + "    1. Comprobar y actualizar programas")
    print(Fore.LIGHTBLUE_EX + "    2. Limpiar papelera de reciclaje")
    print(Fore.LIGHTMAGENTA_EX + "    3. Comprobar errores en el disco duro")
    print(Fore.LIGHTRED_EX + "    4. Desfragmentar el disco duro")
    print(Fore.LIGHTBLACK_EX + "    5. Finalizar procesos innecesarios")
    print(Fore.LIGHTYELLOW_EX + "    6. Salir\n")

    # Detén la animación ANTES del input
    animar = False
    time.sleep(0.1)  # Da tiempo a que el hilo termine y limpie la línea

    opcion = input(Fore.WHITE + "Introduce el número de la opción que necesitas y después pulsa ENTER o INTRO: ")


    if opcion == "1":
        print(Fore.GREEN + "\nIniciando actualización de programas...")
        os.system("winget upgrade --all")
        print(Fore.GREEN + "\nActualización finalizada.\n")
    elif opcion == "2":
        print(Fore.GREEN + "\nIniciando limpieza de la papelera de reciclaje...")
        #os.system('PowerShell.exe Clear-RecycleBin -Force')
        os.system('PowerShell.exe Clear-RecycleBin -Force -Scope CurrentUser')
        print(Fore.GREEN + "\nPapelera de reciclaje vaciada.\n")
    elif opcion == "3":
        disco = input(Fore.WHITE + "Introduce el nombre del disco a inspeccionar (Ejemplo: C): ")
        print(Fore.GREEN + "\nIniciando comprobación de errores en el disco duro...")
        os.system(f"chkdsk {disco}: /F")
        print(Fore.GREEN + f"\nComprobación de errores en el disco duro {disco} finalizada.\n")
    elif opcion == "4":
        disco = input(Fore.WHITE + "Introduce el nombre del disco a desfragmentar (Ejemplo: C): ")
        print(Fore.GREEN + "\nIniciando desfragmentación del disco duro...")
        os.system(f"defrag {disco}: /O")
        print(Fore.GREEN + f"\nDesfragmentación del disco duro {disco} finalizada.\n")
    elif opcion == "5":
        proceso = input(Fore.WHITE + "Introduce el nombre del proceso a finalizar (ejemplo: notepad.exe): ")
        os.system(f"taskkill /IM {proceso} /F")
        print(Fore.GREEN + f"\nProceso {proceso} finalizado.\n")
    elif opcion == "6":
        print(Fore.YELLOW + "\nSaliendo del programa.")
        sys.exit()
    else:
        print(Fore.RED + "Opción no válida, recuerde que sólo debe introducir un número.\n")


