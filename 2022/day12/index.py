#%%
from copy import deepcopy

with open("input.txt", "r", encoding="utf-8") as f:
    letter_lists = f.read().splitlines()


start_pos: tuple[int, int]
end_pos: tuple[int, int]
heights = {}
for j, letter_list in enumerate(letter_lists):
    for i, letter in enumerate(letter_list):
        if letter == "S":
            start_pos = (i, j)
            heights[(i, j)] = ord("a")
        elif letter == "E":
            end_pos = (i, j)
            heights[(i, j)] = ord("z")
        else:
            heights[(i, j)] = ord(letter)
assert start_pos
assert end_pos

max_x = len(letter_lists[0])
max_y = len(letter_lists)

def find_shortest_path(sps: list[tuple[int, int]], ep: tuple[int, int]):
    frontier = {loc: 0 for loc in sps}
    visited = {loc: 0 for loc in sps}
    
    while len(frontier) > 0:
        cur_pos = min(frontier, key=frontier.get)
        
        cur_score = frontier[cur_pos]
        del frontier[cur_pos]

        next_score = cur_score + 1
        
        cur_height = heights[cur_pos]
        for delta in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            next_x = cur_pos[0] + delta[0]
            next_y = cur_pos[1] + delta[1]
            if next_x < 0 or next_x >= max_x:
                continue
            if next_y < 0 or next_y >= max_y:
                continue
        
            next_pos = (next_x, next_y)
            if next_pos in visited and visited[next_pos] <= next_score:
                continue

            next_height = heights[next_pos]
            if next_height - cur_height > 1:
                continue

            if next_pos == ep:
                return next_score

            frontier[next_pos] = next_score
            visited[next_pos] = next_score
    return False

shortest_path = find_shortest_path([start_pos], end_pos)
print("Part 1: ", shortest_path)
# %% Part 2

start_pos_list: list[tuple[int, int]] = []
for j, letter_list in enumerate(letter_lists):
    for i, letter in enumerate(letter_list):
        if letter == "S" or letter == "a":
            start_pos_list.append((i, j))
shortest_path = find_shortest_path(start_pos_list, end_pos)

print("Part 2: ", shortest_path)
# %%
