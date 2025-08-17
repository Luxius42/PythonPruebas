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
from colorama import init, Fore, Style

init(autoreset=True)  # Inicializa colorama

while True:
    print(Fore.CYAN + "#" * 40)
    print(Fore.YELLOW + "  **MANTENIMIENTO DEL SISTEMA** ")
    print(Fore.RED + "   NOTA.- Recuerda que debes ejecutar este script\n   como ADMINISTRADOR ya que ALGUNOS COMANDOS\n"
          "   requieren permisos elevados.")
    print(Fore.CYAN + "#" * 40 + "\n")
    print(Fore.GREEN + "    1. Comprobar y actualizar programas")
    print(Fore.LIGHTBLUE_EX + "    2. Limpiar papelera de reciclaje")
    print(Fore.LIGHTMAGENTA_EX + "    3. Comprobar errores en el disco duro")
    print(Fore.LIGHTRED_EX + "    4. Desfragmentar el disco duro")
    print(Fore.LIGHTBLACK_EX + "    5. Finalizar procesos innecesarios")
    print(Fore.LIGHTYELLOW_EX + "    6. Salir\n")
    opcion = input(Fore.WHITE + "Introduce el número de la opción que necesitas y después pulsa ENTER o INTRO: ")

    if opcion == "1":
        print(Fore.GREEN + "\nIniciando actualización de programas...")
        os.system("winget upgrade --all")
        print(Fore.GREEN + "\nActualización finalizada.\n")
    elif opcion == "2":
        print(Fore.GREEN + "\nIniciando limpieza de la papelera de reciclaje...")
        os.system("echo y | PowerShell.exe Clear-RecycleBin")
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