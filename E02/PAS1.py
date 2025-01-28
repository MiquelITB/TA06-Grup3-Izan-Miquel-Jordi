import os

def contar_errores_separacion(ruta):
    errores_separacion = 0

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
                            # Eliminar espais en blanc inicial i final
                            linea = linea.strip()

                            # Verificar que la separació entre els valors sigui exactament 1 espai
                            # Si trobem més d'un espai consecutiu, comptem l'error
                            if '  ' in linea:  # Si hi ha més d'un espai consecutiu
                                errores_separacion += linea.count('  ')  # Comptar la quantitat d'errors de separació

                except (OSError, IOError) as e:
                    print(f"Error al processar l'arxiu {ruta_archivo}: {e}")

    return errores_separacion

# Ruta del directori on es troben els arxius
ruta_directorio = './E01'

# Cridar la funció per comptar els errors de separació
errores = contar_errores_separacion(ruta_directorio)

# Imprimir el resultat
print(f"El nombre total d'errors de separació (més d'un espai consecutiu) en els arxius és: {errores}")
