#%%
from math import prod
import re
from functools import cache
from typing import Literal, TypeAlias

BlueprintType: TypeAlias = tuple[int, int, int, int, int, int, int]
with open("input.txt", "r", encoding="utf-8") as f:
    data: list[BlueprintType] = [
        tuple(map(int, re.findall(r"\d+", s))) for s in f.read().splitlines()  # type: ignore
    ]


def find_quality_level(blueprint: BlueprintType, problem: Literal[1, 2]):
    (
        blueprint_nr,
        ore_robot_ore,
        clay_robot_ore,
        obsidian_robot_ore,
        obsidian_robot_clay,
        geode_robot_ore,
        geode_robot_obsidian,
    ) = blueprint

    max_ore_robots = max(
        [ore_robot_ore, clay_robot_ore, obsidian_robot_ore, geode_robot_ore]
    )
    max_clay_robots = obsidian_robot_clay
    max_obsidian_robots = geode_robot_obsidian
    match problem:
        case 1:
            max_time = 24
        case 2:
            max_time = 32
    @cache
    def find_max_geodes(
        t: int = max_time,  # time remaining
        o: int = 0,  # ore available
        o_r: int = 1,  # ore robots
        c: int = 0,  # clay available
        c_r: int = 0,  # clay robots
        ob: int = 0,  # obsidian available
        ob_r: int = 0,  # obsidian robots
    ):
        if t <= 0:
            return 0

        geode_numbers: list[int] = []

        # Ore robot
        if o_r < max_ore_robots and o >= ore_robot_ore:
            geode_numbers.append(
                find_max_geodes(
                    t - 1,  # new time
                    o + o_r - ore_robot_ore,  # ore + newly mined ore - cost
                    o_r + 1,  # number of robots + 1
                    c + c_r,  # clay + newly mined clay
                    c_r,  # clay robots stay the same
                    ob + ob_r,  # obsidian + newly mined obsidian
                    ob_r,  # obsidian robots stay the same
                )
            )

        # Clay robot
        if c_r < max_clay_robots and o >= clay_robot_ore:
            geode_numbers.append(
                find_max_geodes(
                    t - 1,  # new time
                    o + o_r - clay_robot_ore,  # ore + newly mined ore - cost
                    o_r,  # number of robots stay the same
                    c + c_r,  # clay + newly mined clay
                    c_r + 1,  # clay robots + 1
                    ob + ob_r,  # obsidian + newly mined obsidian
                    ob_r,  # obsidian robots stay the same
                )
            )

        # Obsidian robot
        if (
            ob_r < max_obsidian_robots
            and o >= obsidian_robot_ore
            and c >= obsidian_robot_clay
        ):
            geode_numbers.append(
                find_max_geodes(
                    t - 1,  # new time
                    o + o_r - obsidian_robot_ore,  # ore + newly mined ore - cost
                    o_r,  # number of robots stay the same
                    c + c_r - obsidian_robot_clay,  # clay + newly mined clay - cost
                    c_r,  # clay robots
                    ob + ob_r,  # obsidian + newly mined obsidian
                    ob_r + 1,  # obsidian robots + 1
                )
            )

        # Geode robot
        if o >= geode_robot_ore and ob >= geode_robot_obsidian:
            geodes_from_this_robot = t - 1
            geodes_from_future = find_max_geodes(
                t - 1,  # new time
                o + o_r - geode_robot_ore,  # ore + newly mined ore - cost
                o_r,  # number of robots stay the same
                c + c_r,  # clay + newly mined clay
                c_r,  # clay robots
                ob + ob_r - geode_robot_obsidian,  # obsidian + newly mined- cost
                ob_r,  # obsidian robots
            )
            geode_numbers.append(geodes_from_this_robot + geodes_from_future)

        geode_numbers.append(
            find_max_geodes(
                t - 1,  # new time
                o + o_r,  # ore + newly mined ore
                o_r,  # number of robots stay the same
                c + c_r,  # clay + newly mined clay
                c_r,  # clay robots
                ob + ob_r,  # obsidian + newly mined obsidian
                ob_r,  # obsidian robots
            )
        )

        return max(geode_numbers)
    max_geodes = find_max_geodes()
    match problem:
        case 1:
            return max_geodes * blueprint_nr
        case 2:
            return max_geodes


print("Part 1: ", sum(find_quality_level(bp, problem=1) for bp in data))
print("Part 2: ", prod(find_quality_level(bp, problem=2) for bp in data[:3]))


# %%
