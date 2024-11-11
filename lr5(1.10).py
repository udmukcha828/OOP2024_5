import numpy as np
number = 3.14
vector3 = np.array([1, 2, 3, 4, 5])
closest_element = vector3[np.argmin(np.abs(vector3 - number))]
print(closest_element)