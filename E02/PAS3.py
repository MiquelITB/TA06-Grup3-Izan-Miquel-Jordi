import os

def contar_valores_archivos(ruta):
    total_valores_numericos = 0
    total_valores_letras = 0
    total_líneas_correctas = 0  # Comptador de línies correctes (31 valors numèrics)
    total_líneas_incorrectas = 0  # Comptador de línies incorrectes (no 31 valors numèrics)

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

                            # Filtrar valors numèrics i lletres
                            valors_numerics = 0
                            valors_letras = 0

                            for valor in valores_a_contar:
                                # Si el valor és un número (sense espais separadors)
                                if valor.replace('.', '', 1).isdigit():  # Comprovar si és numèric
                                    valors_numerics += 1
                                # Si el valor és lletres
                                elif valor.isalpha():  # Comprovar si és lletres
                                    valors_letras += 1

                            # Comptar els valors numèrics i les lletres
                            total_valores_numericos += valors_numerics
                            total_valores_letras += valors_letras

                            # Comprovar si hi ha exactament 31 valors numèrics
                            if valors_numerics == 31:
                                total_líneas_correctas += 1  # Línia correcta amb 31 valors numèrics
                            else:
                                total_líneas_incorrectas += 1  # Línia incorrecta (no té 31 valors numèrics)

                except (OSError, IOError) as e:
                    print(f"Error al processar l'arxiu {ruta_archivo}: {e}")

    # Calcular la suma de línies correctes i incorrectes
    total_líneas_totales = total_líneas_correctas + total_líneas_incorrectas

    # Imprimir resultats finals
    print(f"Total de línies correctes (31 valors numèrics): {total_líneas_correctas}")
    print(f"Total de línies incorrectes (no 31 valors numèrics): {total_líneas_incorrectas}")
    print(f"Total de línies (correctes + incorrectes): {total_líneas_totales}")
    print(f"Total de valors numèrics trobats (sense les dues primeres files i les tres primeres columnes): {total_valores_numericos}")
    print(f"Total de valors de lletres trobats (sense les dues primeres files i les tres primeres columnes): {total_valores_letras}")
    
    return total_valores_numericos, total_valores_letras, total_líneas_correctas, total_líneas_incorrectas, total_líneas_totales

# Ruta del directori on es troben els arxius
ruta_directorio = './E01'

# Cridar la funció per comptar els valors dels arxius
total_valores_numericos, total_valores_letras, total_líneas_correctas, total_líneas_incorrectas, total_líneas_totales = contar_valores_archivos(ruta_directorio)
