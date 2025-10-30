"""
Ciclo 4 - Regra 4: Após um número, só pode vir operador ou ')'
Desenvolvedor: [Seu nome]
"""
import pytest
from TDD.main.main import eh_expressao_valida


class TestRegra04:
    """Testes para validar que após um número só pode vir operador ou ')'"""
    
    def test_deve_aceitar_numero_seguido_de_operador(self):
        """Deve aceitar número seguido de operador (+, -, *, /)"""
        assert eh_expressao_valida("1+2") == True
        assert eh_expressao_valida("5-3") == True
        assert eh_expressao_valida("4*2") == True
        assert eh_expressao_valida("8/4") == True
    
    def test_deve_aceitar_numero_seguido_de_parentese_fechamento(self):
        """Deve aceitar número seguido de parêntese de fechamento"""
        assert eh_expressao_valida("(1+2)") == True
        assert eh_expressao_valida("(5)") == True
        assert eh_expressao_valida("((3))") == True
    
    def test_deve_rejeitar_numero_seguido_de_parentese_abertura(self):
        """Deve rejeitar número diretamente seguido de parêntese de abertura"""
        assert eh_expressao_valida("2(3+4)") == False
        assert eh_expressao_valida("5(2)") == False
    
    def test_deve_aceitar_numeros_multiplos_digitos(self):
        """Deve aceitar números com múltiplos dígitos"""
        assert eh_expressao_valida("123+456") == True
        assert eh_expressao_valida("100*200") == True
    
    def test_deve_aceitar_numero_no_final_da_expressao(self):
        """Deve aceitar número como último caractere da expressão"""
        assert eh_expressao_valida("1+2") == True
        assert eh_expressao_valida("(3*4)") == True