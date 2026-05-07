"""
Perfilador de Datasets CSV.

Lee cualquier CSV con encabezados y genera un reporte de calidad: tipo
inferido, nulos, valores unicos y un ejemplo por cada columna.
"""


def es_valor_nulo(valor):
    """Considera nulo: None, string vacio o solo espacios.

    NO son nulos: el numero 0, '0', 'null' o 'None' como texto.
    """
    if valor is None:
        return True
    if isinstance(valor, str) and valor.strip() == "":
        return True
    return False


def es_numerico(valor):
    try:
        float(str(valor).replace(",", "").strip())
        return True
    except (ValueError, TypeError):
        return False


def es_fecha(valor):
    """Reconoce fechas con formato YYYY-MM-DD."""
    v = str(valor).strip()
    if len(v) < 10 or v[4] != "-" or v[7] != "-":
        return False
    try:
        anio = int(v[:4])
        mes = int(v[5:7])
        dia = int(v[8:10])
    except ValueError:
        return False
    return 1900 <= anio <= 2100 and 1 <= mes <= 12 and 1 <= dia <= 31


def es_booleano(valor):
    v = str(valor).strip().lower()
    return v in {"true", "false", "yes", "no", "si", "1", "0", "t", "f"}
