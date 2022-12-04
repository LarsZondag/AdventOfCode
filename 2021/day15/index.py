# %%
from collections import defaultdict
import numpy as np
from heapq import heappush, heappop
with open('input.txt') as f:
    data = [list(x) for x in (l.strip() for l in f.readlines())]
data = np.array(data, dtype=int)
# %%

def find_smallest_risk(risk_arr: np.ndarray):
    Ny, Nx = risk_arr.shape
    risks = defaultdict(lambda: np.inf)
    risks[(0,0)] = 0
    nodes_to_visit = [(0, (0, 0))]
    exit_loc = (Ny-1, Nx - 1)
    while len(nodes_to_visit) > 0:
        current_risk, (y, x) = heappop(nodes_to_visit)
        if (y, x) == exit_loc: return current_risk
        for [dy, dx] in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
            neighbor_loc = (y + dy, x + dx)

            if not (0 <= neighbor_loc[1] < Nx and 0 <= neighbor_loc[0] < Ny):
                continue

            if neighbor_loc in risks:
                continue

            current_neighbor_risk = risks[neighbor_loc]
            proposed_neighbor_risk = current_risk + risk_arr[neighbor_loc]
            if proposed_neighbor_risk < current_neighbor_risk:
                risks[neighbor_loc] = proposed_neighbor_risk
                heappush(nodes_to_visit, (proposed_neighbor_risk, neighbor_loc))
    return np.inf

# %% P1
find_smallest_risk(data)

# %% P2
Ny, Nx = data.shape
shape = np.array(data.shape) * 5
new_data = np.zeros(shape)
for i in range(5):
    for j in range(5):
        tile = 1 + (data + i + j - 1) % 9
        new_data[j*Ny: (j+1)*Ny, i*Nx: (i+1)*Nx] = tile
find_smallest_risk(new_data)
# %%
