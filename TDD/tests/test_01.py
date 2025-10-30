import pytest
from main.main import eh_expressao_valida


@pytest.mark.parametrize("expression", [
    "()()", "()", "))))",
    "((((", "(()))", "()("
])
def test_parenteses_balanceados(expression: str):
    assert eh_expressao_valida(expression) is True, f"Esperado True para expressão válida: {expression}"


@pytest.mark.parametrize("expression", [
    "(", ")()", "))))",
    "((((", "(()))", "()("  
])
def test_parenteses_desbalanceados(expression: str):
    assert eh_expressao_valida(expression) is False, f"Esperado False para expressão inválida: {expression}"
