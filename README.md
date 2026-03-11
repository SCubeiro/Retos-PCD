# Reto Semana 1 - Calculadora de Sumas

Programación para Ciencia de Datos | IPN 2026

## Descripción

Programa que lee líneas desde la entrada estándar (stdin), donde cada línea contiene valores separados por comas, y calcula la suma de todos los valores de cada línea.

Maneja correctamente:
- Líneas vacías (resultado: 0)
- Números decimales (se truncan, no redondean)
- Caracteres inválidos mezclados con números (se eliminan)
- Espacios extra alrededor de los valores
- Números negativos

## Cómo ejecutar

```bash
# Desde un archivo
python main.py < entrada.txt

# Entrada manual (terminar con Ctrl+D en Mac/Linux)
python main.py
```

## Ejemplo

**Entrada:**
```
1,2,3
10

1.9,2.1,3.7
1a2,3b,4
-5,10,3
```

**Salida:**
```
6
10
0
6
19
8
```

## Autor

Santiago Alexey Corona Cubeiro
Instituto Politécnico Nacional
