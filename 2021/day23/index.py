# %%
from collections import defaultdict
from numpy import sign, Inf
from copy import deepcopy
import re
with open('input.txt') as f:
    data = [x.strip() for x in f.readlines()]
data
hallway = data[1]
hallway = [x == '.' for x in hallway]
hallway = [None] * sum(hallway)
hallway

roomA = []
roomB = []
roomC = []
roomD = []
for line in data[2:-1]:
    A, B, C, D = re.findall(r"([A-Z])", line)
    roomA.append(A)
    roomB.append(B)
    roomC.append(C)
    roomD.append(D)
rooms = dict(A=roomA, B=roomB, C=roomC, D=roomD)
room_to_hallway_index = dict(A=2, B=4, C=6, D=8)
energy_per_type = dict(A=1, B=10, C=100, D=1000)

def amphipods_are_sorted(rs):
    for key, values in rs.items():
        for value in values:
            if value != key:
                return False
    return True

def hall_rooms_to_state(h, rs):
    new_hall = tuple(h)
    rr = tuple([tuple([x for x in y]) for y in rs.values()])
    return (new_hall, rr)

seen_game_states = defaultdict(lambda: Inf)
next_game_states = defaultdict(lambda: Inf)
lowest_energy_ever = Inf
state_path = []

def move_amphipod(h, rs, energy=0, prev_states = []):
    global seen_game_states
    global next_game_states
    global lowest_energy_ever
    global state_path
    if energy >= lowest_energy_ever:
        return
    if amphipods_are_sorted(rs):
        lowest_energy_ever = energy
        state_path = prev_states
        print(f"I found a solution with energy: {energy}")
        return
    # First try to move the amphipods in the hallway
    for i, hh in enumerate(h):
        if hh is None:
            continue
        if rs[hh][0] is None:
            # There is space in my room, let's see if I can get there
            dest_index = room_to_hallway_index[hh]
            direction = sign(dest_index - i)

            if any(h[i+direction:dest_index+direction:direction]): 
                continue

            # Check for traitor in my room
            spot = None
            traitor = False
            for ii, pos in enumerate(rs[hh]):
                if pos is None: 
                    spot = ii
                elif pos != hh: traitor = True
            if traitor: continue
            moves = spot + 1

            # I CAN MOVE!
            new_rooms = deepcopy(rs)
            new_hallway = deepcopy(h)
            new_hallway[i] = None
            energy_coef = energy_per_type[hh]
            moves += abs(i - dest_index)
            new_rooms[hh][spot] = hh
            new_energy = energy + moves * energy_coef
            state_to_add = hall_rooms_to_state(new_hallway, new_rooms)
            if new_energy >= seen_game_states[state_to_add]: continue

            seen_game_states[state_to_add] = new_energy
            next_game_states[state_to_add] = (new_hallway, new_rooms, new_energy, [*prev_states, state_to_add])

    # Now move amphipods out into the hallway!
    for i, spots in rs.items():
        already_sorted = True
        for spot in spots:
            already_sorted = already_sorted and spot == i
        if already_sorted: continue
        spot = None
        for ii, spot in enumerate(spots):
            if spot is not None:
                moves = ii + 1
                originatingFromIndex, toMove = ii, spot
                break
        if spot is None: continue
        starting_index = room_to_hallway_index[i]
        energy_coef = energy_per_type[toMove]

        # Move into the hallway and left and right. -1 is to the left, +1 to the right
        for dir in [-1, 1]:
            for ii, hh in enumerate(h[starting_index::dir]):
                if hh is not None:
                    break
                hallwaypos = starting_index + ii * dir
                if hallwaypos in room_to_hallway_index.values():
                    continue
                new_rooms = deepcopy(rs)
                new_rooms[i][originatingFromIndex] = None
                new_hallway = deepcopy(h)
                new_hallway[hallwaypos] = toMove
                new_energy = energy + (moves + ii) * energy_coef
                state_to_add = hall_rooms_to_state(new_hallway, new_rooms)
                if new_energy >= seen_game_states[state_to_add]: continue
                seen_game_states[state_to_add] = new_energy
                next_game_states[state_to_add] = (new_hallway, new_rooms, new_energy, [*prev_states, state_to_add])


next_game_states[hall_rooms_to_state(hallway, rooms)] = (hallway, rooms, 0, [(hall_rooms_to_state(hallway, rooms))])
seen_game_states[hall_rooms_to_state(hallway, rooms)] = 0
competing_energy = Inf
depth = 0
while next_game_states:
    depth +=1
    print(depth)
    ngs = next_game_states
    next_game_states = defaultdict(lambda: Inf)

    for h, rs, energy, prev_states in ngs.values():
        move_amphipod(h, rs, energy, prev_states)
print(lowest_energy_ever)


#%%
def print_state(h, rs):
    hh = [x if x is not None else ' ' for x in h]
    A = [x if x is not None else ' ' for x in rs[0]]
    B = [x if x is not None else ' ' for x in rs[1]]
    C = [x if x is not None else ' ' for x in rs[2]]
    D = [x if x is not None else ' ' for x in rs[3]]
    print("#############")
    print(f"#{''.join(hh)}#")
    print(f"###{A[0]}#{B[0]}#{C[0]}#{D[0]}###")
    for i in range(1, len(A)):
        print(f"  #{A[i]}#{B[i]}#{C[i]}#{D[i]}#")
    print(f"  #########")
depth = 0
for h, rs in state_path[-5:]:
    if depth >= 4: break
    print_state(h, rs)
    print()
    depth +=1
# %%
