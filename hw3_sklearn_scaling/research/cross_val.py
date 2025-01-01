import numpy as np
import typing
from collections import defaultdict


def kfold_split(num_objects: int,
                num_folds: int) -> list[tuple[np.ndarray, np.ndarray]]:
    """Split [0, 1, ..., num_objects - 1] into equal num_folds folds
       (last fold can be longer) and returns num_folds train-val
       pairs of indexes.

    Parameters:
    num_objects: number of objects in train set
    num_folds: number of folds for cross-validation split

    Returns:
    list of length num_folds, where i-th element of list
    contains tuple of 2 numpy arrays, he 1st numpy array
    contains all indexes without i-th fold while the 2nd
    one contains i-th fold
    """

    fold_size = num_objects // num_folds
    last_fold_size = num_objects % num_folds + fold_size
    indexes = np.arange(num_objects)

    current_shift = 0
    fold_index = list()
    for i in range(num_folds - 1):
        index = indexes[current_shift:current_shift + fold_size]
        current_shift += fold_size
        fold_index.append(index)
    index = indexes[current_shift:current_shift + last_fold_size]
    fold_index.append(index)

    folds = list()
    for i in range(num_folds):
        validation = fold_index[i]
        train = np.concatenate([fold_index[j] for j in range(num_folds) if j != i])
        folds.append((train, validation))

    return folds


def knn_cv_score(X: np.ndarray, y: np.ndarray, parameters: dict[str, list],
                 score_function: callable,
                 folds: list[tuple[np.ndarray, np.ndarray]],
                 knn_class: object) -> dict[str, float]:
    """Takes train data, counts cross-validation score over
    grid of parameters (all possible parameters combinations)

    Parameters:
    X: train set
    y: train labels
    parameters: dict with keys from
        {n_neighbors, metrics, weights, normalizers}, values of type list,
        parameters['normalizers'] contains tuples (normalizer, normalizer_name)
        see parameters example in your jupyter notebook

    score_function: function with input (y_true, y_predict)
        which outputs score metric
    folds: output of kfold_split
    knn_class: class of knn model to fit

    Returns:
    dict: key - tuple of (normalizer_name, n_neighbors, metric, weight),
    value - mean score over all folds
    """

    scores = dict()

    for normalizer, normalizer_name in parameters['normalizers']:
        for n_neighbors in parameters['n_neighbors']:
            for metric in parameters['metrics']:
                for weight in parameters['weights']:
                    knn = knn_class(n_neighbors=n_neighbors, metric=metric, weights=weight)
                    fold_score = list()

                    for train, validation in folds:
                        X_train, y_train = X[train], y[train]
                        X_validation, y_validation = X[validation], y[validation]

                        if normalizer:
                            normalizer.fit(X_train)
                        X_train_scalled = normalizer.transform(X_train) if normalizer else X_train
                        X_validation_scalled = normalizer.transform(X_validation) if normalizer else X_validation

                        knn.fit(X_train_scalled, y_train)
                        y_predict = knn.predict(X_validation_scalled)

                        current_score = score_function(y_validation, y_predict)
                        fold_score.append(current_score)

                    score_mean = np.mean(fold_score)
                    scores[(normalizer_name, n_neighbors, metric, weight)] = score_mean

    return scores
