#%%

with open("input5.txt", encoding="utf-8") as f:
    data = f.read()

stacks, instructions = [s.splitlines() for s in data.split("\n\n")]
stacks = [s[1::4] for s in stacks]
stacks.reverse()

crates = [[]]*len(stacks[0])
for stack in stacks[1:]:
    for i, crate in enumerate(stack):
        if crate == " ": continue
        crates[i] = [*crates[i], crate]
crates
instructions = [s[5:] for s in instructions]
instructions = [s.split(" from ") for s in instructions]
instructions = [[s[0]] + s[1].split(" to ") for s in instructions]
instructions = [tuple(map(int, s)) for s in instructions]

for inst in instructions:
    print(crates)
    n_move, from_i, to_i = inst
    from_i -= 1
    to_i -= 1
    to_move = crates[from_i][-n_move:]
    # to_move.reverse() # comment out for part 2
    crates[to_i] += to_move
    crates[from_i] = crates[from_i][:-n_move]
crates

final_message = [s[-1] for s in crates]
"".join(final_message)