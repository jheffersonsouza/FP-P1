"""
1. Em uma eleição para representante de turma concorreram 4 candidatos (C1, C2,
   C3 e C4). Durante a apuração, além dos votos de cada candidato, foram apurados
   os votos nulos e brancos.

   |  1. Escreva um programa que leia a quantidade dos votos válidos de cada
       candidato, os votos brancos e os votos nulos.

   |  2. Ao final imprima o total de eleitores, a quantidade total de votos válidos, o
       percentual de votos válidos de cada candidato e o percentual de votos
       brancos e nulos.
"""
import random

from utils.Colors import VERDE, VERMELHO
from utils.Graph import plot
from utils.SecondRound import temSegundoTurno

while True:
    # Votos válidos: É válido o voto dado diretamente a um determinado candidato ou a um partido
    print('-' * 80)
    C1 = int(input('Digite a quantia de {} do {} candidato: '.format(VERDE('votos'), VERDE('primeiro'))))
    C2 = int(input('Digite a quantia de {} do {} candidato: '.format(VERDE('votos'), VERDE('segundo'))))
    C3 = int(input('Digite a quantia de {} do {} candidato: '.format(VERDE('votos'), VERDE('terceiro'))))
    C4 = int(input('Digite a quantia de {} do {} candidato: '.format(VERDE('votos'), VERDE('quarto'))))
    print('-' * 80)

    # Sanitizando a entrada de votos, só pode ser >= 0.
    if C1 < 0 or C2 < 0 or C3 < 0 or C4 < 0:
        print('Quantidade de {} invalida! Não existe uma quantidade {} de {}.'
              .format(VERMELHO('votos'), VERMELHO('negativa'), VERMELHO('votos')))

    else:
        # Como a renata nao ensinou o sys.exit() é preciso colocar tudo dentro do if-else.

        # Voto Branco: O voto em branco ocorre quando o eleitor não quer votar em nenhum candidato e ao mesmo tempo deseja anular seu voto
        # Mais uma vez sanitizando entrada de votos.
        VB = int(input('Digite a quantia de {} em {}: '.format(VERDE('votos'), VERDE('branco'))))
        if VB < 0:
            print('Quantidade de votos brancos invalida!')

        else:
            # Voto Nulo: O voto nulo acontece quando o eleitor insere um número que não pertence a nenhum candidato ou partido político, podendo ser um erro intencional ou não.
            VN = int(input('Digite a quantia de {}: '.format(VERDE('votos nulos'))))
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
                plot(C1, C2, C3, C4, VB, VN)
                break

# TODO: Atualizar os comentarios daqui e fazer uma separação de seções entre features.
# Ganhador é o que tiver mais votos.
# Esse dict serve para determinaro vencedor, que foge do enunciado principal ou seja pode usar
candidatos = {"Candidato 1": C1, "Candidato 2": C2, "Candidato 3": C3, "Candidato 4": C4}

ganhador = max(candidatos, key=candidatos.get)

print('O {} de eleitores foi {}, a quantidade {} de {} validos foi {}.\n'
      .format(VERDE('total'), VERDE(total), VERDE('total'), VERDE('votos'), VERDE(VV)))
print('O {} recebeu {} dos {} válidos.'.
      format(VERDE('Candidato 1'), VERDE(f'{porC1}%'), VERDE('votos')))
print('O {} recebeu {} dos {} válidos.'
      .format(VERDE('Candidato 2'), VERDE(f'{porC2}%'), VERDE('votos')))
print('O {} recebeu {} dos {} válidos.'
      .format(VERDE('Candidato 3'), VERDE(f'{porC3}%'), VERDE('votos')))
print('O {} recebeu {} dos {} válidos.'
      .format(VERDE('Candidato 4'), VERDE(f'{porC4}%'), VERDE('votos')))
print(' ')
print('{} dos eleitores votaram em {}.'.format(VERDE(f'{porVB}%'), VERDE('branco')))
print('{} dos eleitores votaram em {}.'.format(VERDE(f'{porVN}%'), VERDE('nulo')))
print('-' * 80)

# Conforme o TSE se o candidato com a maior quantidade de votos não tiver pelo menos 50% dos votos válidos haverá segundo turno.
if max(candidatos.values())/VV < VV/2:
    temSegundoTurno(candidatos)
else:
    print('O candidato {} foi {}!'.format(VERDE('vencedor'), ganhador))
    print('-' * 80)
