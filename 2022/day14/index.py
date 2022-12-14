#%%
with open("input.txt", "r", encoding="utf-8") as f:
    data = f.read().splitlines()

rocks: set[tuple[int, int]] = set()
sands: set[tuple[int, int]] = set()
max_y = 0

for rock_curve_str in data:
    rock_curve = rock_curve_str.split(" -> ")
    for start, end in zip(rock_curve[:-1], rock_curve[1:]):
        start_x, start_y = [int(number) for number in start.split(",")]
        end_x, end_y = [int(number) for number in end.split(",")]
        for y in range(min(start_y, end_y), max(start_y, end_y) + 1):
            for x in range(min(start_x, end_x), max(start_x, end_x) + 1):
                rocks.add((x, y))
                max_y = max(max_y, y)


sand_origin = (500, 0)
grain_fell_out = False
while grain_fell_out is False:
    sand_x, sand_y = sand_origin
    while True:
        if sand_y > max_y:
            grain_fell_out = True
            break

        next_pos = (sand_x, sand_y + 1)
        if next_pos not in rocks and next_pos not in sands:
            sand_y += 1
            continue

        next_pos = (sand_x - 1, sand_y + 1)
        if next_pos not in rocks and next_pos not in sands:
            sand_y += 1
            sand_x -= 1
            continue
        
        next_pos = (sand_x + 1, sand_y + 1)
        if next_pos not in rocks and next_pos not in sands:
            sand_y += 1
            sand_x += 1
            continue
        sands.add((sand_x, sand_y))
        break

print("Part 1: ", len(sands))

#%% Part 2
rocks = set()
sands = set()
max_y = 0

for rock_curve_str in data:
    rock_curve = rock_curve_str.split(" -> ")
    for start, end in zip(rock_curve[:-1], rock_curve[1:]):
        start_x, start_y = [int(number) for number in start.split(",")]
        end_x, end_y = [int(number) for number in end.split(",")]
        for y in range(min(start_y, end_y), max(start_y, end_y) + 1):
            for x in range(min(start_x, end_x), max(start_x, end_x) + 1):
                rocks.add((x, y))
                max_y = max(max_y, y)

floor_y = max_y + 2

sand_origin = (500, 0)
sand_at_origin = False
while sand_at_origin is False:
    sand_x, sand_y = sand_origin
    while True:
        if sand_y + 1 == floor_y:
            sands.add((sand_x, sand_y))
            break

        next_pos = (sand_x, sand_y + 1)
        if next_pos not in rocks and next_pos not in sands:
            sand_y += 1
            continue

        next_pos = (sand_x - 1, sand_y + 1)
        if next_pos not in rocks and next_pos not in sands:
            sand_y += 1
            sand_x -= 1
            continue
        
        next_pos = (sand_x + 1, sand_y + 1)
        if next_pos not in rocks and next_pos not in sands:
            sand_y += 1
            sand_x += 1
            continue
        

        sands.add((sand_x, sand_y))
        if sand_y == 0:
            sand_at_origin = True
        break

print("Part 2: ", len(sands))