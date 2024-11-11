import numpy as np
N = 3
vector4 = np.random.rand(10)
top_N_values = np.sort(vector4)[-N:]
print(vector4)
print(top_N_values)