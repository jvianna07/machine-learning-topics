import numpy as np
import math


# Cálculo de média
def arithmetic_mean (X):
    n = len(X)
    soma=0
    for i in X:
        soma+=i
    
    return soma/n



# Cálculo de mediana
def median(X):
    X=np.sort(X)
    n=len(X)
    if n % 2 == 0:
        i=int(n/2)
        return (X[i-1]+X[i])/2
    else:
        i=int(n/2)
        return X[i]



# Cálculo da variância
def var_X(X):
    X=np.array(X)
    V=0
    muu=arithmetic_mean(X)
    for i in X:
        V+=((i-muu)**2)
    return V/(len(X))



# Cálculo do desvio padrão
def std_dev(X):
    return math.sqrt(var_X(X))



# Cálculo da moda
def mode(X):
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
    k = len(X) * p
    if isinstance(k, float):
        if k.is_integer():
            k = int(k)
            return((X[k-1]+X[k])/2)
        else:
            k = math.ceil(k)
            return(X[k-1])
    else:
        return "p must be a float number between [0;1]"
