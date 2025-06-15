import random

from utils.Colors import VERDE, VERMELHO


def listToString(lst):
    return str(lst).replace('[', '').replace(']', '').replace("'", '').replace(',', ' e')


def temSegundoTurno(candidatos):
    votos_maiores = sorted(candidatos.values(), reverse=True)

    candidatos_maiores_votos = []
    candidatos_2 = candidatos.copy()
    for maior_voto in votos_maiores:
        # Se minha lista já tiver os 2 candidatos de maior voto já pode parar.
        if len(candidatos_maiores_votos) == 2:
            break
        for candidato, votos in candidatos.items():
            if candidatos_2.get(candidato) is not None and votos == maior_voto:
                candidatos_maiores_votos.append(candidato)
                candidatos_2.pop(candidato)
                break

    print(f'{VERMELHO("Nenhum Candidato")} possui a condição de vitória necessaria ({VERDE('50% dos votos válidos')}).')
    print(f'O {VERDE('ganhador')} vai ser definido por um segundo turno entre os dois Candidatos com mais votos.({VERDE(listToString(candidatos_maiores_votos))})')

    # Limpando candidatos para ficarem somente os dos segundo turno.
    candidatos.clear()
    while True:
        for candidato in candidatos_maiores_votos:
            candidatos[candidato] = int(
                input(f"Digite a quantidade de {VERDE('votos')} do {VERDE(candidato)} no segundo turno: "))
            while candidatos[candidato] < 0:
                print('Quantidade de {} invalida! Não existe uma quantidade {} de {}.'
                      .format(VERMELHO('votos'), VERMELHO('negativa'), VERMELHO('votos')))
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
