RESET = '\033[0m'


def reset():
    return RESET


def VERDE(str):
    return f'\033[1;32m{str}{reset()}'


def VERMELHO(str):
    return f'\033[31m{str}{reset()}'
