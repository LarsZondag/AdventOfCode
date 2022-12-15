#%%
# file = "sample.txt"
file = "input.txt"
with open(file, "r", encoding="utf-8") as f:
    data = [s[len("Sensor at "):].split(": closest beacon is at ") for s in f.read().splitlines()]

sensors = []
min_x, max_x = 0, 0
min_y, max_y = 0, 0
for sensor_line in data:
    sensor = {}
    string_x, string_y = sensor_line[0].split(", ")
    sensor["x"] = int(string_x[2:])
    sensor["y"] = int(string_y[2:])
    string_x, string_y = sensor_line[1].split(", ")
    sensor["beacon_x"] = int(string_x[2:])
    sensor["beacon_y"] = int(string_y[2:])

    sensor["distance"] = abs(sensor["x"] - sensor["beacon_x"]) + abs(sensor["y"] - sensor["beacon_y"])
    sensors.append(sensor)
    min_x = min(min_x, sensor["x"] - sensor["distance"])
    max_x = max(max_x, sensor["x"] + sensor["distance"])
    min_y = min(min_y, sensor["y"] - sensor["distance"])
    max_y = max(max_y, sensor["y"] + sensor["distance"])
#%% Part 1
debug = False
def debug_print(*args, **kwargs):
    if debug:
        print(*args, **kwargs)

y = 10 if file == "sample.txt" else 2000000
n_cannot_contain_beacon = 0
print(f"x to check: ", max_x - min_x)
for x in range(min_x, max_x + 1):
    cannot_contain_beacon = False
    is_sensor_position = False
    is_beacon_position = False
    for sensor in sensors:
        if x == sensor["x"] and y == sensor["y"]:
            is_sensor_position = True
            break
        if x == sensor["beacon_x"] and y == sensor["beacon_y"]:
            is_beacon_position = True
            break
        distance = abs(sensor["x"] - x) + abs(sensor["y"] - y)
        if distance <= sensor["distance"]:
            cannot_contain_beacon = True
            break
    if is_sensor_position:
        debug_print("S", end="")
    elif is_beacon_position:
        debug_print("B", end="")
    elif cannot_contain_beacon:
        n_cannot_contain_beacon += 1
        debug_print("#", end="")
    else:
        debug_print(".", end="")
debug_print("")
n_cannot_contain_beacon



# %% Part 2

sns = [(sensor["x"], sensor["y"], sensor["distance"]) for sensor in sensors]

min_x = 0
max_x = 20 if file == "sample.txt" else 4000000
min_y = 0
max_y = 20 if file == "sample.txt" else 4000000

for x in range(min_x, max_x + 1):
    y = 0
    this_is_the_beacon = True
    if x % 100000 == 0:
        print(f"{x} out of {max_x}")
    while y <= max_y:
        this_is_the_beacon = True
        for sensor_x, sensor_y, sensor_distance in sns:
            distance = abs(x-sensor_x) + abs(y-sensor_y)
            if distance <= sensor_distance:
                y = sensor_y + sensor_distance - abs(sensor_x - x) + 1
                this_is_the_beacon = False
                break
        if this_is_the_beacon:
            print(x, y)
            print(x * 4000000 + y)
            break
    if this_is_the_beacon: break