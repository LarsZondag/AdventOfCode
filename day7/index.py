# %%
from typing import Counter
import numpy as np
with open('input.txt') as f:
    positions = [int(x) for x in f.read().strip().split(',')]
positions = np.array(positions)
# %% P1
aligning_pos = np.median(positions)
fuel = np.sum(np.abs(positions - aligning_pos), dtype=np.int)
print(fuel)
# %% P2
def fuel_calc(p, x): return np.sum(np.abs(x-p) + np.square(x-p))/2


aligning_pos = np.median(positions)
current_fuel = fuel_calc(positions, aligning_pos)
fuel_pos_plus_1 = fuel_calc(positions, aligning_pos+1)
fuel_pos_minus_1 = fuel_calc(positions, aligning_pos-1)
step = 1 if fuel_pos_minus_1 > fuel_pos_plus_1 else -1
nextfuel = fuel_calc(positions, aligning_pos + step)

while nextfuel < current_fuel:
    aligning_pos += 1
    current_fuel = nextfuel
    nextfuel = fuel_calc(positions, aligning_pos + step)
print(int(aligning_pos), int(current_fuel))


# %%
