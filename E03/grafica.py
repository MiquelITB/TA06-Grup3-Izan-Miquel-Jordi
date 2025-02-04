import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Leer el archivo CSV
archivo_csv = "resultado_estadistica.csv"
df = pd.read_csv(archivo_csv)

# 2. Inspeccionar los datos
print(df.head())

# 3. Gráfico de barras para el Total por Año
plt.figure(figsize=(10, 6))
sns.barplot(data=df, x='Año', y='Total', palette='Blues_d')
plt.title('Total por Año')
plt.ylabel('Total (mm)')
plt.xlabel('Año')
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()
plt.savefig('grafica.png')  # Guarda la gráfica como una imagen

# 4. Gráfico de líneas para la Media por Año
plt.figure(figsize=(10, 6))
sns.lineplot(data=df, x='Año', y='Media', marker='o', color='orange')
plt.title('Media Anual por Año')
plt.ylabel('Media (litros/m²)')
plt.xlabel('Año')
plt.grid(axis='both', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()
plt.savefig('grafica2.png')  # Guarda la gráfica como una imagen


# 5. Gráfico de barras para la Variación porcentual
plt.figure(figsize=(10, 6))
sns.barplot(data=df, x='Año', y='Variación (%)', palette='coolwarm')
plt.title('Variación Porcentual por Año')
plt.ylabel('Variación (%)')
plt.xlabel('Año')
plt.axhline(0, color='gray', linestyle='--', alpha=0.7)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
plt.savefig('grafica3.png')  # Guarda la gráfica como una imagen
