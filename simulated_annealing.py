from copy import deepcopy
from math import sqrt, exp
from random import random, randint
from matplotlib import animation
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
    order[a:b] = order[a:b][::-1]

def prob_distr(d_E, T):
    return exp(-d_E / T)

point_count = 50

fig, ax = plt.subplots()
ax.set_xlim(0, 40)
ax.set_ylim(0, 40)
line, = ax.plot([], [], 'o-', lw=2)

vertices_x = np.array([(random() * 40) for _ in range(point_count)])
vertices_y = np.array([(random() * 40) for _ in range(point_count)])

current_order = [i for i in range(point_count)]
all_orders = [deepcopy(current_order)]  # Store all orders for animation

def update(frame):
    """Update function for animation."""
    x_vals = vertices_x  # Keep all points
    y_vals = vertices_y
    order = all_orders[frame]

    ordered_x = [x_vals[i] for i in order] + [x_vals[order[0]]]
    ordered_y = [y_vals[i] for i in order] + [y_vals[order[0]]]

    line.set_data(ordered_x, ordered_y)
    return line,

T_0 = 1000
k_max = 1000000
decay = 0.999

T = T_0
best_order = deepcopy(current_order)
E_0 = target_func(best_order, vertices_x, vertices_y)
iter_without_change = 0
needed_iterations = k_max

for k in range(k_max):
    new_order = deepcopy(current_order)
    swap_points(new_order)
    E_1 = target_func(new_order, vertices_x, vertices_y)
    d_E = E_1 - E_0
    if d_E < 0:
        current_order = deepcopy(new_order)
        best_order = deepcopy(new_order)
        E_0 = E_1
        all_orders.append(deepcopy(current_order))
        iter_without_change = 0
    elif prob_distr(d_E, T) > random():
        current_order = deepcopy(new_order)
        E_0 = E_1
        all_orders.append(deepcopy(current_order))
    else:
        iter_without_change += 1
    
    if iter_without_change > 500:
        needed_iterations = k
        break
    T *= decay
    
print("needed iterations: " + str(needed_iterations))
print("final temperature: " + str(T))

ani = animation.FuncAnimation(fig, update, frames=len(all_orders), interval=10, blit=True, repeat=False)
plt.show()
