import numpy as np


def are_multisets_equal(x: np.ndarray, y: np.ndarray) -> bool:
    """
    Проверить, задают ли два вектора одно и то же мультимножество.
    """
    values1, counts1 = np.unique(x, return_counts=True)
    values2, counts2 = np.unique(y, return_counts=True)
    return np.array_equal(values1, values2) and np.array_equal(counts1, counts2)


def max_prod_mod_3(x: np.ndarray) -> int:
    """
    Вернуть максимальное прозведение соседних элементов в массиве x, 
    таких что хотя бы один множитель в произведении делится на 3.
    Если таких произведений нет, то вернуть -1.
    """
    products = x[:-1] * x[1:]
    divisible_by_3 = (x[:-1] % 3 == 0) | (x[1:] % 3 == 0)
    products_divisible_by_3 = products[divisible_by_3]
    return np.max(products_divisible_by_3) if len(products_divisible_by_3) else -1


def convert_image(image: np.ndarray, weights: np.ndarray) -> np.ndarray:
    """
    Сложить каналы изображения с указанными весами.
    """
    result = np.tensordot(image, weights, axes=([2], [0]))
    return result


def rle_scalar(x: np.ndarray, y: np.ndarray) -> int:
    """
    Найти скалярное произведение между векторами x и y, заданными в формате RLE.
    В случае несовпадения длин векторов вернуть -1.
    """
    x_decoded = np.repeat(x[:, 0], x[:, 1])
    y_decoded = np.repeat(y[:, 0], y[:, 1])
    if len(x_decoded) != len(y_decoded):
        return -1
    return np.dot(x_decoded, y_decoded)


def cosine_distance(X: np.ndarray, Y: np.ndarray) -> np.ndarray:
    """
    Вычислить матрицу косинусных расстояний между объектами X и Y.
    В случае равенства хотя бы одно из двух векторов 0, косинусное расстояние считать равным 1.
    """
    dot_product = np.dot(X, Y.T)
    magnitude_X = np.linalg.norm(X, axis=1)[:, None]
    magnitude_Y = np.linalg.norm(Y, axis=1)[None, :]
    result = dot_product / (magnitude_X * magnitude_Y)
    result[(magnitude_X == 0) | (magnitude_Y == 0)] = 1
    return result