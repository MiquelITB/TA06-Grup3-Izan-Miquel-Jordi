import os
carpeta = '/home/miguel.valencia.7e8/PycharmProjects/TA06-Grup3-Izan-Miquel-Jordi/TA06-Grup3-Izan-Miquel-Jordi/E01'

# Obtener la lista de archivos en la carpeta
lista_archivos = os.listdir(carpeta)

# Variable para almacenar la primera línea del primer archivo
primera_linea = None

# Iterar sobre cada archivo
for nombre_archivo in lista_archivos:
    ruta_archivo = os.path.join(carpeta, nombre_archivo)
    
    # Leer el contenido del archivo
    with open(ruta_archivo, 'r') as archivo:
        contenido = archivo.read()
        
    # Obtener la primera línea del archivo
    lineas = contenido.split('\n')
    primera_linea_archivo = lineas[0]
    
    # Si es el primer archivo, almacenar la primera línea
    if primera_linea is None:
        primera_linea = primera_linea_archivo
    # Si la primera línea no coincide, imprimir mensaje y salir del bucle
    elif primera_linea != primera_linea_archivo:
        print('La primera línea de los archivos no es la misma.')
        break
else:
    # Si se completa el bucle sin encontrar diferencias, imprimir mensaje
    print('La primera línea de todos los archivos es la misma.')
#    print(f'Contenido: {contenido}')
    




