from shapely.geometry import Polygon, LineString, Point
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from scipy.spatial import ConvexHull

#рисование 2D
# (функция для итеративного вывода при добавлении точек)

def print_polygon(y, y_2):
    plt.figure()
    if (len(y_2)>2):
        polx = Polygon(y_2).convex_hull
        x1, y1 = polx.exterior.xy
        plt.plot(x1, y1, color='#de3163', alpha=0.7,
                 linewidth=5, solid_capstyle='round', zorder=2)
    elif (len(y_2)==2):
        polx = LineString(y_2)
        plt.plot(*polx.xy, color='#de3163', alpha=0.7,
                 linewidth=5, solid_capstyle='round', zorder=2)
    else:
        polx = Point(y_2)
        plt.plot(*polx)
    poly = Polygon(y)
    x, y = poly.exterior.xy
    plt.plot(x, y, color='#423189', alpha=0.7,
             linewidth=5, solid_capstyle='round', zorder=2)
    plt.grid(True)
    plt.show()


def print_2D(y,res):
    poly = Polygon(y).convex_hull
    polx = Polygon(res).convex_hull
    x, y = poly.exterior.xy
    x1, y1 = polx.exterior.xy

    plt.plot(x, y, color='#423189', alpha=0.7,
             linewidth=5, solid_capstyle='round', zorder=2)

    plt.plot(x1, y1, color='#de3163', alpha=0.7,
             linewidth=5, solid_capstyle='round', zorder=3)
    plt.grid(True)
    plt.show()


def print_3D(res):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection="3d")
    hull = ConvexHull(res)
    # draw the polygons of the convex hull
    for s in hull.simplices:
        tri = Poly3DCollection([res[s]])
        tri.set_color('#800080')
        tri.set_alpha(0.5)
        ax.add_collection3d(tri)
        # draw the vertices
    ax.scatter(res[:, 0], res[:, 1], res[:, 2], marker='o', color='#32144f')
