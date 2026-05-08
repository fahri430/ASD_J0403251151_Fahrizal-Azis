'''
Fahrizal Azis
J0403251151
TPL A1
'''

# 1. Definisi Node dan Hubungan Antar Node
nodes = ["Rapli", "Arizz", "Ipin", "Akbar", "Diaz"]

# List dari tuples untuk mendefinisikan hubungan (edge) dengan format: (Follower, Followed)
edges = [
    ("Rapli", "Arizz"), ("Rapli", "Ipin"),
    ("Arizz", "Ipin"),
    ("Ipin", "Rapli"),
    ("Akbar", "Arizz"),
    ("Diaz", "Akbar"), ("Diaz", "Rapli")
]

# 2. Pembuatan Adjacency List
adj_list = {node: [] for node in nodes}
for origin, destination in edges:
    adj_list[origin].append(destination)

# 3. Pembuatan Adjacency Matrix
# Inisialisasi matriks n x n dengan 0
n = len(nodes)
adj_matrix = [[0 for _ in range(n)] for _ in range(n)]

# Mapping nama node ke indeks untuk kemudahan matriks
node_indices = {node: idx for idx, node in enumerate(nodes)}

# Mengisi matriks dengan 1 untuk setiap edge
for origin, destination in edges:
    i = node_indices[origin]
    j = node_indices[destination]
    adj_matrix[i][j] = 1

# 4. Menampilkan Output Sesuai Ketentuan
print("=== 1. Nama Node ===")
print(nodes)
print("\n=== 2. Hubungan Antar Node (Edges) ===")
for origin, destination in edges:
    print(f"{origin} follows {destination}")

print("\n=== 3. Adjacency List ===")
for node, neighbors in adj_list.items():
    print(f"{node}: {neighbors}")

print("\n=== 4. Adjacency Matrix ===")
# Print header
print(f"{'':>8} " + " ".join(f"{n:>7}" for n in nodes))
for i, row in enumerate(adj_matrix):
    print(f"{nodes[i]:>8} " + " ".join(f"{val:>7}" for val in row))