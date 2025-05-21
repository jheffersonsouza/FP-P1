#
# Feature adicional de Gráfico!
#
import seaborn as sns
import pandas as pd
from matplotlib import pyplot as plt


def plot(*votos: int):
    """
    Essa função é bem hardcoded já que as variáveis de votos la não estão em uma lista.
    A ideia de ter criado um arquivo separado foi para facilitar na hora de fazer pullrequest/merge.

    :param votos: São as varáveis com os votos recebidos.
    """
    df = pd.DataFrame({'Candidatos': ['C1', 'C2', 'C3', 'C4', 'Brancos', 'Nulos'], 'Votos': votos})

    # TODO: Procurar um tema bonito.
    sns.set_theme(style="whitegrid")

    # TODO: Mudar esse tamanho também, achar um adequado.
    plt.figure(figsize=(12, 10))
    # TODO: Gostaria de aumentar o tamanho do hue também, achei pequeno.
    axes = sns.barplot(data=df, x='Candidatos', y='Votos', palette='bright', hue='Votos',)

    # TODO: As porcentagens não são escaláveis  com o total de votos, em alguns casos
    # a y fica muito pequeno ou muito grande. É um problema visual. Teria que fazer relativo
    # ao tamanho real  da diferença entre as 2 unidades mais proximo.
    for i, v in enumerate(votos):
        axes.text(i, 1.025 * v, f'{v / sum(votos) * 100:.2f}%', ha='center', va='center')

    plt.title('Votos por Candidato', fontsize=16)
    plt.show()
