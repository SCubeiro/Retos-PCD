# Reto 02 — Clasificador de Temperaturas

Programa que lee reportes de temperatura de ciudades en formato CSV desde la entrada estándar, convierte todo a Celsius y clasifica cada ciudad según su temperatura.

## Problema

Una agencia de viajes recibe temperaturas de ciudades del mundo mezclando Celsius y Fahrenheit. El programa normaliza las unidades y etiqueta cada ciudad con su clasificación climática.

## Uso

```bash
python3 main.py < tests/entrada1.txt
```

## Formato de entrada

CSV con encabezado `ciudad,temperatura,unidad`. La unidad puede ser `C` o `F` (también se acepta en minúscula). Se ignoran líneas con datos inválidos.

```
ciudad,temperatura,unidad
CDMX,22,C
Nueva York,50,F
```

## Formato de salida

CSV con encabezado `ciudad,temperatura_celsius,clasificacion`. La temperatura siempre se muestra con un decimal.

```
ciudad,temperatura_celsius,clasificacion
CDMX,22.0,Templado
Nueva York,10.0,Frio
```

## Clasificación

| Rango (°C)   | Clasificación |
|--------------|---------------|
| < 0          | Congelante    |
| 0 a 15       | Frio          |
| 16 a 25      | Templado      |
| 26 a 35      | Calido        |
| > 35         | Extremo       |

## Conversión

`celsius = (fahrenheit - 32) × 5 / 9`

## Pruebas

| Archivo         | Descripción                                      |
|-----------------|--------------------------------------------------|
| entrada1.txt    | Ejemplo básico del reto (Celsius y Fahrenheit)   |
| entrada2.txt    | Valores en los límites exactos, espacios, minúsculas |
| entrada3.txt    | Líneas inválidas que deben ignorarse             |

Para verificar contra la salida esperada:

```bash
python3 main.py < tests/entrada1.txt | diff - tests/salida1.txt
python3 main.py < tests/entrada2.txt | diff - tests/salida2.txt
python3 main.py < tests/entrada3.txt | diff - tests/salida3.txt
```

Si no imprime nada, el output es correcto.
