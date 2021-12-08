# %%
with open('input.txt') as f:
    lines = [l.strip().split(" | ") for l in f.readlines()]
inputs = [l[0] for l in lines]
outputs = [l[1] for l in lines]


# %%


def identify_unique_digit(s: str):
    if len(s) == 2:  # 1
        return True
    elif len(s) == 4:  # 4
        return True
    elif len(s) == 3:  # 7
        return True
    elif len(s) == 7:  # 8
        return True
    else:
        return False


unique_outputs = [list(filter(identify_unique_digit, o.split()))
                  for o in outputs]
unique_outputs = [item for sublist in unique_outputs for item in sublist]
len(unique_outputs)
# %%
