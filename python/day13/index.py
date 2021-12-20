#%%
import numpy as np
with open('input.txt') as f:
    data = f.read()
dot_locations, instructions_raw = data.split('\n\n')

instructions_raw = [x for x in instructions_raw.splitlines()]
instructions = []
for instruction in instructions_raw:
    a, b = instruction.split('=')
    instructions.append((a[-1:], int(b)))

dot_locations = [ds.split(',') for ds in dot_locations.splitlines()]
dot_locations = np.array(dot_locations, dtype=int)
Nx, Ny = np.max(dot_locations, axis=0) + 1

dots = np.zeros((Ny, Nx), dtype=bool)
for dot_location in dot_locations:
    x, y = dot_location
    dots[y, x] = True

#%%
def visualize_dots(arr: np.ndarray):
    Ny, _ = arr.shape
    for y in range(Ny):
        to_print = ['█' if x else ' ' for x in arr[y, :] ]
        print("".join(to_print))

# %% P1
def fold(arr: np.ndarray, instruction):
    direction, position = instruction
    if (direction == 'y'):
        above, below = arr[:position, :].copy(), arr[position+1:, :].copy()
        flip = np.flipud
    else:
        above, below = arr[:, :position].copy(), arr[:, position+1:].copy()
        flip = np.fliplr
    
    if len(above) >= len(below):
        below.resize(above.shape)
    else:
        above.resize(below.shape)
    below = flip(below)
    return above + below

dots_after_1_fold = fold(dots.copy(), instructions[0])
print(f"P1: {np.sum(dots_after_1_fold)}")

final_dots = dots.copy()
for instruction in instructions:
    final_dots = fold(final_dots, instruction)
visualize_dots(final_dots)

# %%
