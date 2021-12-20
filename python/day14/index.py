#%%
from collections import defaultdict
from typing import Counter
import numpy as np
with open('input.txt') as f:
    data = f.read()
template, rules = data.split('\n\n')
rules = rules.splitlines()
rules = {key: value for key, value in (x.split(' -> ') for x in rules )}
strings = []
for i in range(len(template) - 1):
    strings.append(template[i:i+2])
start_counter = dict(Counter(strings))
#%%
def get_answer(depth = 10):
    counter = start_counter.copy()

    for _ in range(depth):
        new_counter = defaultdict(int)
        for key, freq in counter.items():
            middle = rules[key]
            left = key[0]
            right = key[1]
            new_counter[left + middle] += freq
            new_counter[middle + right] += freq
        counter = new_counter

    char_counter = defaultdict(int)
    for key, freq in counter.items():
        char_counter[key[0]] += freq
    char_counter[template[-1]] += 1

    char_counter = dict(sorted(char_counter.items(), key=lambda item: item[1], reverse=True))
    frequencies = list(char_counter.values())
    print(frequencies[0] - frequencies[-1])


# %% P1
get_answer(10)

#%% P2
get_answer(40)

# %% Much better solution from Reddit:
from collections import Counter

tpl, _, *rules = open('input.txt').read().split('\n')
rules = dict(r.split(" -> ") for r in rules)
pairs = Counter(map(str.__add__, tpl, tpl[1:]))
chars = Counter(tpl)
for _ in range(40):
    for (a,b), c in pairs.copy().items():
        x = rules[a+b]
        pairs[a+b] -= c
        pairs[a+x] += c
        pairs[x+b] += c
        chars[x] += c

print(max(chars.values())-min(chars.values()))

# %%
