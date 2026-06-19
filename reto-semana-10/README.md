# Reto Semana 10 - Analizador de Precios de Acciones

Programacion para Ciencia de Datos | IPN 2026

## Descripcion

Analizador del comportamiento historico de precios de acciones construido con
**Pandas Series**. A partir de una serie de precios de cierre diarios (indice de
fechas habiles) calcula estadisticas, mide rendimiento y riesgo, genera
indicadores tecnicos y produce senales y alertas de trading. Se analizan tres
acciones simuladas (60 dias cada una): **ACME Corp** (tendencia leve),
**VolatilTech** (alta volatilidad) y **DeclineCorp** (tendencia bajista).
Implementado como notebook de Jupyter siguiendo el formato pedido por el profesor.

## Temas aplicados

- Estadisticas de Series: `.iloc[-1]`, `.min/.max/.mean/.median/.std`
- Rendimientos diarios con `.pct_change()`
- Medias moviles simples con `.rolling(ventana).mean()`
- Bandas de Bollinger (media movil +/- N desviaciones)
- Maximos y minimos locales con ventana centrada
- Clasificacion de tendencia (ALCISTA / BAJISTA / LATERAL)
- Senales de trading por cruce de medias moviles (COMPRA / VENTA / MANTENER)
- Alertas por cambios significativos y clasificacion de volatilidad
- `.idxmax()` / `.idxmin()` para ubicar el mejor y peor dia
- Bonus: RSI (Relative Strength Index) y backtesting de la estrategia

## Funciones implementadas

| Funcion | Que hace |
|---------|----------|
| `estadisticas_basicas` | Estadisticas descriptivas de los precios |
| `calcular_rendimientos` | Rendimiento diario porcentual |
| `analisis_rendimientos` | Total, promedio, mejor/peor dia, dias +/-, volatilidad |
| `media_movil` | Media movil simple (SMA) |
| `bandas_bollinger` | Banda media, superior e inferior |
| `detectar_maximos_minimos` | Maximos y minimos locales |
| `clasificar_tendencia` | ALCISTA / BAJISTA / LATERAL |
| `generar_senales_trading` | COMPRA / VENTA / MANTENER por cruce de MAs |
| `alertas_precio` | Alertas de SUBIDA/CAIDA sobre un umbral |
| `clasificar_volatilidad` | BAJA / MEDIA / ALTA / MUY ALTA |
| `generar_reporte_completo` | Integra todo en un reporte |
| `calcular_rsi` (bonus) | Indice de fuerza relativa |
| `backtest_estrategia` (bonus) | Simula la estrategia y mide su rendimiento |

## Estructura del proyecto

```
reto-semana-10/
  reto_10_analizador_acciones.ipynb   # solucion completa, ejecutada con outputs
  README.md
  .gitignore
```

## Resultados

Comparacion de las tres acciones (datos simulados con `seed=42`):

```
ACME Corp     Rendimiento:  -7.75%   Volatilidad: MEDIA      Tendencia: LATERAL
VolatilTech   Rendimiento: +33.35%   Volatilidad: MUY ALTA   Tendencia: ALCISTA
DeclineCorp   Rendimiento: -33.81%   Volatilidad: MEDIA      Tendencia: BAJISTA
```

- Sistema de alertas: **24 alertas** (umbral 5%) detectadas en VolatilTech.
- RSI de ACME al cierre: **62.28**; backtesting de la estrategia: **+3.03%**.

> Nota: la seccion "Salida Esperada" del enunciado es ilustrativa (proviene de
> otra muestra de datos); lo que se respeta es el formato y la logica, no los
> numeros exactos.

## Casos limite cubiertos

Series vacias o de un solo dato, NaN intercalados, ventanas mayores que la serie,
ventanas invalidas (error claro en espanol) y valores no numericos (coaccion a
NaN). Estan demostrados en la seccion "Pruebas de Casos Limite" del notebook y
ninguno rompe la ejecucion.

## Autor

Santiago Alexey Corona Cubeiro
Instituto Politecnico Nacional
