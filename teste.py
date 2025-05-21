import random
# Definindo o dicionário de candidatos e votos
c1 = 1
c2 = 1
c3 = 1
c4 = 1

candidatos = {"Candidato 1": c1,"Candidato 2": c2,"Candidato 3": c3,"Candidato 4": c4}

# Encontrando o maior número de votos
maior_voto = max(candidatos.values())

# Criando uma lista dos candidatos que têm o maior número de votos
candidatos_maiores_votos = [candidato for candidato, votos in candidatos.items() if votos == maior_voto]

# Verificando se há mais de um candidato com o maior número de votos
if len(candidatos_maiores_votos) > 1:
    # Escolhendo um vencedor aleatório entre os candidatos com o maior número de votos
    sorteado = random.choice(candidatos_maiores_votos)
    print(f'O ganhador sorteado foi \033[1;32m{sorteado}\033[0;0m!')
else:
    print(f'O ganhador foi o único candidato com o maior número de votos: \033[1;32m{candidatos_maiores_votos[0]}\033[0;0m')