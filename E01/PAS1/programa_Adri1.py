import os

def contar_valores_archivos(ruta):
    total_valores = 0
    for directorio_raiz, directorios, archivos in os.walk(ruta):
        for archivo in archivos:
            ruta_archivo = os.path.join(directorio_raiz, archivo)
            with open(ruta_archivo, 'r') as archivo_actual:
                contenido = archivo_actual.read()
                valores = contenido.split()  # Suponiendo que los valores están separados por espacios
                total_valores += len(valores)

    return total_valores

ruta_directorio = '/home/miguel.valencia.7e8/PycharmProjects/TA06-Grup3-Izan-Miquel-Jordi/TA06-Grup3-Izan-Miquel-Jordi/E01'  # Reemplaza esto con la ruta de tu directorio de archivos
total_valores = contar_valores_archivos(ruta_directorio)
print(f"El número total de valores en los 16 mil archivos es: {total_valores}")