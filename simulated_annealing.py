from copy import deepcopy
from math import sqrt, exp
from random import random, randint
import numpy as np
import matplotlib.pyplot as plt

def target_func(order, vertices_x, vertices_y):
    d = 0
    point1 = (vertices_x[order[0]], vertices_y[order[0]])
    for i in order[1:] + [order[0]]:
        point2 = (vertices_x[i], vertices_y[i])
        d += dist(point1, point2)
        point1 = point2
    return d

def dist(point1, point2):
    return sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)

def swap_points(order):
    a = randint(0, len(order) - 1)
    b = randint(0, len(order) - 1)
    while b == a:
        b = randint(0, len(order) - 1)
    order[a], order[b] = order[b], order[a]

def prob_distr(d_E, T):
    return exp(-d_E / T)

point_count = 15

vertices_x = np.array([(random() * 40) for _ in range(point_count)])
vertices_y = np.array([(random() * 40) for _ in range(point_count)])

T_0 = 10
k_max = 100000
decay = 0.01

T = T_0
current_order = [i for i in range(point_count)]
best_order = deepcopy(current_order)
E_0 = target_func(best_order, vertices_x, vertices_y)

for k in range(k_max):
    new_order = deepcopy(current_order)
    swap_points(new_order)
    E_1 = target_func(new_order, vertices_x, vertices_y)
    d_E = E_1 - E_0
    if d_E < 0:
        current_order = deepcopy(new_order)
        best_order = deepcopy(new_order)
        E_0 = E_1
    elif prob_distr(d_E, T) > random():
        current_order = deepcopy(new_order)
        E_0 = E_1
    T = T_0 / (1 + k * decay)

ordered_x = [vertices_x[i] for i in best_order] + [vertices_x[best_order[0]]]
ordered_y = [vertices_y[i] for i in best_order] + [vertices_y[best_order[0]]]

plt.plot(ordered_x, ordered_y, '.')
plt.plot(ordered_x, ordered_y)
plt.show()
