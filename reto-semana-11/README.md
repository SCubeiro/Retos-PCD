# Reto Semana 11 - Sistema de Gestion de Calificaciones

Programacion para Ciencia de Datos | IPN 2026

## Descripcion

Gestor de calificaciones para el departamento de Control Escolar construido con
**Pandas DataFrames**. Trabaja con tres tablas relacionadas (estudiantes,
calificaciones y materias) y permite consultar datos, calcular promedios,
identificar estudiantes en riesgo y generar reportes academicos. Los datos son
simulados: **15 estudiantes** de los semestres 2, 3 y 4, con **95 registros** de
calificaciones (que incluyen algunos valores nulos a proposito). Implementado
como notebook de Jupyter siguiendo el formato pedido por el profesor.

## Temas aplicados

- Construccion y relacion de DataFrames (`merge` por `boleta` y `materia_id`)
- Agregaciones con `groupby` (promedio por estudiante, por materia, por semestre)
- Manejo de NaN: el promedio por materia usa `mean(axis=1)` (ignora parciales faltantes)
- Filtrado booleano y busqueda parcial de texto con `str.contains`
- Validacion de integridad (nulos y valores fuera del rango [0, 10])
- Ordenamiento y ranking con `sort_values`
- Exportacion a CSV y JSON (`to_csv`, `json.dump`)
- Bonus: predictor de riesgo por tendencia y comparador de estudiantes

## Funciones implementadas

| Funcion | Que hace |
|---------|----------|
| `info_general` | Totales, semestres y materias con registros |
| `validar_datos` | Cuenta nulos y calificaciones fuera de rango |
| `buscar_estudiante` | Busca por boleta, nombre (parcial) o semestre |
| `obtener_kardex` | Kardex con materias, promedio y aprobadas/reprobadas |
| `filtrar_por_rendimiento` | Filtra estudiantes por rango de promedio |
| `calcular_promedio_materia` | Estadisticas de una materia y tasa de aprobacion |
| `ranking_estudiantes` | Top-N por promedio general |
| `estadisticas_por_semestre` | Agregaciones por semestre |
| `identificar_estudiantes_riesgo` | Riesgo por bajo promedio y/o materias reprobadas |
| `generar_reporte_academico` | Integra todo en un reporte |
| `exportar_kardex` | Exporta el kardex a CSV o JSON |
| `predecir_riesgo_proximo_semestre` (bonus) | Riesgo futuro por tendencia a la baja |
| `comparar_estudiantes` (bonus) | Compara el rendimiento de dos estudiantes |

## Decisiones de diseno

- **Promedio de una materia** = media de `parcial_1`, `parcial_2` y `final`
  ignorando los faltantes (NaN), tal como pide el consejo de manejar nulos.
- **Promedio de un estudiante** = media de los promedios de sus materias.
- **Tasa de aprobacion** = porcentaje de registros materia-alumno con promedio
  >= 6 (granularidad por registro, no por alumno).
- **En riesgo** = promedio general < umbral (7.0) **o** mas de 2 materias
  reprobadas; el motivo puede ser "Bajo promedio", "Mat. reprob." o "Ambos".

## Estructura del proyecto

```
reto-semana-11/
  reto_11_gestor_estudiantes.ipynb       # solucion completa, ejecutada con outputs
  kardex_2021630001_YYYYMMDD.csv         # kardex exportado de ejemplo (CSV)
  kardex_2021630001_YYYYMMDD.json        # kardex exportado de ejemplo (JSON)
  README.md
  .gitignore
```

## Resultados

```
RESUMEN GENERAL
  Total de estudiantes : 15
  Promedio global      : 7.67
  Tasa de aprobacion   : 89.5%

POR SEMESTRE        Estudiantes  Promedio  Tasa Aprob.
  Semestre 2                  5      7.96        92.0%
  Semestre 3                  5      7.75        91.4%
  Semestre 4                  5      7.30        85.7%

ESTUDIANTES EN RIESGO: 3 (umbral 7.0, max 2 reprobadas)
```

- Se exporto el kardex del estudiante 2021630001 a CSV y JSON.

> Nota: la seccion "Salida Esperada" del enunciado es ilustrativa (proviene de
> otra muestra de datos); lo que se respeta es el formato y la logica, no los
> numeros exactos.

## Casos limite cubiertos

DataFrames vacios, calificaciones con NaN y fuera de rango, boletas inexistentes,
semestre no numerico, criterio de busqueda invalido y formato de exportacion no
soportado (todos con mensaje claro en espanol). Estan demostrados en la seccion
"Pruebas de Casos Limite" del notebook y ninguno rompe la ejecucion.

## Autor

Santiago Alexey Corona Cubeiro
Instituto Politecnico Nacional
