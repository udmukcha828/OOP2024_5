import numpy as np
random_vector = np.random.rand(5, 3)
normalized_vector = (random_vector - np.mean(random_vector, axis=0)) / np.std(random_vector, axis=0)
print(random_vector)
print(normalized_vector)