import math
import numpy as np
import matplotlib.pyplot as plt

class Animal:
    def __init__(self, name, mammal, size):
        self.name = name
        self.mammal = mammal
        self.size = size * 2 - 1
    
    def to_vector(self):
        return (self.mammal, self.size)
    
    def norm(self):
        return math.sqrt(self.mammal ** 2 + self.size ** 2)
    
    def normalize(self):
        norm = self.norm()
        return (self.mammal / norm, self.size / norm)
    
def center(self, mean):
    return (self.mammal - mean[0], self.size - mean[1])
    
def mean(vectors):
    vec_sum = [0, 0]
    count = 0
    for vector in vectors:
        vec_sum[0] += vector[0]
        vec_sum[1] += vector[1]
        count += 1
    return (vec_sum[0] / count, vec_sum[1] / count)

def scalar_product(vec1, vec2):
    return vec1[0] * vec2[0] + vec1[1] * vec2[1]

def add(vec1, vec2):
    return (vec1[0] + vec2[0], vec1[1] + vec2[1])

def sub(vec1, vec2):
    return (vec1[0] - vec2[0], vec1[1] - vec2[1])

def norm(vector):
    return math.sqrt(vector[0] ** 2 + vector[1] ** 2)

def normalize(vector):
    _norm = norm(vector)
    return (vector[0] / _norm, vector[1] / _norm)

# Tiere
# Elefant, Giraffe, Löwe, Panther, Hund, Ratte, Maus, Walhai,
# Thunfisch, Forelle, Clownfisch, Hering, Seepferdchen

# Merkmale
# Säugetier, Größe

animals = [
    Animal("Elefant",       1, 0.94),
    Animal("Giraffe",       1, 0.86),
    Animal("Löwe",          1, 0.75),
    Animal("Panther",       1, 0.71),
    Animal("Hund",          1, 0.63),
    Animal("Ratte",         1, 0.34),
    Animal("Maus",          1, 0.11),
    Animal("Walhai",       -1, 1.00),
    Animal("Thunfisch",    -1, 0.77),
    Animal("Forelle",      -1, 0.56),
    Animal("Clownfisch",   -1, 0.28),
    Animal("Hering",       -1, 0.40),
    Animal("Seepferdchen", -1, 0.01),
]

# die Maus verhält sich zum Elefanten wie der Clownfisch zum ...
elefant_v = animals[0].to_vector()
mouse_v = animals[6].to_vector()
d_v = sub(elefant_v, mouse_v)

clownfish_v = animals[-3].to_vector()
new_v = add(clownfish_v, d_v)

best_fit = (-1, -1)
for i in range(len(animals)):
    similarity = scalar_product(new_v, animals[i].to_vector())
    if similarity > best_fit[1]:
        best_fit = (i, similarity)

print("Die Maus verhält sich zum Elefanten wie der Clownfisch zum ...")
print(animals[best_fit[0]].name)

mean_v = mean([animal.to_vector() for animal in animals])
# animal 1, 2, similarity
best_fit = (-1, -1, -1)
similarity_list = []
embeddings = []
for i in range(len(animals)):
    embeddings.append(
        normalize(sub(animals[i].to_vector(), mean_v))
    )
    for j in range(i + 1, len(animals)):
        similarity = scalar_product(
            normalize(sub(animals[i].to_vector(), mean_v)), 
            normalize(sub(animals[j].to_vector(), mean_v))
        )
        similarity_list.append((i, j, similarity))

similarity_list.sort(key=lambda x: x[2])
for similarity in similarity_list:
    print(animals[similarity[0]].name, animals[similarity[1]].name, similarity[2])


V = np.array(embeddings)
origin = np.zeros((2, len(V)))  # Origin at (0,0) for all vectors

# Create the figure and axis
fig, ax = plt.subplots(figsize=(6,6))

# Draw the quiver plot
ax.quiver(*origin, V[:,0], V[:,1], color="gray", scale=2)

# Add labels near the arrow tips
for i, (x, y) in enumerate(V):
    ax.text(x, y, f'{animals[i].name}', fontsize=12, color='black', ha='left', va='bottom')

# Draw a unit circle
unit_circle = plt.Circle((0, 0), 1, color='red', fill=False, linestyle='dashed', linewidth=1.5)
ax.add_patch(unit_circle)

# Set limits and labels
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
ax.axhline(0, color='black', linewidth=0.5)
ax.axvline(0, color='black', linewidth=0.5)
ax.set_aspect('equal')  # Ensure the aspect ratio is equal
ax.grid(True, linestyle='--')
ax.set_title("Quiver Plot with Unit Circle")

plt.show()