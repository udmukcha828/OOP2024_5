import numpy as np
import time


# 1. Поэлементные операции с массивами

# Создание массивов
x = np.random.random(size=10**6)
y = np.random.random(size=10**6)

# Поэлементная сумма, разность, произведение и частное с помощью цикла
def sum_loop(x, y):
  result = np.zeros_like(x)
  for i in range(len(x)):
    result[i] = x[i] + y[i]
  return result

def difference_loop(x, y):
  result = np.zeros_like(x)
  for i in range(len(x)):
    result[i] = x[i] - y[i]
  return result

def product_loop(x, y):
  result = np.zeros_like(x)
  for i in range(len(x)):
    result[i] = x[i] * y[i]
  return result

def quotient_loop(x, y):
  result = np.zeros_like(x)
  for i in range(len(x)):
    result[i] = x[i] / y[i]
  return result

# Поэлементные операции с помощью операторов +, ∗, −, /
def sum_operators(x, y):
  return x + y

def difference_operators(x, y):
  return x - y

def product_operators(x, y):
  return x * y

def quotient_operators(x, y):
  return x / y

# Замеры времени
print("Сумма (цикл):", end=" ")
start_time = time.time()
sum_loop(x, y)
end_time = time.time()
elapsed_time = end_time - start_time
print(elapsed_time)

print("Сумма (операторы):", end=" ")
start_time = time.time()
sum_operators(x, y)
end_time = time.time()
elapsed_time = end_time - start_time
print(elapsed_time)

print("Разность (цикл):", end=" ")
start_time = time.time()
difference_loop(x, y)
end_time = time.time()
elapsed_time = end_time - start_time
print(elapsed_time)

print("Разность (операторы):", end=" ")
start_time = time.time()
difference_operators(x, y)
end_time = time.time()
elapsed_time = end_time - start_time
print(elapsed_time)

print("Произведение (цикл):", end=" ")
start_time = time.time()
product_loop(x, y)
end_time = time.time()
elapsed_time = end_time - start_time
print(elapsed_time)

print("Произведение (операторы):", end=" ")
start_time = time.time()
product_operators(x, y)
end_time = time.time()
elapsed_time = end_time - start_time
print(elapsed_time)

print("Частное (цикл):", end=" ")
start_time = time.time()
quotient_loop(x, y)
end_time = time.time()
elapsed_time = end_time - start_time
print(elapsed_time)

print("Частное (операторы):", end=" ")
start_time = time.time()
quotient_operators(x, y)
end_time = time.time()
elapsed_time = end_time - start_time
print(elapsed_time)

# 2. Использование нескольких ядер процессора для np.dot
print("nСкалярное умножение np.dot(x, y):")
start_time = time.time()
np.dot(x, y)
end_time = time.time()
elapsed_time = end_time - start_time
print(elapsed_time)

# Проверка загрузки процессора (требует отдельного мониторинга)
# Используйте диспетчер задач или мониторинг системы для проверки загрузки процессора

# 3. Максимальный и минимальный элементы массива
print("nМаксимальный элемент (np.max):", end=" ")
start_time = time.time()
np.max(x)
end_time = time.time()
elapsed_time = end_time - start_time
print(elapsed_time)
print("Максимальный элемент (max):", end=" ")
start_time = time.time()
max(x)
end_time = time.time()
elapsed_time = end_time - start_time
print(elapsed_time)

print("Минимальный элемент (np.min):", end=" ")
start_time = time.time()
np.min(x)
end_time = time.time()
elapsed_time = end_time - start_time
print(elapsed_time)
print("Минимальный элемент (min):", end=" ")
start_time = time.time()
min(x)
end_time = time.time()
elapsed_time = end_time - start_time
print(elapsed_time)

# 4. Эмпирические математическое ожидание и дисперсия
print("nМатематическое ожидание x:", np.mean(x))
print("Дисперсия x:", np.var(x))
print("Математическое ожидание y:", np.mean(y))
print("Дисперсия y:", np.var(y))

# 5. Количество элементов, удовлетворяющих условиям
print("nКоличество элементов x < 0:", np.sum(x < 0))
print("Количество элементов x > 1:", np.sum(x > 1))
print("Количество элементов x > 1.5:", np.sum(x > 1.5))

# 6. Элементы из отрезка [0, 1/2] в массиве y
print("nЭлементы y из отрезка [0, 1/2]:", y[(y >= 0) & (y <= 0.5)])

# 7. Вывод массивов в формате CSV
np.savetxt("data.csv", np.column_stack((x, y)), delimiter=",", fmt="%.6f")
