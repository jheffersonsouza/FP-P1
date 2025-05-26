import random

from utils.Colors import VERDE, VERMELHO


def temSegundoTurno(candidatos):
    # Encontrando o maior número de votos
    maior_voto = max(candidatos.values())

    # Criando uma lista dos candidatos que têm o maior número de votos
    candidatos_maiores_votos = [candidato for candidato, votos in candidatos.items() if votos == maior_voto]
    candidatos_maiores_votos = candidatos_maiores_votos[:2]

    print(
        f'Tivemos um empate, {VERDE(str(candidatos_maiores_votos).replace('[', '').replace(']', '').replace("'", '').replace(',',' e'))} tiveram a mesma quantidade de votos ({VERDE(maior_voto)}). O {VERDE('ganhador')} vai ser definido por um segundo turno.')
    print('-' * 80)

    # Limpando candidatos para ficarem somente os dos segundo turno.
    candidatos.clear()
    for candidato in candidatos_maiores_votos:
        candidatos[candidato] = int(input(f"Digite a quantidade de {VERDE('votos')} do {VERDE(candidato)} no segundo turno: "))
        while candidatos[candidato] < 0:
            print('Quantidade de {} invalida! Não existe uma quantidade {} de {}.'
                  .format(VERMELHO('votos'), VERMELHO('negativa'), VERMELHO('votos')))
            candidatos[candidato] = int(input(f"Digite a quantidade de {VERDE('votos')} do {VERDE(candidato)} no segundo turno: "))

    # Descobre o ganhador do segundo turno
    ganhador = max(candidatos, key=candidatos.get)
    total_candidatos = sum(candidatos.values())
    porcentagem = [(voto / total_candidatos) * 100 for voto in candidatos.values()]

    # Verificação de empate no segundo turno
    maior_voto_candidatos = max(candidatos.values()) 
    empatados = [candidato for candidato, votos in candidatos.items() if votos == maior_voto_candidatos]

    if len(empatados) > 1:
        print('-' * 80)
        print('O segundo turno ficou \033[1;31mempatado\033[1;0m!')
        print(
            '\nSegundo o \033[1;32martigo 110\033[1;0m do \033[1;32mCódigo Eleitoral\033[1;0m: O \033[1;32mcritério\033[1;0m a ser utilizado nos casos de \031[1;32mempate\033[1;0m é a \033[1;32midade\033[1;0m, com o candidato mais \033[1;32mvelho\033[1;0m recebendo \033[1;32mprioridade\033[1;0m.')
        sorteado = random.choice(empatados)
        print(
            f'\nNesse caso, o \033[1;32mganhador\033[1;0m dessa eleição será o \033[1;32m{sorteado}\033[1;0m, visto que ele é o mais \033[1;32mvelho\033[1;0m entre os \033[1;32m{empatados}\033[1;0m.')
        print('-' * 80)
        print(
            f'O \033[1;32mtotal\033[0;0m de eleitores do segundo turno foi \033[1;32m{total_candidatos}\033[0;0m.\n')
        for i, candidato in enumerate(candidatos):
            print(
                f'O \033[1;32m{candidato}\033[0;0m recebeu  \033[1;32m{round(porcentagem[i], 2)}%\033[0;0m dos \033[1;32mvotos totais\033[0;0m no segundo turno.')
        print('-' * 80)

    else:
        print('-' * 80)
        print(
            f"O \033[1;32mvencedor\033[0;0m do segundo turno foi \033[1;32m{ganhador}\033[0;0m com \033[1;32m{candidatos[ganhador]}\033[0;0m votos no segundo turno.")

        print('-' * 80)
        print(
            f'O \033[1;32mtotal\033[0;0m de eleitores do segundo turno foi \033[1;32m{total_candidatos}\033[0;0m.\n')
        for i, candidato in enumerate(candidatos):
            print(
                f'O \033[1;32m{candidato}\033[0;0m recebeu  \033[1;32m{round(porcentagem[i], 2)}%\033[0;0m dos \033[1;32mvotos totais\033[0;0m no segundo turno.')
        print('-' * 80)

temSegundoTurno({"Candidato 1": 9, "Candidato 2": 10, "Candidato 3": 10, "Candidato 4": 10})


