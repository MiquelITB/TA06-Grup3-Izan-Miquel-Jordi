import subprocess

# Ruta de los programas
ruta_programas = './E02'

# Comandos para ejecutar cada uno de los programas (ajustando los nombres según corresponda)
comandos = [
    ['python', f'{ruta_programas}/PAS1.py'],
    ['python', f'{ruta_programas}/PAS2.py'],
    ['python', f'{ruta_programas}/PAS3.py'],
    ['python', f'{ruta_programas}/PAS4.py']
]

# Ejecutar los programas en secuencia
for comando in comandos:
    try:
        subprocess.run(comando, check=True)
        print(f'{comando[1]} ejecutado con éxito')
    except subprocess.CalledProcessError as e:
        print(f'Error al ejecutar {comando[1]}: {e}')