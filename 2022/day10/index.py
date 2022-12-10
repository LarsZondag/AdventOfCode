#%%
with open("input.txt", "r", encoding="utf-8") as f:
    data = f.read().splitlines()

register = []
cur_value = 1
for instruction in data:
    if instruction == "noop":
        register.append(cur_value)
    else:
        V = int(instruction[5:])
        register.extend([cur_value] * 2)
        cur_value += V
if data[-1].startswith("addx"):
    register.append(cur_value)

signal_strength_sum = 0
for i in range(20, 221, 40):
    if i >= len(register): break
    signal_strength_sum += register[i - 1] * i

print(signal_strength_sum)

#%% Part 2
image = [["."]*40 for _ in range(6)]
for i, v in enumerate(register):
    crt_pos = i % 40
    line = int(i / 40)
    if abs(crt_pos - v) <= 1:
        image[line][crt_pos] = "#"
image_joined = ["".join(line) for line in image]

for i in range(0, 40, 5):
    sub_image = [image_joined[j][i:i+5] for j in range(len(image))]
    for sub_image_line in sub_image:
        print(sub_image_line)
    print()
    print()
