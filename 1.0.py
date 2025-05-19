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

bet = str(input('Você quer apostar?(Sim/Não) ')).strip().upper()
estaApostando = False
# TODO: Melhorar o texto das aposta
if bet == 'SIM' or bet == 'S':
    print('Apostas ativada.')
    estaApostando = True
elif bet == 'NÃO' or bet == 'NAO' or bet == 'N':
    print('Apostas desativada.')
else:
    print('Opção inválida, usando padrão: Não.')

# TODO: Esse comentario de baixo acho que ta no local incorreto.

# Votos válidos: É válido o voto dado diretamente a um determinado candidato ou a um partido
print('-' * 80)
C1 = int(input('Digite a quantia de votos do primeiro candidato:'))
C2 = int(input('Digite a quantia de votos do segundo candidato:'))
C3 = int(input('Digite a quantia de votos do terceiro candidato:'))
C4 = int(input('Digite a quantia de votos do quarto candidato:'))
print('-' * 80)

# Sanitizando a entrada de votos, só pode ser >= 0.
if C1 < 0 or C2 < 0 or C3 < 0 or C4 < 0:
    # TODO: Tem alguns acentos faltando, precisa ser ajustado gramaticamente.
    print('Quantidade de votos invalida! Não existe uma quantidade negativa de votos.')
else:
    # Como a renata nao ensinou o sys.exit() é preciso colocar tudo dentro do if-else.

    candidatos = {"Candidato 1": C1, "Candidato 2": C2, "Candidato 3": C3, "Candidato 4": C4}

    # Voto Branco: O voto em branco ocorre quando o eleitor não quer votar em nenhum candidato e ao mesmo tempo deseja anular seu voto
    VB = int(input('Digite a quantia de votos em branco:'))
    # Mais uma vez sanitizando entrada de votos.
    if VB < 0:
        # TODO: Tem alguns acentos faltando, precisa ser ajustado gramaticamente.
        print('Quantidade de votos brancos invalida!')
    else:
        # Voto Nulo: O voto nulo acontece quando o eleitor insere um número que não pertence a nenhum candidato ou partido político, podendo ser um erro intencional ou não.
        VN = int(input('Digite a quantia de votos nulos:'))
        if VN < 0:
            # TODO: Tem alguns acentos faltando, precisa ser ajustado gramaticamente.
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

            # Ganhador é o que tiver mais votos.
            ganhador = max(candidatos, key=candidatos.get)

            if estaApostando:
                ale1 = round(random.uniform(0.5, 0.8), 2)
                ale2 = round(random.uniform(0.5, 0.8), 2)
                ale3 = round(random.uniform(0.5, 0.8), 2)
                ale4 = round(random.uniform(0.5, 0.8), 2)

                if C1 != 0:
                    odd1 = round(100 / porC1 * ale1, 2)
                else:
                    odd1 = round(100 / (porC1 + 0.01 * VV), 2)
                if C2 != 0:
                    odd2 = round(100 / porC2 * ale2, 2)
                else:
                    odd2 = round(100 / (porC2 + 0.01 * VV), 2)
                if C3 != 0:
                    odd3 = round(100 / porC3 * ale3, 2)
                else:
                    odd3 = round(100 / (porC3 + 0.01 * VV), 2)
                if C4 != 0:
                    odd4 = round(100 / porC4 * ale4, 2)
                else:
                    odd4 = round(100 / (porC4 + 0.01 * VV), 2)

                print('As ODDs são as seguintes, a do Candidato 1 está ({}) a do 2 ({}) a do 3 ({}) a do 4 ({}).'
                      .format(odd1, odd2, odd3, odd4))
                aposta = -1
                while aposta == -1:
                    urChoice = int(input('Em qual candidato você quer apostar? (1/2/3/4) '))
                    if urChoice == 1:
                        suaaposta = int(input('Quanto você quer apostar? '))
                        if suaaposta <= 0:
                            print('Valor de aposto inválido!')
                            continue
                        aposta = 1
                        premio = suaaposta * odd1
                        urChoice = "Candidato 1"
                        break
                    elif urChoice == 2:
                        suaaposta = int(input('Quanto você quer apostar? '))
                        if suaaposta <= 0:
                            print('Valor de aposto inválido!')
                            continue
                        aposta = 1
                        premio = suaaposta * odd2
                        urChoice = "Candidato 2"
                        break
                    elif urChoice == 3:
                        suaaposta = int(input('Quanto você quer apostar? '))
                        if suaaposta <= 0:
                            print('Valor de aposto inválido!')
                            continue
                        aposta = 1
                        premio = suaaposta * odd3
                        urChoice = "Candidato 3"
                        break
                    elif urChoice == 4:
                        suaaposta = int(input('Quanto você quer apostar? '))
                        if suaaposta <= 0:
                            print('Valor de aposto inválido!')
                            continue

                        aposta = 1
                        premio = suaaposta * odd4
                        urChoice = "Candidato 4"
                        break
                    else:
                        print('Não entendi, você poderia repetir')
                print('Se seu candidato ganhar você receberá R${}'.format(premio))
                print('O candidato vencedor foi {}!'.format(ganhador))
                if urChoice == ganhador:
                    print('Você ganhou R${}!'.format(premio))
                else:
                    # Esse bonus de vitoria é mentira, só serve pra enganar o usuario a apostar de novo.
                    print('Você perdeu R${}'.format(suaaposta),
                          ', mas calma, tente novamente daqui a 4 anos, você receberá um bônus na vitória caso acerte da proxima vez.')
            else:
                print('O candidato vencedor foi {}!'.format(ganhador))
            print('-' * 80)
            print('O total de eleitores foi {}, a quantidade total de votos validos foi {}.\n'
                  .format(total, VV),
                  '\nO candidato 1 recebeu {}% dos votos válidos.'.format(porC1),
                  '\nO candidato 2 recebeu {}% dos votos válidos.'.format(porC2),
                  '\nO candidato 3 recebeu {}% dos votos válidos.'.format(porC3),
                  '\nO candidato 4 recebeu {}% dos votos válidos.'.format(porC4),
                  '\n\n{}% dos eleitores votarem em branco'.format(porVB),
                  '\n{}% dos eleitores votarem nulo'.format(porVN)
                  )
            print('-' * 80)