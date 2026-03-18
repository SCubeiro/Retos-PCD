import sys

def fahrenheit_a_celsius(f):
    """Convierte Fahrenheit a Celsius."""
    return (f - 32) * 5 / 9

def clasificar_temperatura(celsius):
    """Clasifica la temperatura segun rangos definidos."""
    if celsius < 0:
        return "Congelante"
    elif celsius <= 15:  # 0 a 15
        return "Frio"
    elif celsius <= 25:  # 16 a 25
        return "Templado"
    elif celsius <= 35:  # 26 a 35
        return "Calido"
    else:  # > 35
        return "Extremo"

def main():
    for linea in sys.stdin:
        print(clasificar_temperatura(fahrenheit_a_celsius(linea)))


if __name__ == "__main__":
    main()