import os
import sys

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

"""

# python -m PyInstaller --onefile mantenimientoSistema.py

while True:
    print("#" * 40)
    print("   Mantenimiento del sistema ")
    print("   NOTA.- Recuerda que debes ejecutar este script\n   como administrador ya que\n"
          "   ALGUNOS COMANDOS requieren permisos elevados.")
    print("#" * 40, "\n")
    print("    1. Comprobar y actualizar programas")
    print("    2. Limpiar papelera de reciclaje")
    print("    3. Comprobar errores en el disco duro")
    print("    4. Desfragmentar el disco duro")
    print("    5. Finalizar procesos innecesarios")
    print("    6. Salir\n")
    opcion = input("Introduce el número de la opción que necesitas y después pulsa ENTER o INTRO: ")

    if opcion == "1":
        print("\nIniciando actualización de programas...")
        os.system("winget upgrade --all")
        print("\nActualización finalizada.\n")
    elif opcion == "2":
        print("\nIniciando limpieza de la papelera de reciclaje...")
        os.system("echo y | PowerShell.exe Clear-RecycleBin")
        #os.system('PowerShell.exe Clear-RecycleBin -Force')
        print("\nPapelera de reciclaje vaciada.\n")
    elif opcion == "3":
        disco = input("Introduce el nombre del disco a inspeccionar (Ejemplo: C): ")
        print("\nIniciando comprobación de errores en el disco duro...")
        os.system(f"chkdsk {disco}: /F")
        print(f"\nComprobación de errores en el disco duro {disco} finalizada.\n")
    elif opcion == "4":
        disco = input("Introduce el nombre del disco a desfragmentar (Ejemplo: C): ")
        print("\nIniciando desfragmentación del disco duro...")
        os.system(f"defrag {disco}: /O")
        print(f"\nDesfragmentación del disco duro {disco} finalizada.\n")
    elif opcion == "5":
        proceso = input("Introduce el nombre del proceso a finalizar (ejemplo: notepad.exe): ")
        os.system(f"taskkill /IM {proceso} /F")
        print(f"\nProceso {proceso} finalizado.\n")
    elif opcion == "6":
        print("\nSaliendo del programa.")
        sys.exit()
    else:
        print("Opción no válida, recuerde que sólo debe introducir un número.\n")