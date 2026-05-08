# Reto Semana 5 - Perfilador de Datasets

Programacion para Ciencia de Datos | IPN 2026

## Descripcion

Herramienta de linea de comandos que recibe cualquier archivo CSV con
encabezados y genera un reporte de calidad de datos por columna:

- Tipo inferido (`numerico`, `fecha`, `booleano` o `texto`)
- Total de registros y valores nulos
- Porcentaje de nulos y de valores unicos
- Un valor de ejemplo (primer no nulo)

## Requisitos

- Python 3.8 o superior
- Sin dependencias externas (solo biblioteca estandar)

## Instalacion

```bash
git clone https://github.com/SCubeiro/reto-semana-05.git
cd reto-semana-05

python3 -m venv .venv

# Linux / Mac
source .venv/bin/activate
# Windows
.venv\Scripts\activate

pip install -r requirements.txt
```

## Uso

```bash
python3 main.py --input <ruta_csv_entrada> --output <ruta_csv_salida>
```

| Argumento        | Descripcion                          |
|------------------|--------------------------------------|
| `--input` / `-i` | Ruta al CSV a perfilar (requerido)   |
| `--output` / `-o`| Ruta donde guardar el perfil (requerido) |

## Estructura del proyecto

```
reto-semana-05/
|-- main.py
|-- README.md
|-- requirements.txt
|-- .gitignore
|-- data/
|   |-- ventas.csv
|   |-- empleados.csv
|   |-- sensores.csv
|-- outputs/
    |-- perfil_ventas.csv
    |-- perfil_empleados.csv
    |-- perfil_sensores.csv
```

## Ejemplo

Entrada (`data/ventas.csv`):

```csv
fecha,producto,cantidad,precio,vendedor
2026-01-01,Laptop,2,15000.00,Ana
2026-01-02,Mouse,10,250.00,Bob
2026-01-03,Teclado,,800.00,Ana
2026-01-04,Monitor,3,,Carlos
2026-01-05,Laptop,1,15000.00,
```

Comando:

```bash
python3 main.py --input data/ventas.csv --output outputs/perfil_ventas.csv
```

Salida (`outputs/perfil_ventas.csv`):

```csv
nombre_columna,tipo_inferido,total_registros,valores_nulos,porcentaje_nulos,valores_unicos,porcentaje_unicos,ejemplo_valor
fecha,fecha,5,0,0.00,5,100.00,2026-01-01
producto,texto,5,0,0.00,4,80.00,Laptop
cantidad,numerico,5,1,20.00,4,80.00,2
precio,numerico,5,1,20.00,3,60.00,15000.00
vendedor,texto,5,1,20.00,3,60.00,Ana
```

## Reglas de procesamiento

### Deteccion de nulos

Se considera nulo:
- Celda vacia (`,,`)
- Celda con solo espacios
- `None`

NO son nulos: `0`, `"0"`, `"null"`, `"None"` (texto literal).

### Inferencia de tipo

Se cuenta cuantos valores no nulos cumplen cada tipo y se asigna el tipo
cuya cobertura sea **>= 80%**:

| Tipo      | Condicion                                |
|-----------|------------------------------------------|
| fecha     | formato `YYYY-MM-DD`, anio 1900-2100     |
| booleano  | `true/false/yes/no/si/1/0/t/f`           |
| numerico  | convertible a `float`                    |
| texto     | cualquier otro caso (default)            |

Se evalua primero `fecha` y `booleano` porque tambien podrian parecer
numericos (`'1'`, `'0'`).

### Valores unicos

Solo se consideran valores no nulos. Distincion sensible a mayusculas:
`Ana` y `ana` cuentan como dos valores distintos.

## Autor

Santiago Alexey Corona Cubeiro
Instituto Politecnico Nacional
