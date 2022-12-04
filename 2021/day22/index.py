# %%
from collections import Counter


with open('input.txt') as f:
    data = [x.strip() for x in f.readlines()]


def parse_instruction(x: str):
    direction, interval = x.split(' ')
    direction = direction == 'on'
    interval = interval.split(',')
    interval = [[int(c) for c in s.split('=')[1].split('..')]
                for s in interval]
    return (direction, interval)


instructions = list(map(parse_instruction, data))
# %% Part 1

cubes = dict()
for direction, region in instructions:
    [[x0, x1], [y0, y1], [z0, z1]] = region
    x0 = max(x0, -50)
    y0 = max(y0, -50)
    z0 = max(z0, -50)
    x1 = min(x1, 50)
    y1 = min(y1, 50)
    z1 = min(z1, 50)
    for xx in range(x0, x1+1):
        for yy in range(y0, y1+1):
            for zz in range(z0, z1+1):
                cubes[(xx, yy, zz)] = direction
sum(cubes.values())
# %% Part 2

def get_overlap(c1, c2):
    sx = max(c1[0][0], c2[0][0])
    ex = min(c1[1][0], c2[1][0])
    sy = max(c1[0][1], c2[0][1])
    ey = min(c1[1][1], c2[1][1])
    sz = max(c1[0][2], c2[0][2])
    ez = min(c1[1][2], c2[1][2])
    if sx > ex or sy > ey or sz > ez:
        return
    overlap = ((sx, sy, sz),
               (ex, ey, ez))
    return overlap

def vol_of_cube(cube):
    lengths = [abs(b-a)+1 for a, b in zip(*cube)]
    vol = 1
    for length in lengths:
        vol *= length
    return vol

cubes = Counter()
for direction, region in instructions:
    update = Counter()   
    new_cube = ((region[0][0], region[1][0], region[2][0]),
            (region[0][1], region[1][1], region[2][1]))
    for cube, sign in cubes.items():
        overlap = get_overlap(new_cube, cube)
        if overlap:
            update[overlap] -= sign
    if direction is True:
        update[new_cube] += direction
    cubes.update(update)

sum(sign * vol_of_cube(cube) for cube, sign in cubes.items())

# %%
