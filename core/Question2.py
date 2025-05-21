"""
2. Escreva um algoritmo que leia três números inteiros e imprima o resultado da seguinte equação: 3 * X + 4 * Y + Z. • Onde:
X: o maior número dos 3 digitados.
Y: o menor número dos 3 digitados.
Z: o número que não é nem maior e nem menor.
"""
maiorNumero = int(input('Digite o primeiro número:'))
numeroDoMeio = maiorNumero
menorNumero = maiorNumero
#TODO: Checar com a professora se pode usar o 'continue'
for i in range(0, 2):
    n = int(input(f'Digite o {'segundo' if i == 0 else 'terceiro'} número:'))
    if n > maiorNumero:
        numeroDoMeio = maiorNumero
        maiorNumero = n
        continue
    if n < menorNumero:
        numeroDoMeio = menorNumero
        menorNumero = n
        continue
    numeroDoMeio = n

print('-'*40)
print('Maior número:', maiorNumero)
print('Número do meio:', numeroDoMeio)
print('Menor número:', menorNumero)
print(f'Equação: (3 * {maiorNumero}) + (4 * {menorNumero}) + {numeroDoMeio} = {3 * maiorNumero + 4 * menorNumero + numeroDoMeio}')
print('-'*40)
