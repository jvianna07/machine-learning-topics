import numpy as np
from basic_stats.stats import arithmetic_mean, std_dev, median


# Normaliza os valores na escala determinada 
def reescale(X: list, inf_lim = 0, sup_lim = 1) -> list:
    min_value = min(X)
    max_value = max(X)
    norm = []
    for number in X:
        norm.append(
            inf_lim + ((number - min_value)/(max_value - min_value)) * (sup_lim - inf_lim)
        )

    return norm



# Normaliza os valores na forma gaussiana
def gaussian(X: list) -> list:
    muu = arithmetic_mean(X)
    std = std_dev(X)
    norm = []

    for number in X:
        norm.append(
            (number - muu)/std
            )
        
    return norm
