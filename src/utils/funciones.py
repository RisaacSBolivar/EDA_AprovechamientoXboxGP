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

def categorize_score(score, bins, labels):
    return pd.cut(score, bins=bins, labels=labels, include_lowest=True)

def plot_categorical_numerical_histograms(df, categorical_columns, numerical_columns):
    colors = sns.color_palette("husl", len(categorical_columns) * len(numerical_columns))
    color_idx = 0
    for cat_col in categorical_columns:
        for num_col in numerical_columns:
            plt.figure(figsize=(10, 6))
            sns.countplot(data=df, x=cat_col, color=colors[color_idx])
            plt.title(f'Histograma de {num_col} por {cat_col}')
            plt.xlabel(cat_col)
            plt.ylabel('Conteo')
            plt.ylim(0, 250)
            plt.show()
        color_idx += 1

def plot_categorical_numerical_boxplots(df, categorical_columns, numerical_columns):
    colors = sns.color_palette("husl", len(categorical_columns) * len(numerical_columns))
    color_idx = 0
    for cat_col in categorical_columns:
        for num_col in numerical_columns:
            plt.figure(figsize=(10, 6))
            sns.boxplot(x=df[cat_col], y=df[num_col], palette=[colors[color_idx]])
            plt.title(f'Boxplot de {num_col} por {cat_col}')
            plt.xlabel(cat_col)
            plt.ylabel(num_col)
            plt.xticks(rotation=45)
            plt.show()
        color_idx += 1

def plot_scatter(df, num_col1, num_col2, cat_col=None, point_size=50):
    plt.figure(figsize=(10, 6))
    
    if cat_col:
        sns.scatterplot(data=df, x=num_col1, y=num_col2, hue=cat_col, s=point_size)
    else:
        sns.scatterplot(data=df, x=num_col1, y=num_col2, s=point_size)
    
    plt.title(f'Diagrama de dispersión de {num_col1} vs {num_col2}')
    plt.xlabel(num_col1)
    plt.ylabel(num_col2)
    plt.show()