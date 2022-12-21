#%%
from functools import cache

with open("input.txt", "r", encoding="utf-8") as f:
    data = f.read().splitlines()


neighbours: dict[str, list[str]] = {}
flow_rates: dict[str, int] = {}
for line in data:
    start = len("Valve ")
    end = line.index(" has flow rate")
    current_valve = line[start:end]

    start = line.index("=") + 1
    end = line.index(";")
    flow_rate = int(line[start:end])
    flow_rates[current_valve] = flow_rate

    neighbour_part = line.split(";")[1]
    neighbours_str = neighbour_part[len(" tunnel leads to valve ") :].strip()
    neighbours[current_valve] = neighbours_str.split(", ")

worthwhile_nodes = [node for node, flow_rate in flow_rates.items() if flow_rate > 0]


def find_edges(neighbours, flow_rates):
    edges: dict[str, dict[str, int]] = {node: {} for node in flow_rates.keys()}

    for wn1 in edges.keys():
        for wn2 in worthwhile_nodes:
            if wn1 == wn2:
                continue
            visited: set[str] = set([wn1])
            frontier: list[tuple[str, int]] = [(wn1, 0)]
            while frontier:
                location, steps = frontier.pop(0)
                if location == wn2:
                    edges[wn1][wn2] = steps
                    break

                for nb in neighbours[location]:
                    if nb in visited:
                        continue
                    frontier.append((nb, steps + 1))
                    visited.add(nb)
    return edges


EDGES = find_edges(neighbours, flow_rates)
most_released = 0
max_time = 30


@cache
def find_highest_released(
    time_remaining: int,
    position: str = "AA",
    valve_options: frozenset[str] = frozenset(worthwhile_nodes),
    using_elephant=False,
):
    highest_released = 0
    if using_elephant:
        highest_released = find_highest_released(26, valve_options=valve_options)
    for valve in valve_options:
        if EDGES[position][valve] >= time_remaining:
            continue
        cur_opened = valve_options - {valve}
        new_time_remaining = time_remaining - EDGES[position][valve] - 1
        released = new_time_remaining * flow_rates[valve] + find_highest_released(
            new_time_remaining, valve, cur_opened, using_elephant=using_elephant
        )
        highest_released = max(highest_released, released)

    return highest_released


part1 = find_highest_released(30)
print("Part 1: ", part1)

part2 = find_highest_released(26, using_elephant=True)
print("Part 2: ", part2)

# %%
