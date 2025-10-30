from TDD.main.main import eh_expressao_valida

def test_02_dois_operadores_iguais_seguidos():
    invalid_exprs = ["1++2", "3--1", "5+\t+3"]
    for expr in invalid_exprs:
        assert eh_expressao_valida(expr) is False

    valid_exprs = ["1+2", "3-1", "5 +\t3"]
    for expr in valid_exprs:
        assert eh_expressao_valida(expr) is True


def test_02_operadores_diferentes_seguidos():
    invalid_exprs = ["1+*2", "4/*2", "4/\n*2"]
    for expr in invalid_exprs:
        assert eh_expressao_valida(expr) is False

    valid_exprs = ["2*3", "4/2", "4/ \n2"]
    for expr in valid_exprs:
        assert eh_expressao_valida(expr) is True


def test_02_nao_confundir_operador_seguido_com_espaco():
    valid_exprs = ["1 + 2", "3 - 1", "4 / 2"]
    for expr in valid_exprs:
        assert eh_expressao_valida(expr) is True

    invalid_exprs = ["1 +\n+ 2", "3 -\t- 1"]
    for expr in invalid_exprs:
        assert eh_expressao_valida(expr) is False


def test_02_expressoes_validas_basicas_passam():
    valid_exprs = ["1+2", "10/5", "2 - 1"]
    for expr in valid_exprs:
        assert eh_expressao_valida(expr) is True

    assert eh_expressao_valida("2-\r-1") is False


def test_02_operadores_seguidos_ignorando_qualquer_espacamento():
    invalid_exprs = ["1+\t*2", "3-\n-1", "4/\t*2"]
    for expr in invalid_exprs:
        assert eh_expressao_valida(expr) is False

    valid_exprs = ["1 +\t2", "3 -\n 1", "4/\t2"]
    for expr in valid_exprs:
        assert eh_expressao_valida(expr) is True
