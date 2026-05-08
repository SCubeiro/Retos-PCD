# Reto Semana 4 - Sistema de Inventario Modular

Programacion para Ciencia de Datos | IPN 2026

## Descripcion

Sistema modular que lee un archivo de inventario en CSV, identifica los
productos cuyo stock cayo por debajo del stock minimo y genera un reporte
de reorden ordenado por la cantidad de unidades faltantes.

Las filas con datos invalidos (precio no numerico, stock no entero,
columnas faltantes o de mas, etc.) se ignoran silenciosamente con una
advertencia y el resto del proceso continua.

## Estructura del Proyecto

```
reto-semana-04/
|
|-- main.py                     # Punto de entrada
|-- README.md
|-- .gitignore
|
|-- models/
|   |-- __init__.py
|   |-- producto.py             # Clase Producto
|
|-- utils/
|   |-- __init__.py
|   |-- io.py                   # leer_inventario, escribir_reporte
|   |-- validators.py           # validar_sku, validar_precio, validar_stock
|
|-- data/
|   |-- inventario.csv                  # Datos del ejemplo del enunciado
|   |-- inventario_con_errores.csv      # Caso con filas invalidas
|
|-- outputs/
    |-- reporte_inventario.csv          # Reporte generado
```

## Como ejecutar

```bash
python3 main.py
```

Por default lee `data/inventario.csv` y escribe en
`outputs/reporte_inventario.csv`. Las rutas estan en las constantes
`ARCHIVO_INVENTARIO` y `ARCHIVO_REPORTE` al inicio de `main.py`.

## Formato de entrada

`data/inventario.csv`:

| Columna       | Tipo    | Descripcion                       |
|---------------|---------|-----------------------------------|
| sku           | texto   | Identificador unico del producto  |
| nombre        | texto   | Nombre del producto               |
| categoria     | texto   | Categoria                         |
| precio        | decimal | Precio unitario (>= 0)            |
| stock         | entero  | Cantidad actual (>= 0)            |
| stock_minimo  | entero  | Nivel minimo antes de reordenar   |

## Formato de salida

`outputs/reporte_inventario.csv` contiene **solo** los productos cuyo
`stock < stock_minimo`, ordenados por `unidades_faltantes` descendente:

| Columna             | Calculo                          |
|---------------------|----------------------------------|
| sku                 | -                                |
| nombre              | -                                |
| categoria           | -                                |
| stock_actual        | stock                            |
| stock_minimo        | -                                |
| unidades_faltantes  | stock_minimo - stock             |
| valor_inventario    | precio * stock (2 decimales)     |

## Ejemplo

Entrada (`data/inventario.csv`):

```csv
sku,nombre,categoria,precio,stock,stock_minimo
SKU001,Laptop HP,Electronica,15000.00,5,10
SKU002,Mouse Logitech,Accesorios,350.00,3,15
SKU003,Teclado Mecanico,Accesorios,800.00,20,10
SKU007,SSD 1TB,Almacenamiento,1800.00,0,5
```

Salida (`outputs/reporte_inventario.csv`):

```csv
sku,nombre,categoria,stock_actual,stock_minimo,unidades_faltantes,valor_inventario
SKU002,Mouse Logitech,Accesorios,3,15,12,1050.00
SKU001,Laptop HP,Electronica,5,10,5,75000.00
SKU007,SSD 1TB,Almacenamiento,0,5,5,0.00
```

SKU003 no aparece porque tiene stock 20 >= minimo 10.

## Manejo de errores

El programa ignora silenciosamente las siguientes situaciones:
- Precio no numerico (`N/A`, `pendiente`, etc.)
- Stock o stock_minimo no entero (`abc`, `null`, `???`, etc.)
- Lineas con menos o mas columnas de las esperadas
- Lineas vacias

Para cada registro descartado por validacion se imprime una advertencia
en stdout, pero el proceso no se detiene.

## Autor

Santiago Alexey Corona Cubeiro
Instituto Politecnico Nacional
