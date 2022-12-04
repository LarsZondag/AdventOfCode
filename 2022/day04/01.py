#%%
with open('input.txt', encoding="utf-8") as f:
    data = f.read().splitlines()

assignments = [
    (list(map(int, r[0].split("-"))), list(map(int, r[1].split("-")))) 
    for r in [p.split(",") for p in data]]

n_completely_contained = 0

for ass in assignments:
    ass0 = ass[0]
    ass1 = ass[1]
    if ass0[0] >= ass1[0]:
        if ass0[1] <= ass1[1]:
            # ass0 is completely inside ass1
            n_completely_contained += 1
            continue
    if ass1[0] >= ass0[0]:
        if ass1[1] <= ass0[1]:
            # ass1 is completely inside ass0
            n_completely_contained += 1
n_completely_contained

# %%
