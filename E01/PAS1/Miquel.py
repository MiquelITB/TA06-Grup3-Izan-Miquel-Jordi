import os
carpeta = '../TA06-Grup3-Izan-Miquel-Jordi/E01'
print(carpeta)

# Obtener la lista de archivos en la carpeta
lista_archivos = os.listdir(carpeta)

# Variable para almacenar la primera línea de todos los archivos
primera_linea = None

# Revisión de la primera línea de cada archivo
for archivo in lista_archivos:
    ruta_archivo = os.path.join(carpeta, archivo)
    if os.path.isfile(ruta_archivo):
        with open(ruta_archivo, 'r') as file:
            primera_linea_archivo = file.readline()
            if primera_linea is None:
                primera_linea = primera_linea_archivo
            else:
                if primera_linea != primera_linea_archivo:
                    # Imprime los archivos que no coinciden con la primera línea
                    print(f"ERROR: El archivo {archivo} en la ruta {ruta_archivo} no coincide con la primera línea del archivo.") 
                    primera_linea = None
                    break
    else:
        # Imprime los archivos que son directorios
        print(f"ERROR: Se encontró un directorio en la ruta {ruta_archivo}.")




