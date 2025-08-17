import os

# Comando para actualizar todos los programas instalados con winget
# Asegúrate de tener permisos de administrador para ejecutar este comando   

# Si quieres ejecutar como .executable, puedes usar pyinstaller
# pip install pyinstaller
# python -m PyInstaller --onefile ActualizaPROGRAMAS.py

import os
import sys

print("#"* 40)
print("   Mantenimiento del sistema ")
print("#" * 40, "\n", "\n")
print("    1. Comprobar y actualizar programas" , "\n")
print("    2. Limpiar papelera de reciclaje", "\n")
print("    3. Comprobar errores en el disco duro", "\n")
print("    4. Desfragmentar el disco duro", "\n")
print("    5. Finalizar procesos innecesarios", "\n")
print("    6. Salir", "\n")
opcion = input("Introduce el número de la opción que necesitas, sólo el número: ")

if opcion == "1": # Actualizar programas
    print("\nIniciando actualización de programas...")
    # Ejecuta el comando para actualizar todos los programas instalados
    os.system("winget upgrade --all")
    print("\nActualización finalizada.")
elif opcion == "2": # Limpiar papelera de reciclaje
    print("\nIniciando limpieza de la papelera de reciclaje...")
    # Ejecuta el comando para limpiar la papelera de reciclaje
    # El comando 'echo y' es para confirmar la acción sin necesidad de intervención del usuario
    os.system("echo y | PowerShell.exe Clear-RecycleBin")
    print("\nPapelera de reciclaje vaciada.")
elif opcion == "3": # Comprobar errores en el disco duro
    # Solicita al usuario el nombre del disco a inspeccionar
    disco = input("Introduce el nombre del disco a inspeccionar (Ejemplo: C): ")
    print("\nIniciando comprobación de errores en el disco duro...")
    os.system(f"chkdsk {disco}: /F")
    print(f"\nComprobación de errores en el disco duro {disco} finalizada.")
elif opcion == "4": # Desfragmentar el disco duro
    # Solicita al usuario el nombre del disco a desfragmentar       
    disco = input("Introduce el nombre del disco a inspeccionar (Ejemplo: C): ")
    print("\nIniciando desfragmentación del disco duro...")
    os.system(f"defrag {disco}: /O")
    print(f"\nDesfragmentación del disco duro {disco} finalizada.")
elif opcion == "5": # Finalizar procesos innecesarios
    print("\nIniciando finalización de procesos innecesarios...")
    # Solicita al usuario el nombre del proceso a finalizar
    proceso = input("Introduce el nombre del proceso a finalizar (ejemplo: notepad.exe): ")
    os.system(f"taskkill /IM {proceso} /F")
    print(f"\nProceso {proceso} finalizado.")   
elif opcion == "6":
    print("\nSaliendo del programa.")
    sys.exit()
else:
    print("Opción no válida, recuerde que sólo debe introducir un número.")

#Tras ejecutar el comando, pyinstaller --onefile ActualizaPROGRAMAS.py
# se generará un archivo ejecutable en la carpeta dist.
# Puedes ejecutar el archivo ejecutable generado para actualizar todos los programas instalados.

