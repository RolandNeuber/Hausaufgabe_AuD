mod_eq = [
# x = y (mod m)
#    y  m
    (1, 9), 
    (2, 8), 
    (0, 7)
]

mm = 1
ai = [1 for _ in mod_eq]
for _, m in mod_eq:
    mm *= m

i = 0
for _, m in mod_eq:
    ai[i] = mm / m
    i += 1

mod_ai = [a % m for a, (_, m) in zip(ai, mod_eq)]

# print(ai)
# print(mod_ai)

x = []
for mod_a, (_, m) in zip(mod_ai, mod_eq):
    xi = 1
    while mod_a * xi % m != 1:
        xi += 1
    x.append(xi)

# print(x)

xx = 0
for (m, _), a, x in zip(mod_eq, ai, x):
    xx += m * a * x
xx %= mm
xx = round(xx)

print(xx)