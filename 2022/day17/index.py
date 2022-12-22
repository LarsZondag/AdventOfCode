#%%
from functools import cache
from typing import cast
from typing import Literal

rocks = [
    s.splitlines()
    for s in """####

.#.
###
.#.

..#
..#
###

#
#
#
#

##
##""".split(
        "\n\n"
    )
]

with open("input.txt", "r", encoding="utf-8") as f:
    jet_pattern = cast(list[Literal["<", ">"]], f.read())


@cache
def get_rock_raw(rock_index):
    rock_list = rocks[rock_index]
    rock_height = len(rock_list)
    rock: set[tuple[int, int]] = set()
    for y, rock_line in enumerate(rock_list):
        for x, rock_str in enumerate(rock_line):
            if rock_str == ".":
                continue
            rock.add((x + 2, rock_height - y + 3))
    return rock


def get_rock(rock_index, highest_rock):
    rock = get_rock_raw(rock_index)
    rock = {(x, y + highest_rock) for (x, y) in rock}
    return rock


def move_rock_lateral(
    rock: set[tuple[int, int]],
    static_rocks: set[tuple[int, int]],
    direction: Literal["<", ">"],
):
    if direction == "<":
        if any(x == 0 for (x, _) in rock):
            return rock

        new_rock = {(x - 1, y) for (x, y) in rock}
        if any(piece in static_rocks for piece in new_rock):
            return rock
        return new_rock

    if any(x == 6 for (x, _) in rock):
        return rock

    new_rock = {(x + 1, y) for (x, y) in rock}
    if any(piece in static_rocks for piece in new_rock):
        return rock
    return new_rock


def get_signature(rock_index: int, jet_index: int, static_rocks: set[tuple[int, int]], highest_rock: int):
    relevant_rocks = frozenset((x, highest_rock - y) for (x, y) in static_rocks if y >= highest_rock - 30)
    return (rock_index, jet_index, relevant_rocks)


def find_highest_rock(max_rocks: int):
    global rocks, jet_pattern
    fallen_rocks = 0
    n_rocks = len(rocks)
    static_rocks: set[tuple[int, int]] = set([(i, 0) for i in range(7)])
    highest_rock = 0
    jet_index = 0
    seen: dict[tuple[int, int, frozenset[tuple[int, int]]], tuple[int, int]] = {}
    additional_height = 0
    while fallen_rocks < max_rocks:
        rock_index = fallen_rocks % n_rocks
        rock = get_rock(rock_index, highest_rock)
        while True:
            rock = move_rock_lateral(rock, static_rocks, jet_pattern[jet_index])
            jet_index = (jet_index + 1) % len(jet_pattern)

            new_rock = {(i, y - 1) for (i, y) in rock}
            if all(piece not in static_rocks for piece in new_rock):
                rock = new_rock
                continue

            # The rock has landed
            static_rocks |= rock
            fallen_rocks += 1
            current_rock_max = max(y for (_, y) in rock)
            highest_rock = max(highest_rock, current_rock_max)
            
            # Check to see if the current pattern is already known. If so, repeat
            # as often as possible without inserting more blocks than `max_rocks`
            signature = get_signature(rock_index, jet_index, static_rocks, highest_rock)
            if signature in seen:
                (previously_fr, previously_hr) = seen[signature]
                dfr = fallen_rocks - previously_fr
                dy = highest_rock - previously_hr
                multiples = (max_rocks - fallen_rocks) // dfr
                fallen_rocks += multiples * dfr
                additional_height += multiples * dy

            else:
                seen[signature] = (fallen_rocks, highest_rock)
            break

    return highest_rock + additional_height


highest_rock = find_highest_rock(2022)

print("Part 1: ", highest_rock)
#%%
highest_rock = find_highest_rock(1000000000000)
print("Part 2: ", highest_rock)
