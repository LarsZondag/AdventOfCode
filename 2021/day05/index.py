# %%
import numpy as np
f = open('input.txt')
lines = f.read()
f.close()
lines = [line.split(" -> ") for line in lines.split('\n')]
lines = [[x[0].split(','), x[1].split(',')] for x in lines]
lines = np.array(lines, dtype=np.int)

# %% P1
[max_hor, max_depth] = lines.max(axis=(0, 1))

N = np.zeros((max_hor+1, max_depth+1), dtype=np.int)

for [[x1, y1], [x2, y2]] in lines:
    if x1 != x2 and y1 != y2:
        continue
    x_start = min(x1, x2)
    x_end = max(x1, x2) + 1
    y_start = min(y1, y2)
    y_end = max(y1, y2) + 1
    N[x_start:x_end, y_start:y_end] += 1
np.sum(N >= 2)
# %% P2
[max_hor, max_depth] = lines.max(axis=(0, 1))

N = np.zeros((max_hor+1, max_depth+1), dtype=np.int)

for [[x1, y1], [x2, y2]] in lines:
    x_start = min(x1, x2)
    x_end = max(x1, x2) + 1
    y_start = min(y1, y2)
    y_end = max(y1, y2) + 1
    if x1 == x2 or y1 == y2:
        N[x_start:x_end, y_start:y_end] += 1
    elif abs(x1-x2) == abs(y1-y2):
        xs = list(range(x1, x2, np.sign(x2 - x1)))
        ys = list(range(y1, y2, np.sign(y2 - y1)))
        for i in range(len(xs)):
            x = xs[i]
            y = ys[i]
            N[x, y] += 1
        N[x2, y2] += 1

np.sum(N >= 2)

# %%
