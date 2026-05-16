import pytest
from calculadora import Calculadora


@pytest.fixture
def calc():
    return Calculadora()



def test_soma(calc):
    assert calc.soma(2, 3) == 5
    assert calc.soma(-7, 4) == -3
    assert calc.soma(0.1, 0.2) == pytest.approx(0.3)

def test_subtracao(calc):
    assert calc.subtracao(10, 5) == 5

def test_multiplicacao(calc):
    assert calc.multiplicacao(3, 4) == 12

def test_divisao_comum(calc):
    assert calc.divisao(10, 2) == 5


def test_varias_operacoes(calc):
    resultado = calc.soma(10.5, 4.5)
    resultado = calc.subtracao(resultado, 3)
    resultado = calc.soma(resultado, -2)
    resultado = calc.multiplicacao(resultado, 2)

    assert resultado == 20.0



def test_divisao_por_zero(calc):
    with pytest.raises(ValueError) as excinfo:
        calc.divisao(10, 0)
    assert "O divisor não pode ser zero." in str(excinfo.value)