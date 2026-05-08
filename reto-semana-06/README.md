# Reto Semana 6 - Validador de Codigos con Regex

Programacion para Ciencia de Datos | IPN 2026

## Descripcion

Validador automatico de codigos de productos, envios, empleados y
facturas usando expresiones regulares. Implementado como notebook de
Jupyter siguiendo el formato pedido por el profesor.

## Tipos de codigo soportados

| Tipo      | Formato                  | Ejemplo valido        |
|-----------|--------------------------|-----------------------|
| Producto  | `ABC-1234-MX`            | `TEC-0001-MX`         |
| Envio     | `ENV-YYYY-MM-DD-NNNNNN`  | `ENV-2024-03-15-001234` |
| Empleado  | `EMP-XXX-NNNN`           | `EMP-VEN-1234`        |
| Factura   | `FAC-S-NNNNNN`           | `FAC-A-123456`        |

### Reglas extra

- **Producto:** categoria 3 letras mayus, numero 4 digitos, pais 2 letras mayus.
- **Envio:** anio 2020-2030, mes 01-12, dia 01-31.
- **Empleado:** departamento debe estar en `['VEN', 'ADM', 'TEC', 'LOG', 'RHH']`,
  el numero NO puede empezar con 0.
- **Factura:** serie debe ser una de `A, B, C, D, E`.

## Estructura del proyecto

```
reto-semana-06/
|-- README.md
|-- .gitignore
|-- reto_06_validador_codigos.ipynb   # Notebook con todas las celdas implementadas
|-- resultados.csv                    # CSV exportado por la celda del bonus
```

## Como ejecutar

```bash
# Abrir el notebook en Jupyter / VSCode / Colab y ejecutar todas las celdas
jupyter notebook reto_06_validador_codigos.ipynb
```

O para ejecutarlo sin abrir la UI (requiere `nbconvert`):

```bash
pip install nbconvert ipykernel
jupyter nbconvert --to notebook --execute --inplace reto_06_validador_codigos.ipynb
```

## Funciones implementadas

### Parte 1 - Validadores individuales

```python
validar_producto(codigo)   # -> {"valido", "categoria", "numero", "pais"}
validar_envio(codigo)      # -> {"valido", "fecha", "secuencial"}
validar_empleado(codigo)   # -> {"valido", "departamento", "numero"}
validar_factura(codigo)    # -> {"valido", "serie", "numero"}
```

### Parte 2 - Validador universal

`validar_codigo(codigo)` detecta el tipo por prefijo (`ENV-`, `EMP-`,
`FAC-`) o por la forma `letras-digitos-letras` (productos), y delega
al validador correspondiente.

### Parte 3 - Procesamiento por lotes

`procesar_lote(codigos)` recorre la lista, llama a `validar_codigo` por
cada uno y genera el reporte agregado:

```
{
  "total": 25,
  "validos": 11,
  "invalidos": 14,
  "por_tipo": {
    "producto":    {"total": 6, "validos": 3},
    "envio":       {"total": 5, "validos": 2},
    "empleado":    {"total": 6, "validos": 3},
    "factura":     {"total": 6, "validos": 3},
    "desconocido": {"total": 2, "validos": 0}
  },
  "detalle": [...]
}
```

### Bonus

- `sugerir_correccion(codigo)`: limpia espacios y mayusculas; si la
  version normalizada valida con algun tipo, la retorna como sugerencia.
- `validar_fecha_real(anio, mes, dia)`: usa `datetime.date` para detectar
  fechas imposibles (30 de febrero, 31 de abril, etc.).
- `exportar_resultados(reporte, archivo)`: guarda el detalle del reporte
  en un CSV con columnas `codigo, tipo, valido, detalles`.

## Resultados sobre los 25 codigos de prueba

```
Total procesados: 25
Validos: 11 (44.0%)
Invalidos: 14 (56.0%)

Producto    :   3/6   (50% validos)
Envio       :   2/5   (40% validos)
Empleado    :   3/6   (50% validos)
Factura     :   3/6   (50% validos)
Desconocido :   0/2   (0% validos)
```

> Nota: el enunciado del notebook declara "Total: 26, Validos: 12" como
> resultado esperado, pero la lista `CODIGOS_PRUEBA` solo contiene 25
> codigos (6+5+6+6+2). El desglose por tipo coincide exactamente con el
> esperado, asi que se trata de un error tipografico en el total del
> enunciado.

## Autor

Santiago Alexey Corona Cubeiro
Instituto Politecnico Nacional
