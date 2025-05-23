# ANSI escape codes for text formatting
RESET = '\033[0m'


def reset():
    return RESET

def VERDE(str):
    return f'\033[1;32m{str}{reset()}'


def VERMELHO(str):
    return f'\033[31m{str}{reset()}'


def AZUL(str):
    return f'\033[1;34m{str}{reset()}'


def AMARILLO(str):
    return f'\033[1;33m{str}{reset()}'


def MAGENTA(str):
    return f'\033[1;35m{str}{reset()}'


def CYAN(str):
    return f'\033[1;36m{str}{reset()}'
