# Reto Semana 8 - MeteoSense Analytics

Programacion para Ciencia de Datos | IPN 2026

## Descripcion

Sistema de analisis de datos meteorologicos de la red de sensores de
**MeteoSense** en la Ciudad de Mexico, resuelto con **NumPy**. El reto
procesa una semana de mediciones (5 estaciones x 7 dias x 24 horas) de
temperatura, humedad y CO2, manejando valores faltantes (NaN) de sensores
desconectados. Implementado como notebook de Jupyter siguiendo el formato
pedido por el profesor.

## Temas aplicados

- Creacion e inspeccion de arrays NumPy (ndim, shape, size, dtype, nbytes)
- Indexacion y slicing sobre arrays 3D (estaciones, dias, horas)
- Operaciones vectorizadas y broadcasting (sin loops)
- Funciones estadisticas con manejo de NaN (`nanmean`, `nanstd`, `nanmax`...)
- Estadisticas a lo largo de ejes especificos (`axis=(...)`)
- Indexacion booleana para clasificacion y deteccion de anomalias

## Estructura de los datos

```
temperatura, humedad, co2  -> arrays 3D de shape (5, 7, 24)
   eje 0 -> 5 estaciones (Coyoacan, Azcapotzalco, Xochimilco, Tlalpan, Miguel Hidalgo)
   eje 1 -> 7 dias
   eje 2 -> 24 horas
```

## Estructura del proyecto

```
reto-semana-08/
|-- README.md
|-- .gitignore
|-- reto_08_metricas_sensores.ipynb   # Notebook con todas las celdas resueltas y ejecutadas
```

## Como ejecutar

```bash
# Abrir el notebook en Jupyter / VSCode / Colab y ejecutar todas las celdas
jupyter notebook reto_08_metricas_sensores.ipynb
```

O para ejecutarlo sin abrir la UI (requiere `nbconvert`):

```bash
pip install numpy nbconvert ipykernel
jupyter nbconvert --to notebook --execute --inplace reto_08_metricas_sensores.ipynb
```

## Contenido por partes

### Parte 1 - Exploracion de arrays
Inspeccion de propiedades del array, indexacion para extraer mediciones
puntuales y slicing para subconjuntos (tardes, estaciones pares, dias en
orden inverso).

### Parte 2 - Estadisticas basicas
Estadisticas globales con funciones `nan*` y agregaciones por eje:
temperatura por estacion (`axis=(1,2)`), humedad por hora (`axis=(0,1)`)
y CO2 maximo por dia (`axis=(0,2)`).

### Parte 3 - Operaciones vectorizadas
Conversiones Celsius -> Fahrenheit / Kelvin y normalizacion de humedad,
todo vectorizado. Indice de Confort Termico `ICT = T + 0.05 * H` con
clasificacion por categorias usando indexacion booleana.

### Parte 4 - Analisis avanzado
Deteccion de anomalias de CO2 con el criterio de +/- 2 desviaciones
estandar y analisis del dia de contingencia ambiental (dia 4), incluyendo
el incremento porcentual y la estacion mas afectada.

### Bonus - Reporte ejecutivo
Resumen con rankings de estaciones, patrones horarios y calidad de datos.

## Resultados

```
TEMPERATURA (global)
  Promedio: 21.59 C   Maxima: 32.91 C   Minima: 10.62 C   Desv: 4.28 C

INDICE DE CONFORT TERMICO (830 mediciones validas)
  Frio (<20):         12.4%
  Confortable (20-25): 42.5%
  Calido (25-30):      39.2%
  Muy caluroso (>=30):  5.9%

CALIDAD DEL AIRE (CO2)
  Media: 402.6 ppm    Anomalias (>2 sigma): 31
  Contingencia dia 4: +15.1% vs dias normales

RANKINGS
  Estacion mas calurosa: Azcapotzalco
  Estacion mas humeda:   Xochimilco
  Mejor calidad de aire: Tlalpan
  Hora mas calurosa: 11:00    Hora con mas CO2: 17:00

CALIDAD DE DATOS
  Valores faltantes: 13 (temperatura 7, humedad 3, CO2 3)
```

## Autor

Santiago Alexey Corona Cubeiro
Instituto Politecnico Nacional
