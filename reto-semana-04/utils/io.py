"""Funciones de lectura/escritura del sistema de inventario."""


def leer_inventario(ruta_archivo):
    """Lee el CSV de inventario y retorna una lista de diccionarios.

    No valida los datos, solo arma el diccionario por linea respetando los
    encabezados. Las lineas con un numero de columnas distinto al esperado
    se descartan aqui mismo para que el resto del pipeline reciba registros
    parejos.
    """
    productos_raw = []

    with open(ruta_archivo, "r", encoding="utf-8") as archivo:
        lineas = archivo.readlines()

    if not lineas:
        return productos_raw

    encabezados = [h.strip() for h in lineas[0].strip().split(",")]

    for linea in lineas[1:]:
        linea = linea.strip()
        if not linea:
            continue

        valores = linea.split(",")
        if len(valores) != len(encabezados):
            # columnas faltantes o de mas: se ignora la linea
            continue

        productos_raw.append(dict(zip(encabezados, valores)))

    return productos_raw


def escribir_reporte(productos, ruta_archivo):
    """Guarda el reporte de productos a reordenar en formato CSV."""
    encabezados = [
        "sku", "nombre", "categoria", "stock_actual",
        "stock_minimo", "unidades_faltantes", "valor_inventario"
    ]

    with open(ruta_archivo, "w", encoding="utf-8") as archivo:
        archivo.write(",".join(encabezados) + "\n")

        for p in productos:
            fila = (
                f"{p.sku},{p.nombre},{p.categoria},{p.stock},"
                f"{p.stock_minimo},{p.unidades_faltantes()},"
                f"{p.valor_inventario():.2f}"
            )
            archivo.write(fila + "\n")
