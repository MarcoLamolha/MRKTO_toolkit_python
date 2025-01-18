import matplotlib.pyplot as plt
import seaborn as sns

def plot_distribution(df, column):
    sns.histplot(data=df, x=column)
    plt.show()