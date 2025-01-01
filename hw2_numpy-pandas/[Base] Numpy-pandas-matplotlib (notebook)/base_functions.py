from typing import List
from copy import deepcopy


def get_part_of_array(X: List[List[float]]) -> List[List[float]]:
    """
    X - двумерный массив вещественных чисел размера n x m. Гарантируется что m >= 500
    Вернуть: двумерный массив, состоящий из каждого 4го элемента по оси размерности n 
    и c 120 по 500 c шагом 5 по оси размерности m
    """
    return [X[i][120:500:5] for i in range(0, len(X), 4)]


def sum_non_neg_diag(X: List[List[int]]) -> int:
    """
    Вернуть  сумму неотрицательных элементов на диагонали прямоугольной матрицы X. 
    Если неотрицательных элементов на диагонали нет, то вернуть -1
    """
    sum = 0
    flag = False
    for i in range(min(len(X), len(X[0]))):
        if X[i][i] >= 0:
            sum += X[i][i]
            flag = True
    return sum if flag else -1


def replace_values(X: List[List[float]]) -> List[List[float]]:
    """
    X - двумерный массив вещественных чисел размера n x m.
    По каждому столбцу нужно почитать среднее значение M.
    В каждом столбце отдельно заменить: значения, которые < 0.25M или > 1.5M на -1
    Вернуть: двумерный массив, копию от X, с измененными значениями по правилу выше
    """
    x_copy = deepcopy(X)
    column_sum = [sum(x_copy[i][j] for i in range(len(x_copy))) for j in range(len(x_copy[0]))]
    column_len = len(x_copy)
    column_mean = [column_sum[i]/column_len for i in range(len(x_copy[0]))]
    for i in range(len(x_copy[0])):  # Iterate over each column
        column = [row[i] for row in x_copy]
        for j in range(len(x_copy)):
            if column[j] > 1.5 * column_mean[i] or column[j] < 0.25 * column_mean[i]:
                x_copy[j][i] = -1
    return x_copy
