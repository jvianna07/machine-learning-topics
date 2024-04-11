import numpy as np
from basic_stats.normalize import reescale, gaussian
from basic_stats.stats import arithmetic_mean, std_dev, median

idades = [28,18,49,18,21,22,19,34]
internacoes = [2,4,2,20,1,3,6,2]
# X=[-0.08,  0.24, -0.08,  2.8,  -0.24,  0.08,  0.56, -0.08]
X=[ 0.6,  -0.32,  2.55, -0.32, -0.05,  0.05, -0.23,  1.16]

print(std_dev(X))
# print(np.array(
#     reescale(idades, 18,49)
# ).round(2)
# )

# print(median(idades))
# print(np.array(
#     gaussian(idades)
# ).round(2)
# )