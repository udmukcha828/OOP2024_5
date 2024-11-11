import numpy as np
import imageio.v3 as iio
import matplotlib.pyplot as plt


# Функция для загрузки изображения
def load_image(file_path):
    return iio.imread(file_path)


# Функция для преобразования цветного изображения в оттенки серого
def convert_to_grayscale(image, weights=np.array([0.2126, 0.7152, 0.0722])):
    height, width, num_channels = image.shape

    # Проверка, что количество каналов совпадает с длиной вектора весов
    if num_channels != len(weights):
        raise ValueError("Количество каналов изображения должно совпадать с длиной вектора весов")

    # Умножение каждого канала на соответствующий вес и суммирование результатов
    grayscale_image = np.tensordot(image, weights, axes=([-1], [-1]))

    # Нормализуем значения
    grayscale_image = np.clip(grayscale_image, 0, 255)

    return grayscale_image.astype(np.uint8)


# Основная функция программы
if __name__ == "__main__":
    # Путь к изображению
    file_path = 'imageimage.png'

    # Загрузка изображения
    image = load_image(file_path)

    # Преобразование в оттенки серого
    result = convert_to_grayscale(image)

    # Сохранение изображения в файл
    iio.imwrite('output.png', result)
    print("Серое изображение сохранено в output.png.")

    # Показ изображения в консоли
    plt.axis('off')
    plt.imshow(result, cmap='gray')
    plt.show()
    print("до", image)
    print("после", result)