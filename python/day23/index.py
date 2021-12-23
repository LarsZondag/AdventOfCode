# %%
from collections import defaultdict
from numpy import sign, Inf
from copy import deepcopy
with open('sample_input.txt') as f:
    data = [x.strip() for x in f.readlines()]
data
hallway = data[1]
hallway = [x == '.' for x in hallway]
hallway = [None] * sum(hallway)
hallway


roomA = [data[2][3], data[3][1]]
roomB = [data[2][5], data[3][3]]
roomC = [data[2][7], data[3][5]]
roomD = [data[2][9], data[3][7]]
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
            second_spot_free = rs[hh][1] is None
            if second_spot_free is not True and rs[hh][1] != hh:
                continue
            dest_index = room_to_hallway_index[hh]
            direction = sign(dest_index - i)

            if any(h[i+direction:dest_index+direction:direction]): 
                continue
            # I CAN MOVE!
            new_rooms = deepcopy(rs)
            new_hallway = deepcopy(h)
            new_hallway[i] = None
            energy_coef = energy_per_type[hh]
            moves = abs(i - dest_index)
            if second_spot_free:
                new_rooms[hh][1] = hh
                moves += 2
            else:
                new_rooms[hh][0] = hh
                moves += 1
            new_energy = energy + moves * energy_coef
            state_to_add = hall_rooms_to_state(new_hallway, new_rooms)
            if new_energy >= seen_game_states[state_to_add]: continue

            seen_game_states[state_to_add] = new_energy
            next_game_states[state_to_add] = (new_hallway, new_rooms, new_energy, [*prev_states, state_to_add])

    # Now move amphipods out into the hallway!
    for i, [spot1, spot2] in rs.items():
        if i == spot1 == spot2:
            continue
        moves = 1
        if spot1 is not None:
            originatingFromIndex = 0
            toMove = spot1
        elif spot2 is not None:
            originatingFromIndex = 1
            toMove = spot2
            moves += 1
        else:
            continue
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


def print_state(h, rs):
    hh = [x if x is not None else ' ' for x in h]
    A = [x if x is not None else ' ' for x in rs[0]]
    B = [x if x is not None else ' ' for x in rs[1]]
    C = [x if x is not None else ' ' for x in rs[2]]
    D = [x if x is not None else ' ' for x in rs[3]]
    print(f"""
        #############
        #{"".join(hh)}#
        ###{A[0]}#{B[0]}#{C[0]}#{D[0]}###
          #{A[1]}#{B[1]}#{C[1]}#{D[1]}#
          #########""")
depth = 0
for h, rs in state_path:
    if depth >= 4: break
    print_state(h, rs)
    print()
    depth +=1
# %%
