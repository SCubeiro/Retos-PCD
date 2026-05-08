import sys

def parsear_linea(linea):
    """Parsea una linea CSV y retorna (producto, cantidad, precio) o None si es invalida."""
    partes = linea.split(',')
    if len(partes) != 4:
        return None

    producto = partes[1]

    try:
        cantidad = int(partes[2])
        precio = float(partes[3])
    except ValueError:
        return None

    return producto, cantidad, precio


def agrupar_ventas(lineas):
    """Agrupa las transacciones por producto acumulando unidades e ingresos."""
    productos = {}

    for linea in lineas:
        resultado = parsear_linea(linea)
        if resultado is None:
            continue

        producto, cantidad, precio = resultado

        if producto not in productos:
            productos[producto] = {
                "unidades": 0,
                "ingreso": 0.0
            }

        productos[producto]["unidades"] += cantidad
        productos[producto]["ingreso"] += cantidad * precio

    return productos


def main():
    lineas = []
    primera_linea = True

    for linea in sys.stdin:
        linea = linea.strip()

        if primera_linea:
            primera_linea = False
            continue

        if not linea:
            continue

        lineas.append(linea)

    # Agrupar transacciones por producto
    productos = agrupar_ventas(lineas)

    # Calcular precio promedio
    for prod in productos:
        unidades = productos[prod]["unidades"]
        ingreso = productos[prod]["ingreso"]
        productos[prod]["promedio"] = ingreso / unidades if unidades > 0 else 0.0

    # Ordenar por ingreso total descendente
    productos_ordenados = sorted(
        productos.items(),
        key=lambda x: x[1]["ingreso"],
        reverse=True
    )

    # Imprimir salida CSV
    print("producto,unidades_vendidas,ingreso_total,precio_promedio")
    for nombre, datos in productos_ordenados:
        print(f"{nombre},{datos['unidades']},{datos['ingreso']:.2f},{datos['promedio']:.2f}")


if __name__ == "__main__":
    main()
