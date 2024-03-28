import numpy as np
from cvxopt import matrix, solvers
from scipy.spatial import ConvexHull

def MS(x, y):
    a = np.array([])
    Temp = np.array([np.zeros(3)])
    for i in range(len(x)):
        for j in range(len(y)):
            a = x[i] + y[j]
            Temp = np.append(Temp, [a], axis = 0)
    Temp = np.delete(Temp, 0, axis=0)
    T = ConvexHull(Temp)
    K = np.vstack((Temp[T.vertices, 0], Temp[T.vertices, 1], Temp[T.vertices, 2])).T
    return K

def Hausdorff_d(x, y):
    res = np.zeros(len(y))
    for j in range(len(y)):
        Z = x.T
        loc = y[j]
        P = matrix(np.dot(Z.T, Z).astype(float))
        P = .5 * (P + P.T)
        q = matrix(-2 * np.dot(Z.T, loc).astype(float))
        A = matrix(np.ones(len(x))).T
        b = matrix(1.0)
        G = matrix(-np.eye(len(x)))
        h = matrix(np.zeros(len(x)).reshape((len(x),)))
        solvers.options['show_progress'] = False
        sol = solvers.qp(2 * P, q, G, h, A, b)
        norm_loc = 0
        for k in range(len(loc)):
            norm_loc += loc[k] ** (2)
        res[j] = sol['primal objective'] + norm_loc
    return res

