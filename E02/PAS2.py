import os
import csv

def detectar_delimitador_y_columnas(archivo):
    """
    Detecta el delimitador y el número de columnas en un archivo CSV.
    Se analiza la primera línea del archivo para intentar identificar el delimitador.
    """
    posibles_delimitadores = [',', ';', '\t', '|']
    delimitador_detectado = None
    num_columnas = None

    with open(archivo, 'r', newline='', encoding='utf-8') as f:
        # Leer solo la primera línea para obtener una muestra
        primera_linea = f.readline()

        # Probar con diferentes delimitadores
        for delimitador in posibles_delimitadores:
            # Leer con el delimitador propuesto
            f.seek(0)  # Reiniciar el puntero al principio del archivo
            lector = csv.reader(f, delimiter=delimitador)
            primera_fila = next(lector)  # Obtener la primera fila

            if len(primera_fila) > 1:  # Verifica si parece ser un archivo con más de una columna
                delimitador_detectado = delimitador
                num_columnas = len(primera_fila)
                break
    
    return delimitador_detectado, num_columnas

def verificar_mismo_formato(directorio):
    """
    Verifica que todos los archivos en un directorio tengan la misma extensión.
    """
    archivos = [f for f in os.listdir(directorio) if os.path.isfile(os.path.join(directorio, f))]
    
    if not archivos:
        print("El directorio está vacío.")
        return None
    
    # Obtener la extensión del primer archivo
    extension_esperada = os.path.splitext(archivos[0])[1]
    
    # Verificar que todos los archivos tengan la misma extensión
    for archivo in archivos:
        extension_actual = os.path.splitext(archivo)[1]
        if extension_actual != extension_esperada:
            print(f"El archivo '{archivo}' no tiene el mismo formato ({extension_actual} en lugar de {extension_esperada}).")
            return None
    
    return extension_esperada

def validar_archivos(directorio):
    """
    Valida los archivos en un directorio: primero detecta el delimitador y número de columnas,
    luego verifica el formato (misma extensión), y muestra la salida en consola.
    """
    archivos = [f for f in os.listdir(directorio) if os.path.isfile(os.path.join(directorio, f))]
    
    # Imprimir los detalles de cada archivo
    print("\nDetalles de los archivos:")
    resultados = []  # Lista para almacenar los resultados

    for archivo in archivos:
        ruta_archivo = os.path.join(directorio, archivo)
        
        # Detectar delimitador y columnas
        delimitador, columnas = detectar_delimitador_y_columnas(ruta_archivo)
        
        if delimitador and columnas:
            resultados.append(f"'{archivo}': {columnas} columnas, delimitador '{delimitador}'")
        else:
            resultados.append(f"'{archivo}': No se pudo determinar el formato.")
    
    # Imprimir los resultados en bloques de 10
    for i in range(0, len(resultados), 10):
        print("\n".join(resultados[i:i+10]))  # Imprime en bloques de 10
    
    # Verificar que todos los archivos tengan el mismo formato (misma extensión)
    extension = verificar_mismo_formato(directorio)
    if extension is None:
        return
    
    # Imprimir la validación de formato
    print(f"\nTodos los archivos tienen el mismo formato ({extension}).")

# Cambia 'ruta/del/directorio' por el directorio que deseas verificar
directorio = '/home/miguel.valencia.7e8/PycharmProjects/TA06-Grup3-Izan-Miquel-Jordi/TA06-Grup3-Izan-Miquel-Jordi/E01'
validar_archivos(directorio)