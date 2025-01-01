import numpy as np


def get_part_of_array(X: np.ndarray) -> np.ndarray:
    """
    X - двумерный массив размера n x m. Гарантируется что m >= 500
    Вернуть: двумерный массив, состоящий из каждого 4го элемента по оси размерности n 
    и c 120 по 500 c шагом 5 по оси размерности m
    """
    return X[0:len(X):4, 120:500:5]

def sum_non_neg_diag(X: np.ndarray) -> int:
    """
    Вернуть  сумму неотрицательных элементов на диагонали прямоугольной матрицы X. 
    Если неотрицательных элементов на диагонали нет, то вернуть -1
    """
    diagonal = X.diagonal()
    return np.sum(diagonal[diagonal >= 0]) if np.sum(diagonal) >= 0 else -1


def replace_values(X: np.ndarray) -> np.ndarray:
    """
    X - двумерный массив вещественных чисел размера n x m.
    По каждому столбцу нужно почитать среднее значение M.
    В каждом столбце отдельно заменить: значения, которые < 0.25M или > 1.5M на -1
    Вернуть: двумерный массив, копию от X, с измененными значениями по правилу выше
    """
    x_copy = X.copy()
    column_mean = np.mean(X, axis=0)
    x_copy[(x_copy < 0.25 * column_mean) | (x_copy > 1.5 * column_mean)] = -1
    return x_copy
