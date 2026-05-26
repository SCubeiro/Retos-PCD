# Reto Semana 6 - Validador de Codigos con Regex

Programacion para Ciencia de Datos | IPN 2026

## Descripcion

Validador automatico de codigos de una empresa de logistica usando
expresiones regulares. Lee los codigos desde la entrada estandar (stdin),
uno por linea, detecta de que tipo es cada uno y dice si es valido o no.
El resultado se escribe como CSV a la salida estandar (stdout).

Maneja correctamente:
- Deteccion de tipo por la **estructura** del codigo, no solo por el prefijo
- Validacion estricta por tipo (mayusculas, rangos de fecha, listas permitidas)
- Codigos con tipo correcto pero invalidos (ej. `tec-0001-MX`)
- Codigos que no calzan ninguna estructura (`desconocido`)
- Lineas vacias o con solo espacios (se ignoran)
- Espacios sobrantes alrededor del codigo

## Tipos de codigo

| Tipo      | Formato                 | Ejemplo valido          |
|-----------|-------------------------|-------------------------|
| Producto  | `ABC-1234-MX`           | `TEC-0001-MX`           |
| Envio     | `ENV-YYYY-MM-DD-NNNNNN` | `ENV-2024-03-15-001234` |
| Empleado  | `EMP-XXX-NNNN`          | `EMP-VEN-1234`          |
| Factura   | `FAC-S-NNNNNN`          | `FAC-A-123456`          |

## Reglas de validacion

- **Producto:** categoria 3 letras mayusculas, numero 4 digitos, pais 2 letras mayusculas.
- **Envio:** anio 2020-2030, mes 01-12, dia 01-31, secuencial 6 digitos.
- **Empleado:** departamento en `['VEN', 'ADM', 'TEC', 'LOG', 'RHH']`,
  numero de 4 digitos que **no** empieza con 0.
- **Factura:** serie en `['A', 'B', 'C', 'D', 'E']` (mayuscula), numero 6 digitos.
- **Desconocido:** siempre `INVALIDO`.

## Deteccion de tipo

El tipo se decide por la **estructura** del codigo, no solo por el prefijo.
Un codigo que no calza la estructura base cae en `desconocido` aunque empiece
con un prefijo conocido:

| Codigo         | Tipo        | Razon                                  |
|----------------|-------------|----------------------------------------|
| `TEC-001-MX`   | desconocido | solo 3 digitos, no es `XXX-NNNN-XX`    |
| `TECH-0001-MX` | desconocido | 4 letras en la categoria               |
| `EMP-VEN-123`  | desconocido | solo 3 digitos, no es `EMP-XXX-NNNN`   |
| `FAC-A-12345`  | desconocido | solo 5 digitos, no es `FAC-S-NNNNNN`   |

Un codigo puede ser del tipo correcto y aun asi ser `INVALIDO`:

| Codigo         | Tipo     | Razon                          |
|----------------|----------|--------------------------------|
| `tec-0001-MX`  | producto | categoria/pais en minuscula    |
| `EMP-XXX-1234` | empleado | `XXX` no es un departamento    |
| `FAC-a-123456` | factura  | serie en minuscula             |

## Estructura del proyecto

```
reto-semana-06/
|-- main.py                 # solucion: lee de stdin, escribe csv a stdout
|-- README.md
|-- .gitignore
|-- tests/
    |-- codigos.txt         # codigos de ejemplo
    |-- salida_esperada.txt # salida de referencia para el diff
```

## Como ejecutar

```bash
# Desde un archivo
python3 main.py < tests/codigos.txt

# Guardando la salida en un csv
python3 main.py < tests/codigos.txt > resultados.csv

# Entrada manual (terminar con Ctrl+D en Mac/Linux)
python3 main.py
```

## Ejemplo

**Entrada:**
```
TEC-0001-MX
tec-0001-MX
TEC-001-MX
ENV-2024-03-15-001234
ENV-2019-03-15-001234
EMP-VEN-1234
EMP-VEN-0123
EMP-VEN-123
FAC-A-123456
FAC-a-123456
XXX-1234
```

**Salida:**
```
codigo,tipo,valido
TEC-0001-MX,producto,VALIDO
tec-0001-MX,producto,INVALIDO
TEC-001-MX,desconocido,INVALIDO
ENV-2024-03-15-001234,envio,VALIDO
ENV-2019-03-15-001234,envio,INVALIDO
EMP-VEN-1234,empleado,VALIDO
EMP-VEN-0123,empleado,INVALIDO
EMP-VEN-123,desconocido,INVALIDO
FAC-A-123456,factura,VALIDO
FAC-a-123456,factura,INVALIDO
XXX-1234,desconocido,INVALIDO
```

## Funciones

| Funcion              | Que hace                                            |
|----------------------|-----------------------------------------------------|
| `detectar_tipo`      | reconoce el tipo por estructura con regex anclados  |
| `validar_producto`   | exige categoria y pais en mayusculas                |
| `validar_envio`      | valida los rangos de anio, mes y dia                |
| `validar_empleado`   | valida departamento permitido y numero sin 0 inicial|
| `validar_factura`    | valida la serie contra `SERIES_VALIDAS`             |
| `validar_codigo`     | detecta el tipo y delega al validador, retorna `(tipo, es_valido)` |

## Pruebas

```bash
python3 main.py < tests/codigos.txt | diff - tests/salida_esperada.txt
```

Si no imprime nada, la salida coincide con la esperada.

## Autor

Santiago Alexey Corona Cubeiro
Instituto Politecnico Nacional
