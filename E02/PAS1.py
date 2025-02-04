import os

def contar_errores_separacion(ruta):
    errores_separacion = 0
    errores_cabecera = 0
    errores_segunda_linea = 0

    # Cabecera esperada
    cabecera_esperada = "precip\tMIROC5\tRCP60\tREGRESION\tdecimas\t1"
    # Número de elementos esperados en la segunda línea
    elementos_esperados_segunda_linea = 8

    # Recorrer los archivos dentro del directorio y subdirectorios
    for directorio_raiz, _, archivos in os.walk(ruta):
        for archivo in archivos:
            if archivo.endswith('.dat'):  # Solo procesar archivos .dat
                ruta_archivo = os.path.join(directorio_raiz, archivo)

                try:
                    with open(ruta_archivo, 'r', encoding='utf-8') as archivo_actual:
                        # Leer todas las líneas del archivo
                        lineas = archivo_actual.readlines()

                        # Verificar que el archivo tiene suficiente contenido
                        if len(lineas) < 3:
                            print(f"Advertencia: El archivo {ruta_archivo} tiene menos de 3 líneas. No se puede procesar.")
                            continue

                        # Verificar la cabecera
                        cabecera_actual = lineas[0].strip()
                        if cabecera_actual != cabecera_esperada:
                            print(f"Advertencia: La cabecera del archivo {ruta_archivo} no coincide con la esperada.")
                            errores_cabecera += 1

                        # Verificar la segunda línea
                        segunda_linea_actual = lineas[1].strip()
                        elementos_segunda_linea = segunda_linea_actual.split('\t')

                        if len(elementos_segunda_linea) != elementos_esperados_segunda_linea:
                            print(f"Advertencia: La segunda línea del archivo {ruta_archivo} no tiene la cantidad de elementos esperada.")
                            errores_segunda_linea += 1
                        else:
                            if '  ' in segunda_linea_actual.replace('\t', ' '):
                                print(f"Advertencia: Hay más de un espacio consecutivo en la segunda línea del archivo {ruta_archivo}.")
                                errores_segunda_linea += 1

                        # Procesar cada línea restante
                        for linea in lineas[2:]:
                            linea = linea.strip()
                            if '  ' in linea:  # Si hay más de un espacio consecutivo
                                errores_separacion += linea.count('  ')  # Contar la cantidad de errores de separación

                except (OSError, IOError) as e:
                    print(f"Error al procesar el archivo {ruta_archivo}: {e}")

    return errores_separacion, errores_cabecera, errores_segunda_linea

# Ruta del directorio donde se encuentran los archivos
ruta_directorio = './E01'

# Llamar la función para contar los errores de separación, cabecera y segunda línea
errores_separacion, errores_cabecera, errores_segunda_linea = contar_errores_separacion(ruta_directorio)

# Imprimir los resultados
if errores_separacion == 0 and errores_cabecera == 0 and errores_segunda_linea == 0:
    print("No se han encontrado errores en las cabeceras, la segunda línea ni en las separaciones.")
else:
    print(f"Total de errores de separación: {errores_separacion}")
    print(f"Total de errores de cabecera: {errores_cabecera}")
    print(f"Total de errores en la segunda línea: {errores_segunda_linea}")