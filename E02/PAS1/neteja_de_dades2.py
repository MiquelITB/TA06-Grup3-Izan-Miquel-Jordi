import os

def contar_valores_archivos(ruta):
    total_valores = 0
    files_incorrectes = 0  # Comptador de files que no tenen exactament 31 valors numèrics

    # Recórrer els arxius dins del directori i subdirectoris
    for directorio_raiz, _, archivos in os.walk(ruta):
        for archivo in archivos:
            if archivo.endswith('.dat'):  # Només processar arxius .dat
                ruta_archivo = os.path.join(directorio_raiz, archivo)

                try:
                    with open(ruta_archivo, 'r', encoding='utf-8') as archivo_actual:
                        # Llegir totes les línies de l'arxiu
                        lineas = archivo_actual.readlines()

                        # Ignorar les dues primeres files
                        lineas_a_contar = lineas[2:]  # A partir de la tercera fila

                        # Processar cada línia restant
                        for linea in lineas_a_contar:
                            # Dividir la línia en valors utilitzant espais com a separador
                            valores = linea.split()

                            # Ignorar les tres primeres columnes
                            valores_a_contar = valores[3:]  # Només des de la quarta columna en endavant

                            # Filtrar només valors numèrics
                            valors_numerics = [
                                valor for valor in valores_a_contar if valor.replace('.', '', 1).isdigit()
                            ]

                            # Comptar els valors numèrics si hi ha exactament 31
                            if len(valors_numerics) == 31:
                                total_valores += len(valors_numerics)
                            else:
                                files_incorrectes += 1

                except (OSError, IOError) as e:
                    print(f"Error al processar l'arxiu {ruta_archivo}: {e}")

    print(f"Total de files amb un nombre incorrecte de valors numèrics (menys de 31): {files_incorrectes}")
    return total_valores

# Ruta del directori on es troben els arxius
ruta_directorio = '/home/miguel.valencia.7e8/PycharmProjects/TA06-Grup3-Izan-Miquel-Jordi/TA06-Grup3-Izan-Miquel-Jordi/E01'

# Cridar la funció per comptar els valors dels arxius
total_valores = contar_valores_archivos(ruta_directorio)

# Imprimir el resultat
print(f"El nombre total de valors numèrics en els arxius, excloent les dues primeres files i les tres primeres columnes, és: {total_valores}")
