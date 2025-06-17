RESET = '\033[0m'  # Sequência ANSI para resetar a formatação de cores no terminal
                   # (retorna à cor padrão do terminal após aplicar cor)

def reset():
    return RESET  # Função que retorna a constante RESET (útil para reutilização)

def VERDE(str):
    # Função que aplica a cor verde (negrito) ao texto passado e reseta ao final
    return f'\033[1;32m{str}{reset()}'

def VERMELHO(str):
    # Função que aplica a cor vermelha ao texto passado e reseta ao final
    return f'\033[31m{str}{reset()}'
