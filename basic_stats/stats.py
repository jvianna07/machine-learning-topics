import numpy as np
# import math


# Cálculo de média
def arithmetic_mean (X: list) -> float:
    n = len(X)
    soma = 0
    for i in X:
        soma += i
    
    return soma/n



# Cálculo de mediana
def median(X: list) -> float:
    X = np.sort(X)
    n = len(X)
    if n % 2 == 0:
        i = int(n/2)
        return (X[i-1]+X[i])/2
    else:
        i = int(n/2)
        return X[i]



# Cálculo da variância
def var_X(X: list, biased = False) -> float:
    """Variância amostral (Unbiased) grau de liberdade n-1
    e variância populacional (Biased) grau de liberdade n
    Por padrão a função calcula variância amostral"""

    X = np.array(X)
    V = 0
    muu = arithmetic_mean(X)
    for i in X:
        V += ((i-muu)**2)

    return V/(len(X)) if biased == True else  V/(len(X)-1)



# Cálculo do desvio padrão
def std_dev(X, biased = False) -> float:
    "Por padrão calcula o desvio padrão amostral (Unbiased), n-1"
    return np.sqrt(var_X(X, True)) if biased == True else np.sqrt(var_X(X, False))



# Cálculo do desvio médio absoluto
def mad_X(X: list) -> float:
    X = np.array(X)
    muu = arithmetic_mean(X)
    deviation = X-muu

    return arithmetic_mean(np.abs(deviation))



# Cálculo da moda
def mode(X: list) -> float:
    frequencies = {}
    for i in X:
        if i in frequencies:
            frequencies[i] += 1
        else:
            frequencies[i] = 1

    mode = []
    max_freq = max(frequencies.values())
    for key, value in frequencies.items():
        if value == max_freq:
            mode.append(key)
    return mode



# Cálculo dos percentis
def percentile(X: list, p: float) -> float:
    X = np.sort(X)
    k = len(X) * p

    if isinstance(k, float):
        if k.is_integer():
            k = int(k)
            return((X[k-1]+X[k])/2)
        else:
            k = np.ceil(k)
            return(X[k-1])
        
    elif isinstance(k, int):
        return((X[k-1]+X[k])/2)
    
    else:
        return "p must be a float number between [0;1]"
