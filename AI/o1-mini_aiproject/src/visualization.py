import matplotlib.pyplot as plt
import seaborn as sns

def plot_distribution(data, column):
    """Plot distribution of a column."""
    sns.histplot(data[column], kde=True)
    plt.title(f'Distribution of {column}')
    plt.show()

def plot_correlation(data):
    """Plot correlation heatmap."""
    corr = data.corr()
    sns.heatmap(corr, annot=True, cmap='coolwarm')
    plt.title('Correlation Heatmap')
    plt.show()