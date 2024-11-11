import numpy as np
positive_numbers = np.array([1, 2, 0, 0, 4, 0])[np.array([1, 2, 0, 0, 4, 0]) > 0]
print(positive_numbers)