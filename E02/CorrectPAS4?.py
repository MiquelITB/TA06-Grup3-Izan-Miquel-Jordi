import os
import pandas as pd

def calcular_totales_y_medias_por_anio(ruta_directorio):
    # Diccionario para almacenar totales, medias y estadísticas por año
    resultados = {}
    contador_archivos = 0  # Contador de archivos .dat

    # Recorrer archivos en el directorio y subdirectorios
    for directorio_raiz, _, archivos in os.walk(ruta_directorio):
        for archivo in archivos:
            # Solo procesar archivos con extensión .dat
            if archivo.endswith('.dat'):
                contador_archivos += 1  # Incrementar el contador de estaciones meteorológicas
                ruta_archivo = os.path.join(directorio_raiz, archivo)

                # Leer archivo como texto y dividir en líneas
                with open(ruta_archivo, 'r') as f:
                    lineas = f.readlines()

                # Ignorar las dos primeras filas y procesar las demás
                datos = lineas[2:]

                for linea in datos:
                    # Dividir la línea en columnas
                    columnas = linea.strip().split()

                    # Verificar que hay suficientes columnas
                    if len(columnas) < 3:
                        continue

                    # La primera columna se ignora, la segunda es el año, la tercera es el mes
                    _, anio, mes, *valores = columnas

                    # Convertir año y mes a entero
                    try:
                        anio = int(anio)
                        mes = int(mes)
                    except ValueError:
                        continue

                    # Convertir valores a enteros, ignorar no numéricos o -999
                    valores_validos = []
                    for valor in valores[:31]:  # Solo considerar hasta 31 días
                        try:
                            valor = int(valor)
                            if valor != -999:  # Ignorar valores -999
                                valores_validos.append(valor)
                        except ValueError:
                            continue

                    # Calcular suma mensual y contar días útiles
                    dias_utiles = len(valores_validos)  # Días válidos (útiles)
                    if dias_utiles > 0:
                        total_mes = sum(valores_validos) / 10  # Convertir de décimas de milímetro a milímetros
                    else:
                        total_mes = 0

                    # Agregar resultados al diccionario por año
                    if anio in resultados:
                        resultados[anio]['total'] += total_mes
                        resultados[anio]['dias_utiles'] += dias_utiles
                        resultados[anio]['max_prec'] = max(resultados[anio]['max_prec'], total_mes)
                        resultados[anio]['min_prec'] = min(resultados[anio]['min_prec'], total_mes) if total_mes > 0 else resultados[anio]['min_prec']
                    else:
                        resultados[anio] = {
                            'total': total_mes,
                            'dias_utiles': dias_utiles,  # Nuevo: Contador de días útiles
                            'max_prec': total_mes,
                            'min_prec': total_mes if total_mes > 0 else float('inf')
                        }

    # Calcular estadísticas finales
    tabla_resultados = []
    for anio, valores in resultados.items():
        total = valores['total']
        dias_utiles = valores['dias_utiles']
        # Media basada en los días útiles en vez de 31 días por mes
        media = total / dias_utiles if dias_utiles > 0 else 0
        max_prec = valores['max_prec']
        min_prec = valores['min_prec'] if valores['min_prec'] != float('inf') else 0  # Si no hay datos válidos, min_prec = 0
        tabla_resultados.append([anio, total, media, max_prec, min_prec, dias_utiles])

    # Crear un DataFrame y ordenar por año
    df_resultados = pd.DataFrame(tabla_resultados, columns=['Año', 'Total', 'Media', 'Máxima Mensual', 'Mínima Mensual', 'Días Útiles'])
    df_resultados.sort_values(by='Año', inplace=True)

    # Calcular la columna de variación porcentual
    df_resultados['Variación (%)'] = df_resultados['Total'].pct_change() * 100

    # Convertir la columna "Media" de milímetros a litros por metro cuadrado
    df_resultados['Media'] = df_resultados['Media'] * 10  # Convertir de milímetros a litros por metro cuadrado

    return df_resultados


# Ruta del directorio donde se encuentran los archivos
ruta_directorio = './E01'

# Calcular resultados desde el directorio
resultados = calcular_totales_y_medias_por_anio(ruta_directorio)

# Mostrar la tabla de resultados
print(resultados)