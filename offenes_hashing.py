from random import randint
from math import ceil

from matplotlib import pyplot as plt

def generate_key():
    return randint(10 ** 0 + 1, 10 ** 6 - 1)

def hash_func(y_i, L):
    return y_i % L

def s_linear(j):
    return j

def s_quadr(j):
    return ceil(j/2)**2 * (-1)**j

def add_to_table(hash_table, key, hash_func, s_func):
    initial_hash = hash_func(key, L)
    hash_val = initial_hash
    tries = 1
    while hash_table[hash_val] != None:
        hash_val = (initial_hash - s_func(tries)) % L
        tries += 1
        # print(tries)
    hash_table[hash_val] = key
    return tries - 1 # return number of calls to s(j)

element_count = 4900

# create empty table
hash_table_linear = [None for i in range(5000)]
L = len(hash_table_linear)

keys = []
tries = 0
for i in range(element_count):
    key = generate_key()
    keys.append(key)
    tries += add_to_table(hash_table_linear, key, hash_func, s_linear)

for key in keys:
    assert(key in hash_table_linear)

print("Aufrufe der Sondierungsfunktion linear: " + str(tries))


hash_table_quadr = [None for i in range(5000)]
L = len(hash_table_quadr)

keys = []
tries = 0
for i in range(element_count):
    key = generate_key()
    keys.append(key)
    tries += add_to_table(hash_table_quadr, key, hash_func, s_quadr)

for key in keys:
    assert(key in hash_table_quadr)

print("Aufrufe der Sondierungsfunktion quadratisch: " + str(tries))


plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.imshow([[1 if slot is not None else 0 for slot in hash_table_linear]], cmap="Greys", aspect="auto")
plt.title("Lineare Sondierung - Belegung")
plt.xlabel("Index der Tabelle")
plt.yticks([])
# plt.ylabel("Belegung")

plt.subplot(1, 2, 2)
plt.imshow([[1 if slot is not None else 0 for slot in hash_table_quadr]], cmap="Greys", aspect="auto")
plt.title("Quadratische Sondierung - Belegung")
plt.xlabel("Index der Tabelle")
plt.yticks([])
# plt.ylabel("Belegung")

plt.tight_layout()
plt.show()
