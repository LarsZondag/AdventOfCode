# %%
largerThanPrevious = 0
prevValue = sys.maxsize
input = open('input.txt')
for line in input:
    print(prevValue, int(line), int(line) > prevValue)
    if int(line) > prevValue:
        largerThanPrevious += 1
    prevValue = int(line)
input.close()
largerThanPrevious

# %%
