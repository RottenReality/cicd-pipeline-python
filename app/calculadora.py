"""se definen metodos de la calculadora"""


def sumar(a, b):
    """suma dos números y devuelve el resultado."""
    return a + b


def restar(a, b):
    """resta dos números y devuelve el resultado."""
    return a - b


def multiplicar(a, b):
    """multiplica dos números y devuelve el resultado."""
    return a * b


def dividir(a, b):
    """Divide dos números y devuelve el resultado."""
    if b == 0:
        raise ZeroDivisionError("No se puede dividir por cero")
    return a / b


def potencia(a, b):
    """potencia un número con el otro y devuelve el resultado."""
    return a**b


def modulo(a, b):
    """divide dos números y devuelve el residuo."""
    return a % b
