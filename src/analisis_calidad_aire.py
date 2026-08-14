# Análisis inicial de la calidad del aire en Monterrey

# Datos simulados de concentración de contaminantes
pm25 = [18.2, 22.5, 15.8, 31.4, 27.6]
pm10 = [35.1, 42.7, 30.5, 58.3, 49.2]

# Cálculo de promedios
promedio_pm25 = sum(pm25) / len(pm25)
promedio_pm10 = sum(pm10) / len(pm10)

print("Análisis inicial de calidad del aire")
print("------------------------------------")
print(f"Promedio de PM2.5: {promedio_pm25:.2f}")
print(f"Promedio de PM10: {promedio_pm10:.2f}")