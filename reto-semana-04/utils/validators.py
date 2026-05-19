"""Validaciones para los campos de un producto."""

import math


def validar_sku(sku):
    """SKU debe ser texto no vacio."""
    if not sku or not str(sku).strip():
        return False
    return True


def validar_precio(precio):
    """Precio debe ser numerico finito y >= 0.

    float() acepta 'inf', '-inf', 'NaN', '1e999', etc. y devuelve inf/nan,
    lo que contamina los calculos. Exigimos que el resultado sea finito.
    """
    try:
        p = float(precio)
    except (ValueError, TypeError):
        return False
    return math.isfinite(p) and p >= 0


def validar_stock(stock):
    """Stock debe ser entero >= 0."""
    try:
        # Aceptamos solo enteros: '5' OK, '5.5' no es stock valido
        s = str(stock).strip()
        if s == "":
            return False
        return int(s) >= 0
    except (ValueError, TypeError):
        return False


def validar_producto(sku, nombre, categoria, precio, stock, stock_minimo):
    """Valida todos los campos. Retorna (es_valido, mensaje_error)."""
    if not validar_sku(sku):
        return False, "SKU vacio o invalido"

    if not nombre or not str(nombre).strip():
        return False, "Nombre vacio"

    if not validar_precio(precio):
        return False, f"Precio invalido: {precio}"

    if not validar_stock(stock):
        return False, f"Stock invalido: {stock}"

    if not validar_stock(stock_minimo):
        return False, f"Stock minimo invalido: {stock_minimo}"

    return True, None
