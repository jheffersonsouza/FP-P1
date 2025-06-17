"""
2. Escreva um algoritmo que leia três números inteiros e imprima o resultado da seguinte equação: 3 * X + 4 * Y + Z. • Onde:
X: o maior número dos 3 digitados.
Y: o menor número dos 3 digitados.
Z: o número que não é nem maior e nem menor.
"""

print('-' * 40)  # Imprime uma linha para separação visual

# Solicita o primeiro número e assume que ele é o maior, o menor e o do meio inicialmente
maiorNumero = int(input('Digite o primeiro número:'))
numeroDoMeio = maiorNumero
menorNumero = maiorNumero

# Loop para ler os dois próximos números (totalizando 3 números)
for i in range(0, 2):
    # Solicita o segundo ou o terceiro número, dependendo da iteração
    n = int(input(f'Digite o {'segundo' if i == 0 else 'terceiro'} número:'))

    # Verifica se o novo número é maior que o atual maior
    if n > maiorNumero:
        numeroDoMeio = maiorNumero  # O antigo maior vira o número do meio
        maiorNumero = n             # Atualiza o maior número
        continue                    # Pula para a próxima iteração do loop

    # Verifica se o novo número é menor que o atual menor
    if n < menorNumero:
        numeroDoMeio = menorNumero  # O antigo menor vira o número do meio
        menorNumero = n             # Atualiza o menor número
        continue                    # Pula para a próxima iteração do loop

    # Se não for nem maior nem menor, é o número do meio
    numeroDoMeio = n

print('-' * 40)  # Linha separadora

# Exibe os números classificados
print('Maior número:', maiorNumero)
print('Número do meio:', numeroDoMeio)
print('Menor número:', menorNumero)

# Exibe a equação com os valores processados
print(f'Equação: (3 * {maiorNumero}) + (4 * {menorNumero}) + {numeroDoMeio} = {3 * maiorNumero + 4 * menorNumero + numeroDoMeio}')

print('-' * 40)  # Linha final de separação