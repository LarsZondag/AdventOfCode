#%%
with open('input.txt', encoding="utf-8") as f:
    data = f.read().splitlines()

assignments = [
    (list(map(int, r[0].split("-"))), list(map(int, r[1].split("-")))) 
    for r in [p.split(",") for p in data]]

n_overlap = 0

for ass in assignments:
    block_1 = ass[0]
    block_2 = ass[1]
    # block_1 starts before end of block_2
    # But then it should not end before the start of block_1
    if block_1[0] <= block_2[1] and block_1[1] >= block_2[0]:
        n_overlap += 1
n_overlap


# %%
