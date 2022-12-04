# %%
input = open('input.txt')
commands = [line.split(' ') for line in input]
commands = [[command[0], int(command[1])] for command in commands]
input.close()
# %%
horizontal = 0
depth = 0
aim = 0
for command in commands:
    if command[0] == 'down':
        aim += command[1]
    elif command[0] == 'up':
        aim -= command[1]
    elif command[0] == 'forward':
        horizontal += command[1]
        depth += aim * command[1]
print(horizontal * depth)
# %%
