import random
import os
import csv
import networkx as nx

# Configuration
m = 10  # Number of binary numbers in each set
n = 8  # Number of bits in a binary number
o = 25000 # Number of sets

project_root = os.path.dirname(os.path.dirname(__file__))
input_dir = os.path.join(project_root, 'datasets', 'input_sets')
output_dir = os.path.join(project_root, 'datasets', 'output_sets')

# Create directories if they do not exist
os.makedirs(input_dir, exist_ok=True)
os.makedirs(output_dir, exist_ok=True)

for k in range(o):
  # Generate random binary numbers
  binary_numbers = [random.getrandbits(n) for _ in range(m)]

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

  # Write input binary numbers to a CSV file
  input_file = os.path.join(input_dir, 'input_binary_number_set_' + str(k) + '.csv')    
  with open(input_file, 'w', newline='') as f:
    writer = csv.writer(f)
    for num in binary_numbers:
      writer.writerow([f'{num:0{n}b}'])


  # Write arranged binary numbers to a CSV file
  output_file = os.path.join(output_dir, 'output_binary_number_set_' + str(k) + '.csv') 
  with open(output_file, 'w', newline='') as f:
    writer = csv.writer(f)
    for num in arranged_numbers:
      writer.writerow([f'{num:0{n}b}'])

print('-------------------------[ Test Case Optimizer ]------------------------- \n')
print('Creating', o ,'sets of', m , 'random binary numbers', 'containing', n , 'bits each...... \n')

print(f'Input numbers saved to {'/dataset/input_sets'}')
print(f'Arranged numbers saved to {'/dataset/output_sets'}')

print('------------------------------------------------------------------------- \n')