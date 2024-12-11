import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import re

def calculate_mean_time(time_str):
    if pd.isnull(time_str):
        return np.nan
    match = re.findall(r'\d+', time_str)
    if len(match) == 2:
        return (int(match[0]) + int(match[1])) / 2
    return np.nan

def plot_numerical_histograms(df, numerical_columns, bins_list, kde=False):
    num_cols = 2
    num_rows = (len(numerical_columns) + 1) // num_cols

    fig, axes = plt.subplots(num_rows, num_cols, figsize=(15, num_rows * 5))
    axes = axes.flatten()

    for i, col in enumerate(numerical_columns):
        bins = bins_list[i] if i < len(bins_list) else 10
        sns.histplot(data=df, x=col, bins=bins, kde=kde, ax=axes[i])
        axes[i].set_title(f'Histograma de {col}')
        axes[i].set_xlabel(col)
        axes[i].set_ylabel('Frecuencia')

    # Remove any unused subplots
    for j in range(i + 1, len(axes)):
        fig.delaxes(axes[j])

    plt.tight_layout()
    plt.show()