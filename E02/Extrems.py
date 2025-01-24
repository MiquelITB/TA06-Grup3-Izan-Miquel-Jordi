import os

def get_rainfall_data(ruta):
    rainfall_data = {}

    for directorio_raiz, _, archivos in os.walk(ruta):
        for archivo in archivos:
            if archivo.endswith('.dat'):
                ruta_archivo = os.path.join(directorio_raiz, archivo)

                try:
                    with open(ruta_archivo, 'r', encoding='utf-8') as archivo_actual:
                        lineas = archivo_actual.readlines()

                        for linea in lineas:
                            valores = linea.split()
                            
                            # Ignorar líneas de cabecera o metadatos
                            if len(valores) < 4 or not valores[1].isdigit():
                                continue

                            # Extraer año y valores de precipitación
                            year = valores[1]  # Segunda columna es el año
                            rainfall_values = valores[3:]  # Precipitación desde la 4ª columna

                            # Sumar los valores válidos
                            total_rainfall = sum(
                                float(valor) for valor in rainfall_values if valor.replace('.', '', 1).isdigit() and float(valor) != -999
                            )

                            if year in rainfall_data:
                                rainfall_data[year] += total_rainfall
                            else:
                                rainfall_data[year] = total_rainfall

                except (OSError, IOError) as e:
                    print(f"Error al procesar el archivo {ruta_archivo}: {e}")

    return rainfall_data

def find_extreme_years(rainfall_data):
    max_rainfall = max(rainfall_data.values())
    min_rainfall = min(rainfall_data.values())

    rainiest_years = [year for year, rainfall in rainfall_data.items() if rainfall == max_rainfall]
    driest_years = [year for year, rainfall in rainfall_data.items() if rainfall == min_rainfall]

    return rainiest_years, driest_years

# Ruta al directorio con los archivos .dat
ruta_directorio = './TA06-Grup3-Izan-Miquel-Jordi/E01'
rainfall_data = get_rainfall_data(ruta_directorio)
rainiest_years, driest_years = find_extreme_years(rainfall_data)

print(f": {rainiest_years}")
print(f"Driest years: {driest_years}")
print(f"Number of rainiest years: {len(rainiest_years)}")
print(f"Number of driest years: {len(driest_years)}")
