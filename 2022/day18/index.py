#%%
from functools import cache
from statistics import median

with open("input.txt", "r", encoding="utf-8") as f:
    data = set(eval(f"({s})") for s in f.read().splitlines())

min_x = min(x for (x, _, _) in data) - 5
min_y = min(y for (_, y, _) in data) - 5
min_z = min(z for (_, _, z) in data) - 5
max_x = max(x for (x, _, _) in data) + 5
max_y = max(y for (_, y, _) in data) + 5
max_z = max(z for (_, _, z) in data) + 5
median_y = median(y for (_, y, _) in data)
median_z = median(z for (_, _, z) in data)

target = (min_x + 1, min_y + 1, min_z + 1)

can_go_out: set[tuple[int, int, int]] = set()
cannot_go_out: set[tuple[int, int, int]] = set()


def find_way_out(x: int, y: int, z: int) -> bool:
    global can_go_out
    global cannot_go_out

    if (x, y, z) in can_go_out:
        return True
    if (x, y, z) in cannot_go_out:
        return False

    visited: set[tuple[int, int, int]] = set()
    frontier: set[tuple[int, int, int]] = {(x, y, z)}
    while frontier:
        cur_pos = frontier.pop()
        x, y, z = cur_pos
        if cur_pos == target:
            can_go_out |= visited
            return True

        if cur_pos not in data:
            visited.add(cur_pos)

        variations = [
            (x - 1, y, z),
            (x + 1, y, z),
            (x, y + 1, z),
            (x, y - 1, z),
            (x, y, z + 1),
            (x, y, z - 1),
        ]
        for new_pos in variations:
            i, j, k = new_pos
            if i > max_x:
                continue
            if i < min_x:
                continue
            if j > max_y:
                continue
            if j < min_y:
                continue
            if k > max_z:
                continue
            if k < min_z:
                continue
            if new_pos in visited:
                continue
            if new_pos in data:
                continue
            frontier.add(new_pos)
    cannot_go_out |= visited
    return False


def find_outside_faces(counting_inside: bool):
    outside_faces = 0
    for (i, j, k) in data:
        # left
        if (i - 1, j, k) not in data and (counting_inside or find_way_out(i - 1, j, k)):
            outside_faces += 1
        # right
        if (i + 1, j, k) not in data and (counting_inside or find_way_out(i + 1, j, k)):
            outside_faces += 1
        # down
        if (i, j - 1, k) not in data and (counting_inside or find_way_out(i, j - 1, k)):
            outside_faces += 1
        # up
        if (i, j + 1, k) not in data and (counting_inside or find_way_out(i, j + 1, k)):
            outside_faces += 1
        # bottom
        if (i, j, k - 1) not in data and (counting_inside or find_way_out(i, j, k - 1)):
            outside_faces += 1
        # top
        if (i, j, k + 1) not in data and (counting_inside or find_way_out(i, j, k + 1)):
            outside_faces += 1
    return outside_faces


print("Part 1: ", find_outside_faces(True))
print("Part 2: ", find_outside_faces(False))
