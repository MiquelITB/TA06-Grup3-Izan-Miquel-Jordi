import os

def contar_valores_archivos(ruta):
    total_valores = 0
    
    # Recorrer los archivos en el directorio y subdirectorios
    for directorio_raiz, directorios, archivos in os.walk(ruta):
        for archivo in archivos:
            # Solo procesar archivos con extensión .csv
            if archivo.endswith('.dat'):
                ruta_archivo = os.path.join(directorio_raiz, archivo)
                
                with open(ruta_archivo, 'r') as archivo_actual:
                    # Leer las líneas del archivo
                    lineas = archivo_actual.readlines()
                    
                    # Ignorar las dos primeras filas
                    lineas_a_contar = lineas[2:]  # Desde la tercera fila en adelante
                    
                    # Procesar cada línea
                    for linea in lineas_a_contar:
                        # Dividir la línea en valores por los espacios (o el delimitador adecuado)
                        valores = linea.split()  # Separar por espacios
                        
                        # Excluir el primer valor de la columna 1 (ya que se debe ignorar la primera columna)
                        valores_a_contar = valores[3:]  # Ignorar la primera columna
                        
                        # Sumar la cantidad de valores restantes
                        total_valores += len(valores_a_contar)

    return total_valores

# Ruta del directorio donde se encuentran los archivos
ruta_directorio = '/home/miguel.valencia.7e8/PycharmProjects/TA06-Grup3-Izan-Miquel-Jordi/TA06-Grup3-Izan-Miquel-Jordi/E01'

# Llamar a la función para contar los valores en los archivos
total_valores = contar_valores_archivos(ruta_directorio)

# Imprimir el resultado
print(f"El número total de valores en los archivos, excluyendo las dos primeras filas y la primera columna, es: {total_valores}")

