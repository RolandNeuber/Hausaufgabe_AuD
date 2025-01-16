from time import perf_counter_ns
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
import numpy as np

# Could use memoisation to improve runtime
def Fib_rek(n):
    if n == 0 or n == 1:
        return 1
    return Fib_rek(n - 1) + Fib_rek(n - 2)

def Fib_it(n):
    fib1 = 0
    fib2 = 1
    for x in range(n):
        fib = fib1 + fib2
        fib1 = fib2
        fib2 = fib
    return fib2

def measure_time_ns(function, *args):
    start = perf_counter_ns()
    function(*args)
    end = perf_counter_ns()
    return end - start

def exponential_fit(x, a, b):
    return a * b ** x

xdata = np.array([i for i in range(3, 31)])
ydata_rek = np.array([])
ydata_it = np.array([])

for x in range(3, 31):
    assert(Fib_it(x) == Fib_rek(x))

for index in xdata:
    duration_rek = 0
    duration_it = 0
    print(f"Berechung der {index}ten Fibonacci-Zahl")
    duration_rek += measure_time_ns(Fib_rek, index)
    duration_it += measure_time_ns(Fib_it, index)
    ydata_rek = np.append(ydata_rek, duration_rek)
    ydata_it = np.append(ydata_it, duration_it)

plt.plot(xdata, ydata_rek, label='Daten rekursiv')
plt.plot(xdata, ydata_it, label="Daten iterativ")
popt, pcov = curve_fit(exponential_fit, xdata, ydata_rek)
plt.plot(xdata, exponential_fit(xdata, *popt), label='Fit rekursiv: y = %5.3f * %5.3f ^ x' % tuple(popt))

plt.xlabel('x')
plt.ylabel('y in Nanosekunden')
plt.legend()
plt.show()