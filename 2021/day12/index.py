#%%
from typing import List


with open('input.txt') as f:
    data = [l.strip().split('-') for l in f.readlines()]
data
connections = {}
for a, b in data:
    addition_to_a = set()
    addition_to_a.add(b)
    addition_to_b = set()
    addition_to_b.add(a)
    try:
        connections[a] = connections[a].union(addition_to_a)
    except:
        connections[a] = addition_to_a
    try:
        connections[b] = connections[b].union(addition_to_b)
    except:
        connections[b] = addition_to_b
nodes = [node for connection in data for node in connection]
nodes = list(set(nodes))
small_caves = [node for node in nodes if node != 'start' and node != 'end' and node.islower()]
small_caves = set(small_caves)
# %% P1

N_paths = 0
def find_path_from_node(node: str, small_caves_visited: set):
    my_connections = connections[node]
    for my_connection in my_connections:
        if my_connection in small_caves and my_connection in small_caves_visited: continue
        if my_connection == 'start': continue
        small_caves_visited_new_path = small_caves_visited.copy()
        if my_connection in small_caves: small_caves_visited_new_path.add(my_connection)
        if my_connection == 'end':
            global N_paths
            N_paths += 1
        else:
            find_path_from_node(my_connection, small_caves_visited_new_path)
find_path_from_node('start', set())
print(N_paths)

# %% P2

N_paths = 0
def find_path_from_node_P2(node: str, small_caves_visited: dict):
    my_connections = connections[node]
    for my_connection in my_connections:
        if my_connection in small_caves:
            if small_caves_visited[my_connection] >= 1:
                if 2 in small_caves_visited.values(): continue
        small_caves_visited_new_path = small_caves_visited.copy()
        if my_connection == 'start': continue
        if my_connection in small_caves: small_caves_visited_new_path[my_connection] += 1
        if my_connection == 'end':
            global N_paths
            N_paths += 1
        else:
            find_path_from_node_P2(my_connection, small_caves_visited_new_path)
small_caves_visited = {small_cave: 0 for small_cave in small_caves}
find_path_from_node_P2('start', small_caves_visited)

print(N_paths)
# %%
