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
ydata = np.array([])

for x in range(3, 31):
    assert(Fib_it(x) == Fib_rek(x))

for index in xdata:
    duration = 0
    print(f"Berechung der {index}ten Fibonacci-Zahl")
    duration += measure_time_ns(Fib_rek, index)
    ydata = np.append(ydata, duration)

plt.plot(xdata, ydata, label='Daten')
popt, pcov = curve_fit(exponential_fit, xdata, ydata)
plt.plot(xdata, exponential_fit(xdata, *popt), label='Fit: a=%5.3f, b=%5.3f' % tuple(popt))

plt.xlabel('x')
plt.ylabel('y in Nanosekunden')
plt.legend()
plt.show()