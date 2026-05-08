import sys

def fahrenheit_a_celsius(f):
    """Convierte Fahrenheit a Celsius."""
    return (f - 32) * 5 / 9

def clasificar(celsius):
    """Clasifica la temperatura."""
    if celsius < 0:
        return "Congelante"
    elif celsius <= 15:
        return "Frio"
    elif celsius <= 25:
        return "Templado"
    elif celsius <= 35:
        return "Calido"
    else:
        return "Extremo"

def main():
    # Leer y descartar encabezado de entrada
    primera_linea = True
    
    # Imprimir encabezado de salida
    print("ciudad,temperatura_celsius,clasificacion")
    
    for linea in sys.stdin:
        linea = linea.strip()
        
        # Saltar encabezado
        if primera_linea:
            primera_linea = False
            continue
        
        # Saltar lineas vacias
        if not linea:
            continue
        
        # Separar campos
        partes = linea.split(',')
        if len(partes) != 3:
            continue  # Ignorar linea invalida
        
        ciudad = partes[0].strip()
        temp_str = partes[1].strip()
        unidad = partes[2].strip().upper()
        
        # Validar unidad
        if unidad not in ['C', 'F']:
            continue  # Ignorar
        
        # Convertir temperatura
        try:
            temp = float(temp_str)
        except ValueError:
            continue  # Ignorar si no es numero
        
        # Convertir a Celsius
        if unidad == 'F':
            celsius = fahrenheit_a_celsius(temp)
        else:
            celsius = temp
        
        # Clasificar y imprimir
        clasificacion = clasificar(celsius)
        print(f"{ciudad},{celsius:.1f},{clasificacion}")

if __name__ == "__main__":
    main()