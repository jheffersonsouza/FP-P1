import random

from utils.Colors import VERDE, VERMELHO


def listToString(lst):
    return str(lst).replace('[', '').replace(']', '').replace("'", '').replace(',', ' e')


def temSegundoTurno(candidatos):
    # Encontrando o maior número de votos
    maior_voto = max(candidatos.values())

    # Criando uma lista dos candidatos que têm o maior número de votos
    candidatos_maiores_votos = [candidato for candidato, votos in candidatos.items() if votos == maior_voto]
    candidatos_maiores_votos = candidatos_maiores_votos[:2]

    print(
        f'Tivemos um empate, {VERDE(listToString(candidatos_maiores_votos))} tiveram a mesma quantidade de votos: {VERDE(maior_voto)}. O {VERDE('ganhador')} vai ser definido por um segundo turno.')

    # Limpando candidatos para ficarem somente os dos segundo turno.
    candidatos.clear()
    while True:
        for candidato in candidatos_maiores_votos:
            candidatos[candidato] = int(
                input(f"Digite a quantidade de {VERDE('votos')} do {VERDE(candidato)} no segundo turno: "))
            while candidatos[candidato] < 0:
                print('Quantidade de {} invalida! Não existe uma quantidade {} de {}.'
                      .format(VERMELHO('votos'),  VERMELHO('negativa'),VERMELHO('votos')))
                candidatos[candidato] = int(
                    input(f"Digite a quantidade de {VERDE('votos')} do {VERDE(candidato)} no segundo turno: "))

        if sum(candidatos.values()) > 0:
            break
        print('Quantidade de {} invalida! Não houve eleitores com {}. '
              .format(VERMELHO("votos"), VERMELHO("votos validos")))
    print('-' * 140)
    # Descobre o ganhador do segundo turno
    ganhador = max(candidatos, key=candidatos.get)
    total_votos_candidatos = sum(candidatos.values())
    porcentagem = [(voto / total_votos_candidatos) * 100 for voto in candidatos.values()]

    # Verificação de empate no segundo turno
    maior_voto_candidatos = max(candidatos.values())
    empatados = [candidato for candidato, votos in candidatos.items() if votos == maior_voto_candidatos]

    if len(empatados) > 1:
        print(f'O segundo turno ficou {VERMELHO('empatado')}')
        print(
            f'Segundo o {VERDE('Artigo 110')} do {VERDE('Código Eleitoral')}. O critério a ser utilizado nos casos de {VERDE('empate')} é a {VERDE('idade')} com o candidato mais {VERDE('velho')} recebendo {VERDE('prioridade')}.')
        ganhador = random.choice(empatados)
        print(
            f'Nesse caso, o {VERDE('ganhador')} dessa eleição será o {VERDE(ganhador)}, visto que ele é o mais {VERDE('velho')} entre os {VERDE(listToString(empatados))}.')
    else:
        print(
            f"O {VERDE('vencedor')} do segundo turno foi o {VERDE(ganhador)} com {VERDE(candidatos[ganhador])} votos no segundo turno.")

    print('-' * 140)
    print(f'O {VERDE('total de eleitores')} do segundo turno foi {VERDE(total_votos_candidatos)}')
    for i, candidato in enumerate(candidatos):
        print(
            f'O {VERDE(candidato)} recebeu {VERDE(round(porcentagem[i], 2))}{VERDE('%')} dos {VERDE('votos totais')} no segundo turno.')
    print('-' * 140)

