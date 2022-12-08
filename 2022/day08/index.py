#%%
import numpy as np

with open("input.txt", "r", encoding="utf-8") as f:
    data = [list(map(int, s)) for s in f.read().splitlines()]
data = np.array(data)

#%% Part 1
visible = 0

J, I = data.shape
for i in range(1, J-1):
    for j in range(1, I-1):
        height = data[i, j]
        if (height > data[:i, j]).all():
            visible+=1
        elif (height > data[i+1:, j]).all():
            visible+=1
        elif (height > data[i, :j]).all():
            visible+=1
        elif (height > data[i, j+1:]).all():
            visible+=1
        
visible += 2 * (J - 2) + 2*(I-2) + 4
print("Part 1: ", visible)
#%% Part 2
max_view_score = 0
for i in range(1, J-1):
    for j in range(1, I-1):
        height = data[i, j]
        larger_left = height > data[i, :j][::-1]
        view_left = np.logical_and.accumulate(larger_left).sum() + (~larger_left).any() 
        larger_right = height > data[i, j+1:]
        view_right = np.logical_and.accumulate(larger_right).sum() + (~larger_right).any() 
        larger_top = height > data[:i, j][::-1]
        view_top = np.logical_and.accumulate(larger_top).sum() + (~larger_top).any()
        larger_bottom = height > data[i+1:, j]
        view_bottom = np.logical_and.accumulate(larger_bottom).sum() + (~larger_bottom).any() 
        view_score = view_left * view_right * view_top * view_bottom
        max_view_score = max(max_view_score, view_score)
print("Part 2: ", max_view_score)

#%%