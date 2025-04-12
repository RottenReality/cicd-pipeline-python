# tests/test_calculadora.py
import pytest
import math
from app.calculadora import sumar, restar, multiplicar, dividir, potencia, modulo

def test_sumar():
    assert sumar(2, 3) == 5
    assert sumar(-1, 1) == 0
    assert sumar(0, 0) == 0

def test_restar():
    assert restar(5, 2) == 3
    assert restar(1, -1) == 2
    assert restar(0, 0) == 0

def test_multiplicar():
    assert multiplicar(2, 3) == 6
    assert multiplicar(-1, 5) == -5
    assert multiplicar(0, 10) == 0

def test_dividir():
    assert math.isclose(dividir(10, 2), 5.0, rel_tol=1e-09, abs_tol=1e-09)
    assert dividir(5, -1) == -5.0
    with pytest.raises(ZeroDivisionError):
        dividir(1, 0)

def test_potencia():
    assert potencia(2, 3) == 8
    assert potencia(-1, 5) == -1
    assert potencia(-1, 6) == 1
    assert potencia(2, 0) == 1
    assert potencia(0, 10) == 0

def test_modulo():
    assert modulo(3, 2) == 1
    assert modulo(5, -1) == 0
    assert modulo(2, 2) == 0
    assert modulo(0, 1) == 0
    with pytest.raises(ZeroDivisionError):
        modulo(1, 0)