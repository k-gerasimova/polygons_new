import numpy as np
#import pandas as pd
import openpyxl
import warnings
from matplotlib import pyplot as plt
from math_methods import Hausdorff_d
from control_system import create_system
from draw import print_3D
import algorytms as a

#x_sup - многогранник, в котором убираются вершины
#x_1 - многогранник, в который убираются вершины

epsilon = 0.03 #доли диаметра
y = create_system()

#res = Algo(y_2, y)


res=a.Algo_2(y, epsilon)
#sred = np.append(sred, [dp / (epss * 2)], axis = 0)
    #ax.plot(k, dp / (epss * 2), color = 'blue')
print_3D(res)
print_3D(y)
plt.show()