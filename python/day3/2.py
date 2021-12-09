# %%
from statistics import mean
input = open('input.txt')
lines = input.read().splitlines()
input.close()
binaries = [list(map(int, list(line))) for line in lines]

# %%
oxy_candidates = binaries.copy()
co2_candidates = binaries.copy()
for i in range(len(oxy_candidates[0])):
    oxy_bits_at_i = [b[i] for b in oxy_candidates]
    co2_bits_at_i = [b[i] for b in co2_candidates]
    most_common_at_i = int(mean(oxy_bits_at_i) + 0.5)
    least_common_at_i = 1 - int(mean(co2_bits_at_i) + 0.5)
    if len(oxy_candidates) > 1:
        oxy_candidates = [
            o for o in oxy_candidates if o[i] == most_common_at_i]
    if len(co2_candidates) > 1:
        co2_candidates = [
            o for o in co2_candidates if o[i] == least_common_at_i]
oxy_binary = oxy_candidates[0]
co2_binary = co2_candidates[0]

# %%
binary = [2**i for i in range(len(oxy_binary))]
binary.reverse()
oxy = 0
co2 = 0
for index, decimal in enumerate(binary):
    oxy += decimal * oxy_binary[index]
    co2 += decimal * co2_binary[index]
print(oxy)
print(co2)
print(oxy*co2)

# %%
