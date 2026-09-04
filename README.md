# Análisis de la calidad del aire en el Área Metropolitana de Monterrey

## Descripción

Este proyecto tiene como objetivo realizar un análisis inicial de concentraciones de contaminantes atmosféricos, utilizando datos simulados de PM2.5 y PM10.

El programa calcula promedios, valores mínimos y máximos, clasifica la concentración promedio de PM2.5 y genera una gráfica para visualizar las concentraciones de ambos contaminantes.

## Objetivo

Analizar las concentraciones de PM2.5 y PM10 y observar su comportamiento a través de los días considerados en el conjunto de datos utilizado.

## Contaminantes de interés

* PM2.5
* PM10
* O3
* NO2
* SO2
* CO

En la versión actual del programa se realizan cálculos y visualizaciones para PM2.5 y PM10.

## Herramientas

* Python
* Matplotlib
* Git
* GitHub
* LaTeX

## Requisitos

Para ejecutar el proyecto se necesita:

* Python 3.
* La biblioteca `matplotlib`.
* Git, en caso de clonar el repositorio mediante la terminal.

## Instalación

Después de clonar el repositorio, instala `matplotlib` con:

```bash
python -m pip install matplotlib
```

Si el comando anterior no funciona debido a la configuración de Python, puede utilizarse:

```bash
python3 -m pip install matplotlib
```

## Cómo reproducir el proyecto

### 1. Clonar el repositorio

Clona el repositorio desde GitHub:

```bash
git clone https://github.com/clarissacontreras/calidad-aire-monterrey.git
```

### 2. Entrar a la carpeta del proyecto

```bash
cd calidad-aire-monterrey
```

### 3. Instalar la dependencia

```bash
python -m pip install matplotlib
```

### 4. Ejecutar el programa

Desde la carpeta principal del proyecto, ejecuta:

```bash
python src/analisis_calidad_aire.py
```

### 5. Revisar los resultados

El programa muestra en la terminal:

* Promedio de PM2.5.
* Promedio de PM10.
* Clasificación del PM2.5.
* Valor mínimo y máximo de PM2.5.
* Valor mínimo y máximo de PM10.

Además, genera una gráfica de las concentraciones de PM2.5 y PM10 y la guarda en:

```text
results/contaminantes.png
```

## Resultados esperados

Con los datos actualmente incluidos en `src/analisis_calidad_aire.py`, la ejecución produce los siguientes resultados:

```text
Promedio de PM2.5: 23.10
Promedio de PM10: 43.16
Clasificación del PM2.5: Moderada

Estadísticas de PM2.5
Mínimo: 15.80
Máximo: 31.40

Estadísticas de PM10
Mínimo: 30.50
Máximo: 58.30
```

También se genera la visualización:

```text
results/contaminantes.png
```

## Estructura del proyecto

```text
calidad-aire-monterrey/
├── .gitignore
├── README.md
├── data/
├── docs/
│   └── reporte.tex
├── results/
│   └── contaminantes.png
└── src/
    └── analisis_calidad_aire.py
```

### `src/`

Contiene el código fuente en Python utilizado para realizar los cálculos, clasificación y visualización de los contaminantes.

### `data/`

Está destinada a almacenar los conjuntos de datos utilizados por el proyecto. En la versión actual, los datos utilizados para el análisis están definidos directamente dentro del programa y la carpeta se encuentra disponible para futuras incorporaciones de datos.

Los archivos de datos como `.csv` y `.parquet` están excluidos del control de versiones mediante `.gitignore`.

### `docs/`

Contiene la documentación del proyecto, incluyendo el reporte elaborado en LaTeX.

### `results/`

Contiene las gráficas y resultados generados por los programas del proyecto.

### `.gitignore`

Contiene las reglas utilizadas para evitar que archivos temporales, archivos auxiliares y determinados archivos de datos sean incorporados al control de versiones.

## Reflexión sobre Git

Este proyecto utiliza Git para registrar de manera organizada los cambios realizados durante su desarrollo. El historial de commits permite identificar las diferentes etapas de construcción y modificación del proyecto.

## Verificación de reproducibilidad

Las instrucciones de reproducción de este README fueron verificadas mediante la ejecución del programa desde la carpeta principal del proyecto.

El comando:

```bash
python src/analisis_calidad_aire.py
```

se ejecutó correctamente y produjo los resultados numéricos esperados y la gráfica `results/contaminantes.png`.

## Licencia

Este proyecto utiliza la licencia MIT porque permite que otras personas consulten, utilicen, modifiquen y distribuyan el código con pocas restricciones, manteniendo el aviso de licencia correspondiente. Esta licencia es adecuada para un proyecto académico que busca facilitar la consulta y reutilización del trabajo.

## Cómo citar

Si utilizas este proyecto, puedes consultar la información de citación en el archivo [CITATION.cff](CITATION.cff) o mediante la opción "Cite this repository" disponible en GitHub.

## Verificación automática

Este repositorio utiliza GitHub Actions para verificar automáticamente la compilación de la documentación del proyecto.

El workflow compila el archivo LaTeX `docs/reporte.tex` y verifica que se genere correctamente el documento PDF `docs/reporte.pdf`.

De esta manera, se comprueba automáticamente que la documentación pueda compilarse correctamente.
