import pytest
from main.main import eh_expressao_valida


@pytest.mark.parametrize("expression", [
    "2+3",
    "(2+3)*4",
    "10/2+5",
    "(1+(2*3))",
    "4*(5+6)",
    "(1+2)*3",
    "(1+5)-7",
])
def test_expressao_valida_nao_comeca_ou_termina_com_operador(expression: str):
    """Regra 3: A expressão não pode começar nem terminar com operador."""
    assert eh_expressao_valida(expression) is True, f"Esperado True para expressão válida: {expression}"


@pytest.mark.parametrize("expression", [
    "2+3-",     
    "+2+3",     
    "5+8/",     
    "10/2*",    
    "/2+3",    
    "2+3-",   
    "(1+2)*3/",
    "/(1+2)-5",
    "*(1-5-3)*8",
])
def test_expressao_invalida_comeca_ou_termina_com_operador(expression: str):
    """Regra 3: Expressões que começam ou terminam com operador devem ser inválidas."""
    assert eh_expressao_valida(expression) is False, f"Esperado False para expressão inválida: {expression}"
