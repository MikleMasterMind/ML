from collections import Counter
from typing import List
import math


def are_multisets_equal(x: List[int], y: List[int]) -> bool:
    """
    Проверить, задают ли два вектора одно и то же мультимножество.
    """
    return Counter(x) == Counter(y)


def max_prod_mod_3(x: List[int]) -> int:
    """
    Вернуть максимальное прозведение соседних элементов в массиве x, 
    таких что хотя бы один множитель в произведении делится на 3.
    Если таких произведений нет, то вернуть -1.
    """
    max_product = -1
    for i in range(len(x) - 1):
        if x[i] % 3 == 0 or x[i + 1] % 3 == 0:
            product = x[i] * x[i + 1]
            if product > max_product:
                max_product = product
    return max_product
    


def convert_image(image: List[List[List[float]]], weights: List[float]) -> List[List[float]]:
    """
    Сложить каналы изображения с указанными весами.
    """
    result = [[0.0 for _ in range(len(image[0]))] for _ in range(len(image))]
    for i in range(len(image)):
        for j in range(len(image[0])):
            for k in range(len(image[0][0])):
                result[i][j] += image[i][j][k] * weights[k]
    return result


def rle_scalar(x: List[List[int]], y:  List[List[int]]) -> int:
    """
    Найти скалярное произведение между векторами x и y, заданными в формате RLE.
    В случае несовпадения длин векторов вернуть -1.
    """
    x_norm = [x[i][0] for i in range(len(x)) for _ in range(x[i][1])]
    y_norm = [y[i][0] for i in range(len(y)) for _ in range(y[i][1])]
    return sum(x_norm[i] * y_norm[i] for i in range(len(x_norm))) if len(x_norm) == len(y_norm) else -1


def cosine_distance(X: List[List[float]], Y: List[List[float]]) -> List[List[float]]:
    """
    Вычислить матрицу косинусных расстояний между объектами X и Y. 
    В случае равенства хотя бы одно из двух векторов 0, косинусное расстояние считать равным 1.
    """
    result = [[0.0 for _ in range(len(Y))] for _ in range(len(X))]

    for i in range(len(X)):
        for j in range(len(Y)):
            dot_product = sum(x * y for x, y in zip(X[i], Y[j]))
            magnitude_x = math.sqrt(sum(x ** 2 for x in X[i]))
            magnitude_y = math.sqrt(sum(y ** 2 for y in Y[j]))

            if magnitude_x == 0 or magnitude_y == 0:
                result[i][j] = 1.0
            else:
                result[i][j] = dot_product / (magnitude_x * magnitude_y)

    return result