from math_methods import Hausdorff_d
import numpy as np

def return_ind(x_sup, m):
    i = -1
    for j in range(len(x_sup)):
        if (np.array_equal(m, x_sup[j])):
            i = j
    return i

def j2D(x_sup, x_1, x):
    a = Hausdorff_d(x_1, x)
    max = 0
    max_i = 0
    for i in range(len(a)):
        if (a[i]>=max and x[i] in x_sup):
            m = x[i]
            max = a[i]
            max_i = return_ind(x_sup, m)
    return np.append(x_1, [m], axis=0), np.delete(x_sup, max_i, axis=0)

#Аринин алгоритм
def Algo_1(y_sup1, y_nach, eps):

    min = 1000000
    y_sup = y_sup1
    y = y_nach

    for i in range(len(y)):
        # перебирается каждая вершина изначального массива
        for k in range(len(y_sup)):
            y_1 = np.delete(y_sup, k, axis=0)  # откуда удалять, число, откуда (по строкам)
            # удаляются все вершины по очереди, ищется минимально расстояние
            d = np.sqrt(np.abs(np.max(Hausdorff_d(y_1, y))))
            if (d < min and d <= eps):
            #if (d < min and len(y_sup) < len):
                j_min = k
                min = d
        if (min != 1000000):
            print(min, y_sup[j_min])
            y_sup = np.delete(y_sup, j_min, axis=0)
            min = 1000000
        else:
            break
    return y_sup


def Algo_2(y, epsilon):
    k = np.array([])
    dp = np.array([])
    fin = 0
    res = y
    loc, i_max, max = 0, 0, 0
    for i in range(len(y)):
        for j in range(len(y[i])):
            loc += y[i][j] ** 2
        if (loc > max):
            max = loc
            i_max = i
        loc = 0

    epss = np.sqrt(max) * epsilon
    s = 1
    y_sup = y
    y_2 = np.array([y_sup[i_max]])
    y_sup = np.delete(y_sup, i_max, axis=0)
    d = np.sqrt(np.abs(np.max(Hausdorff_d(y_2, y))))
    dp = np.append(dp, d)
    k = np.append(k, s)
    #llen = len(y_2)

    while (d >= epss and len(y_sup) != 0):
        # while (llen < 10 and len(y_sup != 0)):

        y_2, y_sup = j2D(y_sup, y_2, y)
        d = np.sqrt(np.abs(np.max(Hausdorff_d(y_2, y))))
        dp = np.append(dp, d)
        k = np.append(k, len(y_2))
        llen = len(y_2)

    res = Algo_1(y_2, y, epss)
    return res
