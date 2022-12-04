# %%
import numpy as np

with open('input.txt') as f:
    data = f.read()
data = data.split(',')
data = [d.split('=')[1] for d in data]
xrange, yrange = [[int(x) for x in d.split('..')] for d in data]
# # %%
def ic_reaches_target(vx, vy, minx, maxx, miny, maxy):
    x = y = 0
    reaches_target = False
    while x <= maxx and y >= miny:
        x += vx
        y += vy
        vx = np.sign(vx) * (np.abs(vx) - 1)
        vy -= 1
        if miny <= y <= maxy:
            if minx <= x <= maxx:
                reaches_target = True
                break
    return reaches_target

#%% P1
# Probe returns to y=0 with vy = -vy_initial. 
# Maximum velocity this can be without overshooting is when
# the probe reaches the bottom of the target in 1 step
# abs(bottom) = vy_max -> maximum height is obtained as a sum of:
# 1 + 2 + ... + vy = vy * (vy + 1) / 2
print(int((yrange[0])*(yrange[0]+1)/2))


#%%
# x = v * (v + 1) / 2
# 2x = v^2 + v
# v^2 + v - 2x = 0
# a = 1, b = 1, c = -2x
# v = (-1 +- np.sqrt(1 + 8x))/2
min_x_velocity = int(np.ceil((-1 + np.sqrt(1 + 8 * np.min(xrange)))/2))
max_x_velocity = np.max(xrange)
max_y_velocity = np.abs(yrange[0]) + 1

reaching_target = 0
minx, maxx = np.min(xrange), np.max(xrange)
miny, maxy = np.min(yrange), np.max(yrange)

for vx in range(min_x_velocity, max_x_velocity + 1):
    for vy in range(yrange[0], max_y_velocity):
        if ic_reaches_target(vx, vy, minx, maxx, miny, maxy): reaching_target += 1

print(reaching_target)
# %%
