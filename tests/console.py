import random
import networkx as nx

# Generate random binary numbers
m = 5
n = 4
binary_numbers = [random.getrandbits(n) for _ in range(m)]

print('---------------------[ Input ]--------------------- \n')

for num in binary_numbers:
    print(f'{num:0{n}b}')

# Function to calculate Hamming distance
def hamming_distance(a, b):
    return bin(a ^ b).count('1')

# Create a complete graph with Hamming distances as weights
G = nx.complete_graph(m)
for i in range(m):
    for j in range(i + 1, m):
        G[i][j]['weight'] = hamming_distance(binary_numbers[i], binary_numbers[j])

# Find the minimum spanning tree (MST)
mst = nx.minimum_spanning_tree(G)

# Extract a Hamiltonian path using DFS
path = list(nx.dfs_preorder_nodes(mst))

# Arrange binary numbers based on the Hamiltonian path
arranged_numbers = [binary_numbers[i] for i in path]

# Print the arranged binary numbers
print('---------------------[ Output ]--------------------- \n') 

for num in arranged_numbers:
    print(f'{num:0{n}b}')
