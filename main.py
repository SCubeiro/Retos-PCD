import sys


def limpiar_valor(valor):
    """Quita espacios y caracteres invalidos. Conserva digitos, punto y signo negativo."""
    valor = valor.strip()
    return ''.join(c for c in valor if c in '0123456789.-')


def convertir(texto):
    """Convierte texto a entero truncando decimales. Retorna 0 si no es valido."""
    if not texto:
        return 0
    try:
        return int(float(texto))
    except ValueError:
        return 0


def procesar_linea(linea):
    """Procesa una linea: separa por comas, limpia, trunca y suma."""
    linea = linea.strip()
    if not linea:
        return 0
    valores = linea.split(',')
    return sum(convertir(limpiar_valor(v)) for v in valores)


def main():
    for linea in sys.stdin:
        print(procesar_linea(linea))


if __name__ == "__main__":
    main()
