# %%
with open('input.txt') as f:
    data = f.read().splitlines()
data
east = set()
south = set()

for i, line in enumerate(data):
    for ii, char in enumerate(line):
        if char == '.':
            continue
        if char == '>':
            east.add((i, ii))
        elif char == 'v':
            south.add((i, ii))

NS = len(data)
NE = len(data[0])

def print_snails(e, s):
    for i in range(NS):
        for ii in range(NE):
            if (i,ii) in e:
                print(">", end="")
            elif (i, ii) in s:
                print("v", end="")
            else:
                print(".", end="")
        print()

new_east = set()
new_south = set()
i = 0
while True:
    # if i == 4:
    #     print(i)
    #     print_snails(east, south)
    i += 1
    for y, x in east:
        new_x = (x+1) % NE
        new_pos = (y, new_x)
        if new_pos in east or new_pos in south:
            new_east.add((y, x))
        else:
            new_east.add(new_pos)

    for y, x in south:
        new_y = (y+1) % NS
        new_pos = (new_y, x)
        if new_pos in new_east or new_pos in south:
            new_south.add((y, x))
        else:
            new_south.add(new_pos)
    if new_south == south and new_east == east:
        print(i)
        break
    east = new_east
    south = new_south
    new_east = set()
    new_south = set()
    if i > 1000: break
    

# %%
