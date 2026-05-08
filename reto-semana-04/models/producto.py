class Producto:
    """Representa un producto en el inventario."""

    def __init__(self, sku, nombre, categoria, precio, stock, stock_minimo):
        self.sku = sku
        self.nombre = nombre
        self.categoria = categoria
        self.precio = precio
        self.stock = stock
        self.stock_minimo = stock_minimo

    def necesita_reorden(self):
        """True si el stock actual cayo por debajo del stock minimo."""
        return self.stock < self.stock_minimo

    def unidades_faltantes(self):
        """Unidades que faltan para alcanzar el stock minimo."""
        if self.necesita_reorden():
            return self.stock_minimo - self.stock
        return 0

    def valor_inventario(self):
        """Valor monetario del inventario actual: precio * stock."""
        return self.precio * self.stock

    def __str__(self):
        estado = "[REORDEN]" if self.necesita_reorden() else "[OK]"
        return f"{estado} {self.sku}: {self.nombre} - Stock: {self.stock}/{self.stock_minimo}"

    def __repr__(self):
        return (f"Producto('{self.sku}', '{self.nombre}', '{self.categoria}', "
                f"{self.precio}, {self.stock}, {self.stock_minimo})")
