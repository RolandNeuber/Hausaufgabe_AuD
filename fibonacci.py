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

print("iterativ")
for x in range(3, 31):
    print("x:", x, "y:", Fib_it(x));

print("rekursiv")
for x in range(3, 31):
    print("x:", x, "y:", Fib_rek(x));