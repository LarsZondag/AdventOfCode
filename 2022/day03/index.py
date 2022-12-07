#%%
with open("input.txt", "r", encoding="utf-8") as f:
    data = f.read().split("\n")
backpacks = [(d[:int(len(d) / 2)], d[int(len(d) / 2):]) for d in data]

backpack_commons = [list(set(b[0]).intersection(b[1]))[0] for b in backpacks]
backpack_commons

item_values = [ord(item) - 96 * item.islower() + (27 - 65)*(1-item.islower()) for item in backpack_commons]
sum(item_values)

#%% Part 2
groups = [data[i:i+3] for i in range(0, len(data), 3)]

badge_items = []

for group in groups:
    badge_item = set(group[0]).intersection(group[1]).intersection(group[2])
    badge_items.append(list(badge_item)[0])

badge_values = [ord(item) - 96 * item.islower() + (27 - 65)*(1-item.islower()) for item in badge_items]
sum(badge_values)
