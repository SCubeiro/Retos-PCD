import sys
import re

DEPARTAMENTOS_VALIDOS = ['VEN', 'ADM', 'TEC', 'LOG', 'RHH']
SERIES_VALIDAS = ['A', 'B', 'C', 'D', 'E']


def detectar_tipo(codigo):
    """Detecta el tipo de codigo por su estructura, no solo por el prefijo."""
    # La estructura manda: TEC-001-MX (3 digitos) o EMP-VEN-123 (3 digitos) no
    # matchean ningun patron y caen en 'desconocido', aunque tengan prefijo conocido.
    if re.match(r'^[A-Za-z]{3}-\d{4}-[A-Za-z]{2}$', codigo):
        return "producto"
    if re.match(r'^ENV-\d{4}-\d{2}-\d{2}-\d{6}$', codigo):
        return "envio"
    if re.match(r'^EMP-[A-Za-z]{3}-\d{4}$', codigo):
        return "empleado"
    if re.match(r'^FAC-[A-Za-z]-\d{6}$', codigo):
        return "factura"
    return "desconocido"


def validar_producto(codigo):
    """Valida que categoria y pais sean mayusculas (ABC-1234-MX)."""
    # detectar_tipo ya acepto minusculas; aqui exijo mayusculas con ^...$.
    return re.match(r'^[A-Z]{3}-\d{4}-[A-Z]{2}$', codigo) is not None


def validar_envio(codigo):
    """Valida los rangos de fecha del envio (anio 2020-2030, mes 01-12, dia 01-31)."""
    # El regex fija la forma; los rangos se revisan con int() para no inflar el patron.
    m = re.match(r'^ENV-(\d{4})-(\d{2})-(\d{2})-(\d{6})$', codigo)
    if not m:
        return False
    anio, mes, dia = int(m.group(1)), int(m.group(2)), int(m.group(3))
    return 2020 <= anio <= 2030 and 1 <= mes <= 12 and 1 <= dia <= 31


def validar_empleado(codigo):
    """Valida departamento permitido y numero que no empieza con 0."""
    # TODO
    return False


def validar_factura(codigo):
    """Valida que la serie sea A-E en mayuscula."""
    # TODO
    return False


def validar_codigo(codigo):
    """Detecta el tipo y aplica la validacion estricta. Retorna (tipo, es_valido)."""
    tipo = detectar_tipo(codigo)
    if tipo == "producto":
        return tipo, validar_producto(codigo)
    elif tipo == "envio":
        return tipo, validar_envio(codigo)
    elif tipo == "empleado":
        return tipo, validar_empleado(codigo)
    elif tipo == "factura":
        return tipo, validar_factura(codigo)
    else:
        return "desconocido", False


def main():
    # CSV a stdout: encabezado y una linea por cada codigo no vacio de stdin.
    print("codigo,tipo,valido")
    for linea in sys.stdin:
        codigo = linea.strip()
        if not codigo:
            continue
        tipo, es_valido = validar_codigo(codigo)
        print(f"{codigo},{tipo},{'VALIDO' if es_valido else 'INVALIDO'}")


if __name__ == "__main__":
    main()
