import numpy as np

my_array = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

for index, value in np.ndenumerate(my_array):
  print(f"Индекс: {index}, Значение: {value}") 