import os

def contar_valores_archivos(ruta):
    total_valores = 0
    total_valores_faltantes = 0  # Para contar los valores que son -999
   
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
                       
                        # Excluir las tres primeras columnas
                        valores_a_contar = valores[3:]  # Ignorar las tres primeras columnas
                       
                        # Contabilizar los valores y los que son -999
                        for valor in valores_a_contar:
                            total_valores += 1
                            if valor == '-999':  # Verificar si el valor es -999
                                total_valores_faltantes += 1

    return total_valores, total_valores_faltantes

# Ruta del directorio donde se encuentran los archivos
ruta_directorio = '/home/miguel.valencia.7e8/PycharmProjects/TA06-Grup3-Izan-Miquel-Jordi/TA06-Grup3-Izan-Miquel-Jordi/E01'


# Llamar a la función para contar los valores y los valores -999
total_valores, total_valores_faltantes = contar_valores_archivos(ruta_directorio)

# Calcular el porcentaje de datos faltantes (-999)
if total_valores > 0:
    porcentaje_faltantes = (total_valores_faltantes / total_valores) * 100
else:
    porcentaje_faltantes = 0  # Si no hay valores totales, el porcentaje es 0

# Imprimir el resultado
print(f"El número total de valores en los archivos, excluyendo las dos primeras filas y las tres primeras columnas, es: {total_valores}")
print(f"El número total de valores faltantes (-999) es: {total_valores_faltantes}")
print(f"El porcentaje de datos faltantes (-999) es: {porcentaje_faltantes:.2f}%")
