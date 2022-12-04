# %%
input = open('input.txt')
lines = [int(line) for line in input]
input.close()
sumIncreases = 0
for i in range(0, len(lines)-3):
    if lines[i] < lines[i + 3]:
        sumIncreases += 1
sumIncreases
# %%
