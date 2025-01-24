import os
import pandas as pd

def calcular_totales_y_medias_por_anio(ruta_directorio):
    # Diccionario para almacenar totales y medias por año
    resultados = {}

    # Recorrer archivos en el directorio y subdirectorios
    for directorio_raiz, _, archivos in os.walk(ruta_directorio):
        for archivo in archivos:
            # Solo procesar archivos con extensión .dat
            if archivo.endswith('.dat'):
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

                    # Convertir año a entero
                    try:
                        anio = int(anio)
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

                    # Calcular suma si hay datos válidos
                    if valores_validos:
                        total = sum(valores_validos)
                    else:
                        total = 0

                    # Agregar resultados al diccionario por año
                    if anio in resultados:
                        resultados[anio]['total'] += total
                        resultados[anio]['count'] += len(valores_validos)
                    else:
                        resultados[anio] = {'total': total, 'count': len(valores_validos)}

    # Calcular medias finales
    tabla_resultados = []
    for anio, valores in resultados.items():
        total = valores['total']
        count = valores['count']
        media = total / count if count > 0 else 0
        tabla_resultados.append([anio, total, media])

    # Crear un DataFrame y ordenar por año
    df_resultados = pd.DataFrame(tabla_resultados, columns=['Año', 'Total', 'Media'])
    df_resultados.sort_values(by='Año', inplace=True)

    # Calcular la columna de variación porcentual
    df_resultados['Variación (%)'] = df_resultados['Total'].pct_change() * 100

    # Ordenar por Total de mayor a menor y menor a mayor
    df_altos = df_resultados.sort_values(by='Total', ascending=False).head(5)  # 5 años con más total
    df_bajos = df_resultados.sort_values(by='Total', ascending=True).head(5)  # 5 años con menos total

    # Extraer solo los años con más y menos total
    años_con_mas_total = df_altos['Año'].values
    años_con_menos_total = df_bajos['Año'].values

    # Añadir esas columnas al DataFrame original
    df_resultados['Años con más precipitaciones'] = pd.Series(list(años_con_mas_total) + [None] * (len(df_resultados) - len(años_con_mas_total)))
    df_resultados['Años con menos precipitaciones'] = pd.Series(list(años_con_menos_total) + [None] * (len(df_resultados) - len(años_con_menos_total)))

    return df_resultados


# Ruta del directorio donde se encuentran los archivos
ruta_directorio = './TA06-Grup3-Izan-Miquel-Jordi/E01'

# Calcular resultados desde el directorio
resultados = calcular_totales_y_medias_por_anio(ruta_directorio)

# Mostrar la tabla de resultados
print(resultados)

