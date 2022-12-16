#%%
from numba import jit

# file = "sample.txt"
file = "input.txt"
with open(file, "r", encoding="utf-8") as f:
    data = [s[len("Sensor at "):].split(": closest beacon is at ") for s in f.read().splitlines()]

sensors = []
beacons = []
min_x, max_x = 0, 0
min_y, max_y = 0, 0
for sensor_line in data:
    string_x, string_y = sensor_line[0].split(", ")
    sensor_x = int(string_x[2:])
    sensor_y = int(string_y[2:])
    string_x, string_y = sensor_line[1].split(", ")
    beacon_x = int(string_x[2:])
    beacon_y = int(string_y[2:])

    distance = abs(sensor_x - beacon_x) + abs(sensor_y - beacon_y)
    sensors.append((sensor_x, sensor_y, distance))
    beacons.append((beacon_x, beacon_y))
    min_x = min(min_x, sensor_x - distance)
    max_x = max(max_x, sensor_x + distance)
    min_y = min(min_y, sensor_y - distance)
    max_y = max(max_y, sensor_y + distance)

#%% Part 1
y = 10 if file == "sample.txt" else 2000000

n_cannot_contain_beacon = 0

for x in range(min_x, max_x + 1):
    cannot_contain_beacon = False
    is_sensor_position = False
    is_beacon_position = False
    for (sensor_x, sensor_y, sensor_distance) in sensors:
        if x == sensor_x and y == sensor_y:
            is_sensor_position = True
            break
        distance = abs(sensor_x - x) + abs(sensor_y - y)
        if distance <= sensor_distance:
            cannot_contain_beacon = True
            break
    if is_sensor_position:
        continue
    if cannot_contain_beacon :
        is_beacon_position = any(beacon_x == x and beacon_y == y for beacon_x, beacon_y in beacons)
        if not is_beacon_position:
            n_cannot_contain_beacon += 1
    

print("Part 1: ", n_cannot_contain_beacon)


# %% Part 2
@jit
def find_beacon(start, end, sensor_data):
    for y in range(start, end + 1):
        x = 0
        while x <= end + 1:
            this_is_the_beacon = True
            for sensor_x, sensor_y, sensor_distance in sensor_data:
                distance = abs(x-sensor_x) + abs(y-sensor_y)
                if distance <= sensor_distance:
                    x = sensor_x + sensor_distance - abs(sensor_y - y) + 1
                    this_is_the_beacon = False
                    break
            if this_is_the_beacon:
                print("Part 2: ", x * 4000000 + y)
                return

find_beacon(0, 20 if file == "sample.txt" else 4000000, sensors)
# %%
