# %%
import numpy as np
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
unknown_scanners = {i: scanner for i, scanner in enumerate(scanners)}
known_scanners = {0: set([tuple(x) for x in unknown_scanners.pop(0)])}
not_matching_scanners = set()
scanner_locations = [np.array([0,0,0])]

def find_scanners_match(ks, us, nm, sl, oo = orientation_options):
    dot = np.dot
    number_of_comparisons = 0
    for i, unknown_beacons in us.items():
        for ii, known_beacons in ks.items():
            if (i, ii) in nm: continue
            found_a_match = False
            for orientation_option in oo:
                rotated_unknowns = dot(unknown_beacons, orientation_option)
                for known_beacon in known_beacons:
                    for unknown in rotated_unknowns:
                        number_of_comparisons += 1
                        diff = unknown - known_beacon
                        translated_unknowns = rotated_unknowns - diff

                        translated_unknowns = set([tuple(x) for x in translated_unknowns])
                        if len(translated_unknowns & known_beacons) >= 12:
                            print("number of comparisons: ", number_of_comparisons)
                            found_a_match = True
                            ks[i] = translated_unknowns
                            del us[i]
                            scanner_location = np.array(-diff)
                            sl.append(scanner_location)
                            return
            if not found_a_match: nm.add((i, ii))
    


while len(unknown_scanners) > 0:
    find_scanners_match(known_scanners, unknown_scanners, not_matching_scanners, scanner_locations)
    print(len(unknown_scanners))

all_beacons = set()
for beacons in known_scanners.values():
    all_beacons = all_beacons | beacons
print(len(all_beacons))

max_d = -np.inf
for loc1 in scanner_locations:
    for loc2 in scanner_locations:
        manh_d = np.sum(np.abs(loc1 - loc2))
        max_d = np.max((manh_d, max_d))
print(int(max_d))






# %%
