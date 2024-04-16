import numpy as np
import pandas as pd
from basic_stats.normalize import reescale, gaussian
from basic_stats.stats import arithmetic_mean, std_dev, median, var_X, mad_X
from basic_stats.histogram import Histogram

df= pd.read_csv("../../Listas/Lista02/iris.csv")
# print(df.head())


# petallength'
X = df[df.columns[2]]

print("Variancia", var_X(X))
print("Desvio Padrao", std_dev(X))














# colesterol = np.array([140,160,168,180,180,180,180,184,185,190,
#                        190,192,192,196,200,200,200,205,205,208,
#                        214,214,220,220,225,230,240,260,280,315])

# X = np.array(
#     [1, 3, 2, 3, 2, 2, 0, 1, 0, 0, 3, 0, 2, 3, 2, 2, 3, 3, 0, 3, 2, 0])
# # hist = Histogram(colesterol)

# hist = Histogram(X, 6, 2)

# # print(hist.frequency_table())

# # print("Amplitude:", hist.amplitude)
# # print("Largura: ", hist.class_width)
# # hist.show("blue", 45)
# print('media:', arithmetic_mean(X))

# print('variancia:', var_X(X))

# print('desv padrao:', std_dev(X))

# print('desv media:', mad_X(X))
