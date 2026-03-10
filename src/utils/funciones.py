import re
from typing import List, Optional, Union

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns


def calculate_mean_time(time_str: str) -> float:
    """
    Calcula el tiempo promedio a partir de una cadena de texto que contiene un rango de tiempo.

    Args:
        time_str (str): Cadena de texto con el rango de tiempo (ej. "10-20 hours").

    Returns:
        float: Tiempo promedio calculado. Retorna np.nan si el valor es nulo o no contiene un rango válido.
    """
    if pd.isnull(time_str):
        return np.nan
    match = re.findall(r'\d+', str(time_str))
    if len(match) == 2:
        return (int(match[0]) + int(match[1])) / 2
    return np.nan


def plot_numerical_histograms(
    df: pd.DataFrame, numerical_columns: List[str], bins_list: List[int], kde: bool = False
) -> None:
    """
    Dibuja histogramas para múltiples columnas numéricas en un DataFrame.

    Args:
        df (pd.DataFrame): DataFrame que contiene los datos.
        numerical_columns (List[str]): Lista de nombres de columnas numéricas a graficar.
        bins_list (List[int]): Lista de número de bins correspondientes a cada columna.
        kde (bool, optional): Booleano para superponer la Curva de Estimación de Densidad del Kernel (KDE). Por defecto es False.
    """
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


def categorize_score(
    score: Union[pd.Series, np.ndarray, float], bins: List[Union[int, float]], labels: List[str]
) -> pd.Series:
    """
    Categoriza una variable continua (como una puntuación) en rangos discretos definidos.

    Args:
        score (Union[pd.Series, np.ndarray, float]): Valores a categorizar.
        bins (List[Union[int, float]]): Límites de los rangos para la categorización.
        labels (List[str]): Etiquetas asignadas a cada rango.

    Returns:
        pd.Series: Serie de pandas con los valores categorizados.
    """
    return pd.cut(score, bins=bins, labels=labels, include_lowest=True)


def plot_categorical_numerical_histograms(
    df: pd.DataFrame, categorical_columns: List[str], numerical_columns: List[str]
) -> None:
    """
    Dibuja histogramas de conteo para combinaciones de columnas categóricas y numéricas.

    Args:
        df (pd.DataFrame): DataFrame que contiene los datos.
        categorical_columns (List[str]): Nombres de las columnas categóricas.
        numerical_columns (List[str]): Nombres de las columnas numéricas (solo usado para el título de las gráficas).
    """
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


def plot_categorical_numerical_boxplots(
    df: pd.DataFrame, categorical_columns: List[str], numerical_columns: List[str]
) -> None:
    """
    Dibuja boxplots para analizar la distribución de columnas numéricas agrupadas por columnas categóricas.

    Args:
        df (pd.DataFrame): DataFrame que contiene los datos.
        categorical_columns (List[str]): Nombres de las columnas categóricas para agrupar.
        numerical_columns (List[str]): Nombres de las columnas numéricas a graficar.
    """
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


def plot_scatter(
    df: pd.DataFrame, num_col1: str, num_col2: str, cat_col: Optional[str] = None, point_size: int = 50
) -> None:
    """
    Dibuja un diagrama de dispersión entre dos columnas numéricas, opcionalmente diferenciado por una variable categórica.

    Args:
        df (pd.DataFrame): DataFrame que contiene los datos.
        num_col1 (str): Nombre de la primera columna numérica (eje X).
        num_col2 (str): Nombre de la segunda columna numérica (eje Y).
        cat_col (Optional[str], optional): Nombre de la columna categórica para colorear los puntos (hue). Por defecto es None.
        point_size (int, optional): Tamaño de los puntos en el gráfico. Por defecto es 50.
    """
    plt.figure(figsize=(10, 6))
    
    if cat_col:
        sns.scatterplot(data=df, x=num_col1, y=num_col2, hue=cat_col, s=point_size)
    else:
        sns.scatterplot(data=df, x=num_col1, y=num_col2, s=point_size)
    
    plt.title(f'Diagrama de dispersión de {num_col1} vs {num_col2}')
    plt.xlabel(num_col1)
    plt.ylabel(num_col2)
    plt.show()