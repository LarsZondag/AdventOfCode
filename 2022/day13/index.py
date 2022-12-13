#%% Part 1
with open("input.txt", "r", encoding="utf-8") as f:
    data = [[eval(s) for s in l.splitlines()] for l in f.read().split("\n\n")]


def compare(left, right):
    if isinstance(left, int) and isinstance(right, int):
        if left < right:
            return -1
        elif left > right:
            return 1
        return 0
    elif isinstance(left, int):
        return compare([left], right)
    elif isinstance(right, int):
        return compare(left, [right])

    i = 0
    while True:
        left_end_reached = i + 1 > len(left)
        right_end_reached = i + 1 > len(right)

        if left_end_reached and not right_end_reached:
            return -1
        if right_end_reached and not left_end_reached:
            return 1
        if left_end_reached and right_end_reached:
            return 0
        cur_compare = compare(left[i], right[i])
        if cur_compare != 0:
            return cur_compare
        i += 1


indices = [
    index + 1
    for index, [left_packet, right_packet] in enumerate(data)
    if compare(left_packet, right_packet) == -1
]
print(f"Part 1: {sum(indices)}")

#%% Part 2
from functools import cmp_to_key

new_data = [item for sublist in data for item in sublist]
divider_package1 = [[2]]
divider_package2 = [[6]]
new_data.extend([divider_package1, divider_package2])
new_data.sort(key=cmp_to_key(compare))
index_dp1 = new_data.index(divider_package1) + 1
index_dp2 = new_data.index(divider_package2) + 1

index_dp1 * index_dp2
