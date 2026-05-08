"""
Sistema de Inventario Modular.
Lee data/inventario.csv y genera outputs/reporte_inventario.csv con los
productos que tienen stock por debajo del minimo.
"""

from models.producto import Producto
from utils.validators import validar_producto
from utils.io import leer_inventario, escribir_reporte


ARCHIVO_INVENTARIO = "data/inventario.csv"
ARCHIVO_REPORTE = "outputs/reporte_inventario.csv"


def crear_productos(datos_raw):
    """Convierte los diccionarios crudos del CSV en objetos Producto.

    Las filas que no pasan validar_producto se descartan con una advertencia
    impresa, para que el reporte solo trabaje con datos limpios.
    """
    productos = []

    for datos in datos_raw:
        es_valido, error = validar_producto(
            datos.get("sku"),
            datos.get("nombre"),
            datos.get("categoria"),
            datos.get("precio"),
            datos.get("stock"),
            datos.get("stock_minimo"),
        )

        if not es_valido:
            print(f"Advertencia: registro ignorado - {error}")
            continue

        producto = Producto(
            sku=datos["sku"],
            nombre=datos["nombre"],
            categoria=datos["categoria"],
            precio=float(datos["precio"]),
            stock=int(datos["stock"]),
            stock_minimo=int(datos["stock_minimo"]),
        )
        productos.append(producto)

    return productos


def filtrar_necesitan_reorden(productos):
    return [p for p in productos if p.necesita_reorden()]


def ordenar_por_faltantes(productos):
    return sorted(productos, key=lambda p: p.unidades_faltantes(), reverse=True)


def main():
    print("=" * 50)
    print("SISTEMA DE INVENTARIO - Reporte de Reorden")
    print("=" * 50)

    print(f"\nLeyendo inventario de: {ARCHIVO_INVENTARIO}")
    datos_raw = leer_inventario(ARCHIVO_INVENTARIO)
    print(f"Registros leidos: {len(datos_raw)}")

    productos = crear_productos(datos_raw)
    print(f"Productos validos: {len(productos)}")

    necesitan_reorden = filtrar_necesitan_reorden(productos)
    necesitan_reorden = ordenar_por_faltantes(necesitan_reorden)
    print(f"Productos que necesitan reorden: {len(necesitan_reorden)}")

    print("\n" + "-" * 50)
    print("PRODUCTOS QUE NECESITAN REORDEN:")
    print("-" * 50)
    for p in necesitan_reorden:
        print(p)

    escribir_reporte(necesitan_reorden, ARCHIVO_REPORTE)
    print(f"\nReporte guardado en: {ARCHIVO_REPORTE}")

    print("\n" + "=" * 50)
    print("Proceso completado")
    print("=" * 50)


if __name__ == "__main__":
    main()
