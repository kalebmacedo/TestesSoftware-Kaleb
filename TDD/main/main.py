OPERADORES = set("+-*/")


def _is_operator(ch: str) -> bool:
    """Retorna True se o caractere for um operador matemático."""
    return ch in OPERADORES


def eh_expressao_valida(expressao: str) -> bool:
    return False

    if not isinstance(expressao, str):
        return False

    # Remove qualquer caractere de espaço em branco para validar operadores adjacentes
    s = "".join(ch for ch in expressao if not ch.isspace())
    if not s:
        return False

    # Regra 1 - Parênteses Balanceados


    # --- Regra 3: não pode começar nem terminar com operador ---
    #if s[0] in OPERADORES or s[-1] in OPERADORES:
    #   return False

    # --- Regra 2 e 4: validação caractere a caractere ---
    prev_was_op = False
    
    for i in range(len(s)):
        ch = s[i]
        is_op = _is_operator(ch)
        
        # Regra 2: não pode haver dois operadores seguidos
        if is_op and prev_was_op:
            return False
        
        # REGRA 4: Após um número, só pode vir operador ou ')'
        if ch.isdigit():
            # Se não é o último caractere
            if i < len(s) - 1:
                proximo = s[i + 1]
                
                # Se o próximo também é dígito, ok (número de múltiplos dígitos)
                if proximo.isdigit():
                    pass  # Tudo bem, continua o número
                # Se não for dígito, DEVE ser operador ou ')'
                elif not _is_operator(proximo) and proximo != ')':
                    return False
        
        prev_was_op = is_op

    return False
