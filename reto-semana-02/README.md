# Reto Semana 2 - Clasificador de Temperaturas

Programación para Ciencia de Datos | IPN 2026

## Descripción

Programa que lee reportes de temperatura de ciudades en formato CSV desde la entrada estándar (stdin), convierte todo a Celsius y clasifica cada ciudad según su temperatura.

Maneja correctamente:
- Conversión de Fahrenheit a Celsius
- Clasificación en 5 rangos: Congelante, Frio, Templado, Calido, Extremo
- Unidades en mayúscula o minúscula (C, F, c, f)
- Espacios extra alrededor de los campos
- Líneas vacías o con datos inválidos (se ignoran)

## Cómo ejecutar

```bash
# Desde un archivo
python main.py < tests/entrada1.txt

# Entrada manual (terminar con Ctrl+D en Mac/Linux)
python main.py
```

## Ejemplo

**Entrada:**
```
ciudad,temperatura,unidad
CDMX,22,C
Nueva York,50,F
Moscu,-10,C
Miami,95,F
```

**Salida:**
```
ciudad,temperatura_celsius,clasificacion
CDMX,22.0,Templado
Nueva York,10.0,Frio
Moscu,-10.0,Congelante
Miami,35.0,Calido
```

## Clasificación

| Rango (°C) | Clasificación |
|------------|---------------|
| < 0        | Congelante    |
| 0 a 15     | Frio          |
| 16 a 25    | Templado      |
| 26 a 35    | Calido        |
| > 35       | Extremo       |

## Pruebas

```bash
python main.py < tests/entrada1.txt | diff - tests/salida1.txt
python main.py < tests/entrada2.txt | diff - tests/salida2.txt
python main.py < tests/entrada3.txt | diff - tests/salida3.txt
```

## Autor

Santiago Alexey Corona Cubeiro
Instituto Politécnico Nacional
