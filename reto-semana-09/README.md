# Reto Semana 9 - SecureBank Fraud Detection

Programacion para Ciencia de Datos | IPN 2026

## Descripcion

Sistema basico de deteccion de transacciones anomalas (posible fraude)
para el banco digital **SecureBank**, resuelto con **NumPy**. Se analizan
2,500 transacciones (500 por cada una de 5 categorias de comercio) y se
detectan outliers con dos metodos estadisticos: **IQR** y **Z-Score**.
Implementado como notebook de Jupyter siguiendo el formato pedido por el
profesor.

## Temas aplicados

- Estadisticas descriptivas (media, mediana, desviacion, min, max)
- Percentiles y cuartiles (`np.percentile`), rango intercuartilico (IQR)
- Deteccion de outliers con metodo IQR (Q1 - 1.5*IQR, Q3 + 1.5*IQR)
- Deteccion de outliers con Z-Score (`|z| > 3`)
- Indexacion booleana y operaciones por categoria
- Matriz de correlacion (`np.corrcoef`)

## Categorias analizadas

```
Indice  Categoria          Monto tipico
  0     Supermercados      $200 - $2,000
  1     Restaurantes       $100 - $800
  2     Gasolineras        $300 - $1,500
  3     Tiendas_Online     $150 - $5,000
  4     Entretenimiento    $50 - $500
```

Cada categoria contiene 500 transacciones con un 3-5% de anomalias
inyectadas (montos muy altos o muy bajos).

## Estructura del proyecto

```
reto-semana-09/
|-- README.md
|-- .gitignore
|-- reto_09_detector_anomalias.ipynb   # Notebook con todas las celdas resueltas y ejecutadas
```

## Como ejecutar

```bash
# Abrir el notebook en Jupyter / VSCode / Colab y ejecutar todas las celdas
jupyter notebook reto_09_detector_anomalias.ipynb
```

O para ejecutarlo sin abrir la UI (requiere `nbconvert`):

```bash
pip install numpy nbconvert ipykernel
jupyter nbconvert --to notebook --execute --inplace reto_09_detector_anomalias.ipynb
```

## Contenido por partes

### Parte 1 - Analisis estadistico por categoria
Estadisticas descriptivas, cuartiles (Q1, Q2, Q3), IQR y los limites
inferior/superior para deteccion de outliers de cada categoria.

### Parte 2 - Deteccion de outliers con IQR
Mascara booleana por categoria para marcar montos fuera de
`[Q1 - 1.5*IQR, Q3 + 1.5*IQR]`, separando outliers inferiores y
superiores, y resumen de los mas extremos.

### Parte 3 - Deteccion de outliers con Z-Score
Z-Score por transaccion `z = (x - media) / std` (media ~0 y std ~1 por
categoria) y deteccion con umbral `|z| > 3`.

### Parte 4 - Comparacion y reporte final
Comparacion de ambos metodos (totales, diferencias y coincidencias) y
reporte de transacciones sospechosas, priorizando las detectadas por los
dos metodos.

### Bonus - Correlacion entre categorias
Matriz de correlacion `np.corrcoef` y el par de categorias con la
correlacion mas fuerte.

## Resultados

```
DETECCION DE OUTLIERS (2,500 transacciones)
  Metodo IQR     : 71 outliers  (2.6% - 3.2% por categoria)
  Metodo Z-Score : 55 outliers

  Por categoria        IQR   Z-Score
  Supermercados         15      12
  Restaurantes          16      11
  Gasolineras           13      10
  Tiendas_Online        14      13
  Entretenimiento       13       9

REPORTE EJECUTIVO
  Transacciones sospechosas (union): 71 (2.8%)
  Alta prioridad (ambos metodos):    55

CORRELACION
  Las categorias son practicamente independientes.
  Correlacion mas fuerte: Restaurantes <-> Gasolineras (-0.10)
```

> Nota: todos los Z-Scores detectados (55) caen tambien dentro de los
> outliers de IQR, por eso la union es 71 y la interseccion (alta
> prioridad) es 55. IQR resulta mas sensible que el umbral `|z| > 3`.

## Autor

Santiago Alexey Corona Cubeiro
Instituto Politecnico Nacional
