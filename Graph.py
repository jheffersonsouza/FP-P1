#
# Feature adicional de Gráfico!
#
import seaborn as sns
import pandas as pd
from matplotlib import pyplot as plt


def plot(*votos: int):
    candidatos = []
    for i in range(0, len(votos)):
        candidatos.append(f'C{i + 1}')

    df = pd.DataFrame({'Candidatos': candidatos, 'Votos': votos})

    # TODO: Procurar um tema bonito.
    sns.set_theme(style="whitegrid")

    plt.figure(figsize = (12, 10))
    axes = sns.barplot(data=df, x='Candidatos', y='Votos', palette='bright', hue='Votos')

    for i, v in enumerate(votos):
        axes.text(i, 1.05 * v , f'{v/sum(votos) * 100:.2f}%', ha='center', va='center')

    plt.title('Votos por Candidato', fontsize=16)
    plt.show()
