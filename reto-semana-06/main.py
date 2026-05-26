import sys
import re

DEPARTAMENTOS_VALIDOS = ['VEN', 'ADM', 'TEC', 'LOG', 'RHH']
SERIES_VALIDAS = ['A', 'B', 'C', 'D', 'E']


def detectar_tipo(codigo):
    """Detecta el tipo de codigo por su estructura, no solo por el prefijo."""
    # TODO: reconocer producto/envio/empleado/factura con regex anclados
    return "desconocido"


def validar_producto(codigo):
    """Valida que categoria y pais sean mayusculas (ABC-1234-MX)."""
    # TODO
    return False


def validar_envio(codigo):
    """Valida los rangos de fecha del envio (anio 2020-2030, mes 01-12, dia 01-31)."""
    # TODO
    return False


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
