import numpy as np
matrix4 = np.ones((10, 10))
matrix4[0, :] = 0
matrix4[-1, :] = 0
matrix4[:, 0] = 0
matrix4[:, -1] = 0
print(matrix4)