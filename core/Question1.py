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
# Importação de funções de arquivos ".py" da pasta "utils".
from utils.Colors import VERDE, VERMELHO
from utils.Graph import plot
from utils.SecondRound import temSegundoTurno

# Entrada sanitizada de votos.
while True:
    # Votos válidos: É válido o voto dado diretamente a um determinado candidato ou a um partido
    print('-' * 170)  # Imprime uma linha para separação visual

    C1 = int(input('Digite a quantia de {} do {} candidato: '.format(VERDE('votos'), VERDE('primeiro'))))
    C2 = int(input('Digite a quantia de {} do {} candidato: '.format(VERDE('votos'), VERDE('segundo'))))
    C3 = int(input('Digite a quantia de {} do {} candidato: '.format(VERDE('votos'), VERDE('terceiro'))))
    C4 = int(input('Digite a quantia de {} do {} candidato: '.format(VERDE('votos'), VERDE('quarto'))))

    print('-' * 170)  # linha separadora

    # Total de Votos válidos
    VV = C1 + C2 + C3 + C4

    # Sanitizando a entrada de votos, só pode ser >= 0.
    if C1 < 0 or C2 < 0 or C3 < 0 or C4 < 0:
        print('Quantidade de {} invalida! Não existe uma quantidade {} de {}.'
              .format(VERMELHO('votos'), VERMELHO('negativa'), VERMELHO('votos')))

    # Sanitizando a entrada de votos, tem que ter pelo menos um candidato com 1 voto ou mais.
    elif VV == 0:
        print('Quantidade de {} invalida! Não houve eleitores com {}. '
              .format(VERMELHO("votos"), VERMELHO("votos validos")))

    else:
        # Como a renata não ensinou o sys.exit() é preciso colocar tudo dentro do if-else.
        # Voto Branco: O voto branco ocorre quando o eleitor não quer votar em nenhum candidato e, ao mesmo tempo, deseja anular seu voto
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
                print('-' * 170)  # linha separadora

                # Quantidade total de votos válidos
                VV = C1 + C2 + C3 + C4

                # Quantidade total de eleitores
                total = C1 + C2 + C3 + C4 + VB + VN

                # Calculando a porcentagem de votos de cada candidato e de brancos e nulos em relação aos votos validos e aos votos totais respectivamente.
                porC1 = round(C1 / VV * 100, 2)
                porC2 = round(C2 / VV * 100, 2)
                porC3 = round(C3 / VV * 100, 2)
                porC4 = round(C4 / VV * 100, 2)
                porVB = round(VB / total * 100, 2)
                porVN = round(VN / total * 100, 2)
                plot(C1, C2, C3, C4, VB, VN)
                break

# Mostrando a porcentagem de votos de cada candidato e de brancos e nulos em relação aos votos validos e aos votos totais respectivamente.
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

print(' ')  # Separar as porcentagens que usam votos validos das que usam votos totais.

print('{} dos eleitores votaram em {}.'
      .format(VERDE(f'{porVB}%'), VERDE('branco')))
print('{} dos eleitores votaram em {}.'
      .format(VERDE(f'{porVN}%'), VERDE('nulo')))

print('-' * 170)  # linha separadora

# Esse dict serve para determinar o vencedor, que foge do enunciado principal, ou seja, pode ser usado.
candidatos = {"Candidato 1": C1, "Candidato 2": C2, "Candidato 3": C3, "Candidato 4": C4}
ganhador = max(candidatos, key=candidatos.get)

# Conforme o TSE se o candidato com a maior quantidade de votos não tiver pelo menos 50% dos votos válidos haverá segundo turno.
if max(candidatos.values()) * 100 / VV < 50:
    temSegundoTurno(candidatos)

else:
    # Se houver mais do que 1 candidato com o maior número de votos, há um empate.
    # Nesse caso optamos por um segundo turno em caso desse tipo de empate.
    #Ex. 2 candidatos com X votos e o restante com 0 votos.
    if list(candidatos.values()).count(max(candidatos.values())) > 1:
        temSegundoTurno(candidatos)
    print('O candidato {} foi {}!'.format(VERDE('vencedor'), ganhador))
