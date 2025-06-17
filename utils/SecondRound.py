import random  # Usado para desempate (empate no segundo turno é resolvido por sorteio)

# Importa funções para colorir texto no terminal (verde e vermelho)
from utils.Colors import VERDE, VERMELHO


# Converte uma lista em string, removendo colchetes e formatando com "e"
def listToString(lst):
    return str(lst).replace('[', '').replace(']', '').replace("'", '').replace(',', ' e')


# Função para tratar o segundo turno da eleição
def temSegundoTurno(candidatos):
    # Ordena os votos do maior para o menor
    votos_maiores = sorted(candidatos.values(), reverse=True)

    candidatos_maiores_votos = []  # Lista para armazenar os dois candidatos mais votados
    candidatos_2 = candidatos.copy()  # Cópia auxiliar do dicionário de candidatos

    # Percorre os votos em ordem decrescente para encontrar os dois com maior votação
    for maior_voto in votos_maiores:
        if len(candidatos_maiores_votos) == 2:
            break  # Já encontrou os dois, pode parar
        for candidato, votos in candidatos.items():
            # Verifica se esse candidato ainda está disponível e tem esse número de votos
            if candidatos_2.get(candidato) is not None and votos == maior_voto:
                candidatos_maiores_votos.append(candidato)
                candidatos_2.pop(candidato)  # Remove da cópia para evitar repetição
                break

    # Mensagem informando que ninguém teve mais de 50% dos votos válidos
    print(f'{VERMELHO("Nenhum Candidato")} possui a condição de vitória necessaria ({VERDE("50% dos votos válidos")}).')
    print(f'O {VERDE("ganhador")} vai ser definido por um segundo turno entre os dois Candidatos com mais votos.({VERDE(listToString(candidatos_maiores_votos))})')

    # Limpa o dicionário original e o prepara apenas com os dois candidatos do segundo turno
    candidatos.clear()

    # Loop para garantir que os votos do segundo turno são válidos
    while True:
        for candidato in candidatos_maiores_votos:
            # Solicita votos para cada candidato do segundo turno
            candidatos[candidato] = int(
                input(f"Digite a quantidade de {VERDE('votos')} do {VERDE(candidato)} no segundo turno: "))

            # Validação: votos não podem ser negativos
            while candidatos[candidato] < 0:
                print('Quantidade de {} invalida! Não existe uma quantidade {} de {}.'
                      .format(VERMELHO('votos'), VERMELHO('negativa'), VERMELHO('votos')))
                candidatos[candidato] = int(
                    input(f"Digite a quantidade de {VERDE('votos')} do {VERDE(candidato)} no segundo turno: "))

        # Validação: precisa haver pelo menos 1 voto
        if sum(candidatos.values()) > 0:
            break
        print('Quantidade de {} invalida! Não houve eleitores com {}. '
              .format(VERMELHO("votos"), VERMELHO("votos validos")))

    print('-' * 170)  # linha separadora

    # Determina o ganhador com base na maior quantidade de votos
    ganhador = max(candidatos, key=candidatos.get)
    total_votos_candidatos = sum(candidatos.values())  # Total de votos válidos no segundo turno
    porcentagem = [(voto / total_votos_candidatos) * 100 for voto in candidatos.values()]  # Lista com as porcentagens

    # Verifica se há empate entre os mais votados
    maior_voto_candidatos = max(candidatos.values())
    empatados = [candidato for candidato, votos in candidatos.items() if votos == maior_voto_candidatos]

    if len(empatados) > 1:
        # Mensagem e critério de desempate por idade fictícia (sorteio usado como simulação)
        print(f'O segundo turno ficou {VERMELHO("empatado")}')
        print(
            f'Segundo o {VERDE("Artigo 110")} do {VERDE("Código Eleitoral")}. O critério a ser utilizado nos casos de {VERDE("empate")} é a {VERDE("idade")} com o candidato mais {VERDE("velho")} recebendo {VERDE("prioridade")}.')

        # Sorteia o ganhador entre os empatados (representando o mais velho)
        ganhador = random.choice(empatados)
        print(f'Nesse caso, o {VERDE("ganhador")} dessa eleição será o {VERDE(ganhador)}, visto que ele é o mais {VERDE("velho")} entre os {VERDE(listToString(empatados))}.')
    else:
        # Caso normal: há um vencedor com mais votos
        print(f"O {VERDE('vencedor')} do segundo turno foi o {VERDE(ganhador)} com {VERDE(candidatos[ganhador])} votos no segundo turno.")

    print('-' * 170)  # linha separadora

    # Mostra o total de eleitores que votaram no segundo turno
    print(f'O {VERDE("total de eleitores")} do segundo turno foi {VERDE(total_votos_candidatos)}')

    # Mostra as porcentagens para cada candidato
    for i, candidato in enumerate(candidatos):
        print(f'O {VERDE(candidato)} recebeu {VERDE(round(porcentagem[i], 2))}{VERDE("%")} dos {VERDE("votos totais")} no segundo turno.')

    print('-' * 170)  # linha separadora
