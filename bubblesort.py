from random import randint
from copy import deepcopy

def Bubblesort(array):
    # Pseudocode
    # TODO
    
    for i in range(len(array)):
        for j in range(len(array) - i - 1):
            if array[j + 1] < array[j]:
                array[j + 1], array[j] = array[j], array[j + 1]
    return array

for i in range(1, 11):
    length = 1000 * i
    dataset = set()
    while len(dataset) != length:
        dataset.add(randint(0, length * 10))
    dataset = list(dataset)

    expected = deepcopy(dataset)
    expected.sort()
    assert(Bubblesort(dataset) == expected)