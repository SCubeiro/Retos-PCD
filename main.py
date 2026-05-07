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


def inferir_tipo(valores):
    """Tipo de la columna por mayoria simple, umbral 80%.

    El orden de evaluacion importa: primero fecha y booleano porque tambien
    pueden parecer numericos ('1', '0' son booleanos validos).
    """
    no_nulos = [v for v in valores if not es_valor_nulo(v)]
    if not no_nulos:
        return "texto"

    total = len(no_nulos)
    umbral = 0.8

    n_fechas = sum(1 for v in no_nulos if es_fecha(v))
    n_booleanos = sum(1 for v in no_nulos if es_booleano(v))
    n_numericos = sum(1 for v in no_nulos if es_numerico(v))

    if n_fechas / total >= umbral:
        return "fecha"
    if n_booleanos / total >= umbral:
        return "booleano"
    if n_numericos / total >= umbral:
        return "numerico"
    return "texto"


def calcular_porcentaje(parte, total):
    if total == 0:
        return 0.00
    return round((parte / total) * 100, 2)


def perfilar_columna(nombre, valores):
    """Diccionario con el perfil completo de una sola columna."""
    total = len(valores)
    nulos = sum(1 for v in valores if es_valor_nulo(v))
    no_nulos = [v for v in valores if not es_valor_nulo(v)]
    unicos = len(set(no_nulos))
    ejemplo = no_nulos[0] if no_nulos else ""

    return {
        "nombre_columna": nombre,
        "tipo_inferido": inferir_tipo(valores),
        "total_registros": total,
        "valores_nulos": nulos,
        "porcentaje_nulos": calcular_porcentaje(nulos, total),
        "valores_unicos": unicos,
        "porcentaje_unicos": calcular_porcentaje(unicos, total),
        "ejemplo_valor": ejemplo,
    }
