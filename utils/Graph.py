#
# Feature adicional de Gráfico!
#

# Importa bibliotecas necessárias
import seaborn as sns                 # Biblioteca para gráficos estatísticos com estilo
import pandas as pd                   # Biblioteca para manipulação de dados em formato de tabela (DataFrame)
from matplotlib import pyplot as plt  # Biblioteca base para plotagem de gráficos em Python

# TODO: Suporta plot para o segundo turno.
# A função abaixo cria um gráfico de barras baseado nos votos passados
def plot(*votos: int):
    """
    Essa função é bem hardcoded já que as variáveis de votos não estão em uma lista.
    A ideia de ter criado um arquivo separado foi para facilitar na hora de fazer pull request/merge.

    :param votos: São as variáveis com os votos recebidos.
    """

    # Cria um DataFrame com nomes fixos de candidatos e os votos recebidos (em ordem)
    df = pd.DataFrame({
        'Candidatos': ['C1', 'C2', 'C3', 'C4', 'Brancos', 'Nulos'],
        'Votos': votos
    })

    # TODO: Procurar um tema bonito.
    # Define um tema visual (estilo do gráfico)
    sns.set_theme(style="whitegrid")

    # TODO: Mudar esse tamanho também, achar um adequado.
    # Define o tamanho da figura do gráfico
    plt.figure(figsize=(12, 10))

    # TODO: Gostaria de aumentar o tamanho do hue também, achei pequeno.
    # Cria o gráfico de barras, usando cor diferente com base no valor de 'Votos' (hue)
    axes = sns.barplot(
        data=df,
        x='Candidatos',
        y='Votos',
        palette='bright',
        hue='Votos',  # Este hue funciona, mas é redundante, pois cada valor é único
    )

    # TODO: As porcentagens não são escaláveis com o total de votos.
    # Adiciona texto acima de cada barra mostrando a porcentagem em relação ao total de votos
    for i, v in enumerate(votos):
        axes.text(
            i,                  # posição x da barra
            1.025 * v,          # posição y um pouco acima da barra
            f'{v / sum(votos) * 100:.2f}%',  # texto com porcentagem
            ha='center',  # alinhamento horizontal
        va = 'center'  # alinhamento vertical
    )

    # Adiciona título ao gráfico
    plt.title('Votos por Candidato', fontsize=16)

    # Exibe o gráfico
    plt.show()