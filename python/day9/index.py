#%%
import numpy as np

with open('input.txt') as f:
    data = [list(l.strip()) for l in f.readlines()]
data = np.array(data, dtype=np.int)

# %% P1
padded = np.pad(data, 1, constant_values=11)
dyplus = (padded[1:,:] - padded[:-1,:])[:-1,1:-1] >= 0
dymin = (padded[:-1,:] - padded[1:,:])[1:,1:-1] >= 0
dxplus = (padded[:,1:] - padded[:,:-1])[1:-1,:-1] >= 0
dxmin = (padded[:,:-1] - padded[:,1:])[1:-1,1:] >= 0

low_points = ~(dxplus | dxmin | dyplus | dymin)
low_points = data[low_points]
risk_score = (low_points + 1).sum()
print(risk_score)
# %% p2
idx_low = np.nonzero(~(dxplus | dxmin | dyplus | dymin))
max_y, max_x = data.shape
def find_basin_size(low_y, low_x):
    points_in_basin = set([(low_y,low_x)])
    to_be_checked = points_in_basin.copy()
    to_be_checked_next = set()
    while len(to_be_checked) > 0:
        for y, x in to_be_checked:
            for dy,dx in [(1,0), (-1,0), (0,1), (0,-1)]:
                pos = (y+dy, x+dx)
                if pos[1] >= max_x or pos[1] < 0: continue
                if pos[0] >= max_y or pos[0] < 0: continue
                if data[pos[0], pos[1]] >= 9: continue
                if pos in to_be_checked or pos in points_in_basin: continue
                points_in_basin.add(pos)
                to_be_checked_next.add(pos)
        to_be_checked = to_be_checked_next
        to_be_checked_next = set()
    basin_size = len(points_in_basin)
    return basin_size

basin_sizes = [find_basin_size(low_y, low_x) for low_y, low_x in zip(idx_low[0], idx_low[1])]
top_3_basins = sorted(basin_sizes, reverse=True)[:3]
product_top_3 = np.prod(top_3_basins)
print(product_top_3)
    


# %%
