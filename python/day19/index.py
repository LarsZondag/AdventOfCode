# %%
import numpy as np
from numpy.lib.function_base import copy
with open('sample_input.txt') as f:
    data = f.read()
data = data.split('\n\n')
scanners = [[[int(a) for a in x.split(',')]
         for x in d.splitlines()[1:]] for d in data]

# %%
direction_options = [
    [1, 0, 0],
    [-1, 0, 0],
    [0, 1, 0],
    [0, -1, 0],
    [0, 0, 1],
    [0, 0, -1],
]
direction_options = np.array(direction_options)
orientation_options = list()
i = 0
for x in direction_options:
    for y in direction_options:
        if np.array_equal(np.abs(x), np.abs(y)):
            continue
        z = np.cross(x,y)
        
        orientation_options.append(np.array([x, y, z]))

#%%
unknown_scanners = scanners.copy()
known_beacons = set([tuple(x) for x in unknown_scanners.pop()])
scanner_locations = [np.array([0,0,0])]
while len(unknown_scanners) > 0:
    print(len(unknown_scanners))
    unknown_matched = -1
    for i, unknowns in enumerate(unknown_scanners):
        has_been_matched = False
        for orientation_option in orientation_options:
            if has_been_matched: break
            rotated_unknowns = np.dot(unknowns, orientation_option)
            for known in known_beacons:
                if has_been_matched: break
                for unknown in rotated_unknowns:
                    diff = unknown - known
                    translated_unknowns = rotated_unknowns - diff

                    translated_unknowns = set([tuple(x) for x in translated_unknowns])
                    if len(translated_unknowns & known_beacons) >= 12:
                        has_been_matched = True
                        known_beacons = known_beacons | translated_unknowns
                        unknown_matched = i
                        scanner_location = np.array(-diff)
                        scanner_locations.append(scanner_location)
                        break
        if has_been_matched: break
    if unknown_matched > -1:
        unknown_scanners.pop(unknown_matched)
print(len(known_beacons))

#%%
max_d = -np.inf
for loc1 in scanner_locations:
    for loc2 in scanner_locations:
        manh_d = np.sum(np.abs(loc1 - loc2))
        max_d = np.max((manh_d, max_d))
print(int(max_d))






# %%
