#%% Part 1
str_per_elve = open("input.txt", "r", encoding="utf-8").read().split("\n\n")

calories = [
    sum(int(meal_str) for meal_str in elve_str.split("\n")) for elve_str in str_per_elve
]
max(calories)

#%% part 2
sum(sorted(calories)[-3:])
