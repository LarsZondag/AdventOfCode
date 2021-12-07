# %%
from statistics import mean
input = open('input.txt')
lines = input.read().splitlines()
input.close()
# %%
binaries = [list(map(int, list(line))) for line in lines]
transposed = list(map(list, zip(*binaries)))
means = [mean(line) for line in transposed]
gamma_binary = [round(x) for x in means]
epsilon_binary = [1-round(x) for x in means]
# %%
binary = [2**i for i in range(len(gamma_binary))]
binary.reverse()
gamma = 0
epsilon = 0
for index, decimal in enumerate(binary):
    gamma += decimal * gamma_binary[index]
    epsilon += decimal * epsilon_binary[index]
print(gamma * epsilon)
# %%
