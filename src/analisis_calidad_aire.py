# Análisis inicial de la calidad del aire en Monterrey

# Datos simulados de concentración de contaminantes
pm25 = [18.2, 22.5, 15.8, 31.4, 27.6]
pm10 = [35.1, 42.7, 30.5, 58.3, 49.2]

# Cálculo de promedios
promedio_pm25 = sum(pm25) / len(pm25)
promedio_pm10 = sum(pm10) / len(pm10)


def clasificar_pm25(valor):
    """Clasifica de forma sencilla una concentración de PM2.5."""
    if valor <= 12:
        return "Buena"
    elif valor <= 35.4:
        return "Moderada"
    else:
        return "Elevada"


clasificacion = clasificar_pm25(promedio_pm25)

# Estadísticas básicas
min_pm25 = min(pm25)
max_pm25 = max(pm25)

min_pm10 = min(pm10)
max_pm10 = max(pm10)

print("Análisis inicial de calidad del aire")
print("------------------------------------")
print(f"Promedio de PM2.5: {promedio_pm25:.2f}")
print(f"Promedio de PM10: {promedio_pm10:.2f}")
print(f"Clasificación del PM2.5: {clasificacion}")

print()
print("Estadísticas de PM2.5")
print(f"Mínimo: {min_pm25:.2f}")
print(f"Máximo: {max_pm25:.2f}")

print()
print("Estadísticas de PM10")
print(f"Mínimo: {min_pm10:.2f}")
print(f"Máximo: {max_pm10:.2f}")

import matplotlib.pyplot as plt

# Gráfica de concentraciones de contaminantes
dias = [1, 2, 3, 4, 5]

plt.plot(dias, pm25, marker="o", label="PM2.5")
plt.plot(dias, pm10, marker="s", label="PM10")

plt.title("Concentración de contaminantes")
plt.xlabel("Día")
plt.ylabel("Concentración")
plt.legend()
plt.grid(True)

plt.savefig("results/contaminantes.png", dpi=300)
plt.show()