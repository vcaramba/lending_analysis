import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

def plot_correlation(data):
    fig, ax = plt.subplots(figsize=(60, 60))
    sns.set(font_scale=10)
    correlation_matrix = data.corr(min_periods=1)
    sns.heatmap(correlation_matrix, ax=ax, cmap="plasma", fmt="d")
    ax.set_ylabel('')
    ax.set_xlabel('')
    plt.show()

def get_highly_correlated_vars(df_in):
    lower_bound = -0.8
    upper_bound = 0.8
    corr_matrix = df_in.corr(min_periods=1).abs()

    upper = corr_matrix.where(np.triu(np.ones(corr_matrix.shape), k=1).astype(np.bool))

    # Find indices of feature columns with correlation greater than 0.80
    features_above_max = [column for column in upper.columns if any(upper[column] > upper_bound)]

    # Find indices of feature columns with correlation less than -0.8
    features_below_min = [column for column in upper.columns if any(upper[column] < lower_bound)]
    features_to_drop = features_above_max + features_below_min

    return features_to_drop