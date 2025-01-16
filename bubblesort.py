from random import randint
from time import perf_counter_ns
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
import numpy as np

def Bubblesort(array):
    # Bubblesort sortiert Datensätze wie folgt:
    # Für jedes Element findet ein Durchlauf statt.
    # In jedem Durchlauf wird das jeweils größte Element im unsortierten Teil der Liste gesucht 
    # und an das Ende des unsortierten Teils verschoben.
    # Der sortierte Teil am Ende der Liste ist Anfang 0 Element lang
    # und wächst mit jedem Durchlauf um 1.
    # Jedem Durchlauf werden alle benachbarten Element im unsortierten Teil der Liste 
    # von nacheinander von vorne nach hinten verglichen und vertauscht, falls 
    # das Nachfolgeelement größer ist als das Vorgängerelement.

    # Pseudocode
    # for i in 0..array_length
    #    for j in 0..(array_length - i - 1)
    #        if array[j] > array[j + 1]
    #            array.swap(j, j+1)
    #        endif       
    #    endfor
    # endfor
    
    for i in range(len(array)):
        for j in range(len(array) - i - 1):
            if array[j + 1] < array[j]:
                array[j + 1], array[j] = array[j], array[j + 1]
    return array

def generate_dataset(length):
    """Generates a random dataset of the specified length and no duplicate elements."""
    dataset = set()
    while len(dataset) != length:
        dataset.add(randint(0, length * 10))
    dataset = list(dataset) 
    return dataset

def measure_time_ns(function, *args):
    start = perf_counter_ns()
    function(*args)
    end = perf_counter_ns()
    return end - start

# Laufzeit von Bubblesort wächst Quadratisch O(n²)
def quadratic_fit(x, a, b, c):
    return a * x * x + b * x + c

xdata = np.array([i * 1000 for i in range(1, 11)])
ydata = np.array([])

for length in xdata:
    duration = 0
    print("Anzahl zu sortierender Elemente:", length)
    for j in range(10):
        dataset = generate_dataset(length)
        duration += measure_time_ns(Bubblesort, dataset)
    duration /= 10
    ydata = np.append(ydata, duration)

plt.plot(xdata, ydata, label='Daten')
popt, pcov = curve_fit(quadratic_fit, xdata, ydata)
plt.plot(xdata, quadratic_fit(xdata, *popt), label='Fit: y = %5.3f * x² + %5.3f * x + %5.3f' % tuple(popt))

plt.xlabel('x (Länge des Datensatzes)')
plt.ylabel('y in Nanosekunden')
plt.legend()
plt.show()