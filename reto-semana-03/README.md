# Reto Semana 3 - Analizador de Ventas

Programación para Ciencia de Datos | IPN 2026

## Descripción

Programa que lee transacciones de ventas en formato CSV desde la entrada estándar (stdin),
las agrupa por producto y genera un reporte consolidado ordenado por ingreso total descendente.

Maneja correctamente:
- Agrupación de múltiples transacciones del mismo producto
- Cálculo de unidades vendidas, ingreso total y precio promedio
- Ordenamiento por ingreso total (mayor a menor)
- Líneas con datos inválidos (cantidad o precio no numérico, columnas faltantes)
- Líneas vacías

## Cómo ejecutar

```bash
# Desde un archivo
python3 main.py < tests/entrada1.txt

# Entrada manual (terminar con Ctrl+D en Mac/Linux)
python3 main.py
```

## Ejemplo

**Entrada:**
```
fecha,producto,cantidad,precio_unitario
2026-01-01,Laptop,2,15000.00
2026-01-02,Mouse,10,250.00
2026-01-03,Laptop,1,14500.00
2026-01-04,Teclado,5,800.00
2026-01-05,Mouse,8,250.00
```

**Salida:**
```
producto,unidades_vendidas,ingreso_total,precio_promedio
Laptop,3,44500.00,14833.33
Mouse,18,4500.00,250.00
Teclado,5,4000.00,800.00
```

## Métricas calculadas

| Métrica | Fórmula |
|---------|---------|
| `unidades_vendidas` | Suma de todas las cantidades del producto |
| `ingreso_total` | Suma de (cantidad × precio) por transacción |
| `precio_promedio` | ingreso_total / unidades_vendidas |

## Pruebas

```bash
python3 main.py < tests/entrada1.txt | diff - tests/salida1.txt
python3 main.py < tests/entrada2.txt | diff - tests/salida2.txt
python3 main.py < tests/entrada3.txt | diff - tests/salida3.txt
```

| Caso | Descripción |
|------|-------------|
| 1    | Ejemplo principal: Laptop, Mouse, Teclado |
| 2    | Datos inválidos: cantidad y precio no numéricos, línea incompleta |
| 3    | Decimales, líneas vacías, múltiples productos |

## Autor

Santiago Alexey Corona Cubeiro
Instituto Politécnico Nacional
