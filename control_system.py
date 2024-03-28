import numpy as np
from math_methods import MS

def create_system():
    n = 3  # size of invertible matrix I wish to generate
    while(True):
        A = np.random.rand(n, n)
        mx = np.sum(np.abs(A), axis=1)
        np.fill_diagonal(A, mx)
        if np.linalg.eigh(A)[0][0] > 1 and np.linalg.eigh(A)[0][1] > 1 and np.linalg.eigh(A)[0][2] >1:
            break
    U = np.array([[1, 1, 1], [-1, 1, 1], [1, -1, 1], [1, 1, -1], [-1, -1, 1], [-1, 1, -1], [1, -1, -1], [-1, -1, -1]])
    # рандомить пока собств вектор не станет >1
    X = np.dot(-np.linalg.inv(A), U.T)
    # X = MS(np.dot(np.linalg.inv(A),X).T, U)
    N = 4 #количество шагов
    for i in range(N):
        X = MS(np.dot(np.linalg.inv(A), X).T, U).T
    res = X.T
    return res