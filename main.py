# 1. Em uma eleição para representante de turma concorreram 4 candidatos (C1, C2,
#   C3 e C4). Durante a apuração, além dos votos de cada candidato, foram apurados
#   os votos nulos e brancos.
#
#   |  1. Escreva um programa que leia a quantidade dos votos válidos de cada
#       candidato, os votos brancos e os votos nulos.
#
#   |  2. Ao final imprima o total de eleitores, a quantidade total de votos válidos, o
#       percentual de votos válidos de cada candidato e o percentual de votos
#       brancos e nulos.

import random

while True:
    # Votos válidos: É válido o voto dado diretamente a um determinado candidato ou a um partido
    print('-' * 80)
    C1 = int(input('Digite a quantia de \033[1;32mvotos\033[0;0m do \033[1;32mprimeiro\033[0;0m candidato: '))
    C2 = int(input('Digite a quantia de \033[1;32mvotos\033[0;0m do \033[1;32msegundo\033[0;0m candidato: '))
    C3 = int(input('Digite a quantia de \033[1;32mvotos\033[0;0m do \033[1;32mterceiro\033[0;0m candidato: '))
    C4 = int(input('Digite a quantia de \033[1;32mvotos\033[0;0m do \033[1;32mquarto\033[0;0m candidato: '))
    print('-' * 80)

    # Sanitizando a entrada de votos, só pode ser >= 0.
    if C1 < 0 or C2 < 0 or C3 < 0 or C4 < 0:
        print('Quantidade de \033[31mvotos\033[0;0m invalida! Não existe uma quantidade \033[31mnegativa\033[0;0m de \033[31mvotos\033[0;0m.')

    else:
        # Como a renata nao ensinou o sys.exit() é preciso colocar tudo dentro do if-else.
        candidatos = {"Candidato 1": C1, "Candidato 2": C2, "Candidato 3": C3, "Candidato 4": C4}

        # Voto Branco: O voto em branco ocorre quando o eleitor não quer votar em nenhum candidato e ao mesmo tempo deseja anular seu voto
        # Mais uma vez sanitizando entrada de votos.
        VB = int(input('Digite a quantia de \033[1;32mvotos\033[0;0m em \033[1;32mbranco\033[0;0m:'))
        if VB < 0:
            print('Quantidade de votos brancos invalida!')

        else:
            # Voto Nulo: O voto nulo acontece quando o eleitor insere um número que não pertence a nenhum candidato ou partido político, podendo ser um erro intencional ou não.
            VN = int(input('Digite a quantia de \033[1;32mvotos\033[0;0m \033[1;32mnulos\033[0;0m:'))
            if VN < 0:
                print('Quantidade de votos nulo invalida!')

            else:
                # Esse print fecha o do fim do quarto candidato
                print('-' * 80)
                # Quantidade total de votos válidos
                VV = C1 + C2 + C3 + C4

                # Quantidade total de eleitores
                total = C1 + C2 + C3 + C4 + VB + VN

                # Calculando a porcentagem de votos de cada candidato e de brancos e nulos.
                porC1 = round(C1 / VV * 100, 2)
                porC2 = round(C2 / VV * 100, 2)
                porC3 = round(C3 / VV * 100, 2)
                porC4 = round(C4 / VV * 100, 2)
                porVB = round(VB / total * 100, 2)
                porVN = round(VN / total * 100, 2)
                break


# Ganhador é o que tiver mais votos.
ganhador = max(candidatos, key=candidatos.get)
ganhadores = max(candidatos.values())
if (C1 > C2 and C1 == C3 and C1 > C4) or (C1 > C2 and C1 == C3 and C1 == C4) or (C1 > C2 and C1 > C3 and C1 == C4) or (C1 == C2 and C1 > C3 and C1 > C4) or  (C1 == C2 and C1 == C3 and C1 > C4) or   (C1 == C2 and C1 > C3 and C1 == C4) or (C2 > C1 and C2 == C3 and C2 > C4) or   (C2 > C1 and C2 == C3 and C2 == C4) or (C2 > C1 and C2 > C3 and C2 == C4) or   (C2 == C1 and C2 > C3 and C2 > C4) or (C2 == C1 and C2 == C3 and C2 > C4) or   (C2 == C1 and C2 > C3 and C2 == C4) or  (C3 > C1 and C3 == C2 and C3 > C4) or (C3 > C1 and C3 == C2 and C3 == C4) or (C3 > C1 and C3 > C2 and C3 == C4) or (C3 == C1 and C3 > C2 and C3 > C4) or (C3 == C1 and C3 == C2 and C3 > C4) or (C3 == C1 and C3 > C2 and C3 == C4) or (C4 > C1 and C4 == C2 and C4 == C3) or (C4 > C1 and C4 == C2 and C4 > C3) or (C4 > C1 and C4 > C2 and C4 == C3) or(C4 == C1 and C4 > C2 and C4 > C3) or (C4 == C1 and C4 == C2 and C4 > C3) or (C4 == C1 and C4 > C2 and C4 == C3) or (C4 == C2 and C4 > C1 and C4 > C3) or (C4 == C2 and C4 == C1 and C4 > C3) or   (C4 == C2 and C4 > C1 and C4 == C3) or (C1 == C2 == C3 == C4):

    print('O total de eleitores foi {}, a quantidade total de votos validos foi {}.\n'.format(total, VV),
    '\nO \033[1;32mcandidato 1\033[0;0m recebeu \033[1;32m{}%\033[0;0m dos \033[1;32mvotos\033[0;0m válidos.'.format(porC1),
    '\nO \033[1;32mcandidato 2\033[0;0m recebeu \033[1;32m{}%\033[0;0m dos \033[1;32mvotos\033[0;0m válidos.'.format(porC2),
    '\nO \033[1;32mcandidato 3\033[0;0m recebeu \033[1;32m{}%\033[0;0m dos \033[1;32mvotos\033[0;0m válidos.'.format(porC3),
    '\nO \033[1;32mcandidato 4\033[0;0m recebeu \033[1;32m{}%\033[0;0m dos \033[1;32mvotos\033[0;0m válidos.'.format(porC4),
    '\n\n\033[1;32m{}%\033[0;0m dos eleitores votaram em \033[1;32mbranco\033[0;0m'.format(porVB),
    '\n\033[1;32m{}%\033[0;0m dos eleitores votaram \033[1;32mnulo\033[0;0m'.format(porVN)
    )
    print('-' * 80)


    # Encontrando o maior número de votos
    maior_voto = max(candidatos.values())

    # Criando uma lista dos candidatos que têm o maior número de votos
    candidatos_maiores_votos = [candidato for candidato, votos in candidatos.items() if votos == maior_voto]
    print(f'Tivemos um empate,\033[1;32m{candidatos_maiores_votos}\033[0;0m tiveram a mesma quantidade de votos (\033[1;32m{maior_voto}\033[0;0m). O \033[1;32mganhador\033[0;0m vai ser definido por um segundo turno.\n')
    print('-' * 80)
    segundo_turno = {}
    for candidato in candidatos_maiores_votos:
        votos_segundo_turno = int(input(f"Digite a quantidade de \033[1;32mvotos\033[0;0m do \033[1;32m{candidato}\033[0;0m no segundo turno: "))
        segundo_turno[candidato] = votos_segundo_turno

        # Descobre o ganhador do segundo turno
    ganhador = max(segundo_turno, key=segundo_turno.get)
    total_segundo_turno = sum(segundo_turno.values())
    porcentagem = [(voto/ total_segundo_turno) * 100 for voto in segundo_turno.values()]
    print('-' * 80)
    print(f"O \033[1;32mvencedor\033[0;0m do segundo turno foi \033[1;32m{ganhador}\033[0;0m com \033[1;32m{segundo_turno[ganhador]}\033[0;0m votos no segundo turno.")

    print('-' * 80)
    print(f'O \033[1;32mtotal\033[0;0m de eleitores do segundo turno foi \033[1;32m{total_segundo_turno}\033[0;0m.\n')
    for i, candidato in enumerate(segundo_turno):
        print(f'O \033[1;32m{candidato}\033[0;0m recebeu  \033[1;32m{round(porcentagem[i], 2)}%\033[0;0m dos \033[1;32mvotos totais\033[0;0m no segundo turno.')
    print('-' * 80)


else:
    print('O candidato \033[1;32mvencedor\033[0;0m foi {}!'.format(ganhador))

    print('-' * 80)
    print('O total de eleitores foi {}, a quantidade total de votos validos foi {}.\n'.format(total, VV),

    '\nO candidato 1 recebeu {}% dos votos válidos.'.format(porC1),
    '\nO candidato 2 recebeu {}% dos votos válidos.'.format(porC2),
    '\nO candidato 3 recebeu {}% dos votos válidos.'.format(porC3),
    '\nO candidato 4 recebeu {}% dos votos válidos.'.format(porC4),

    '\n\n{}% dos eleitores votaram em branco'.format(porVB),
    '\n{}% dos eleitores votaram nulo'.format(porVN)
    )
    print('-' * 80)
