#%% Part 1
with open("input.txt", "r", encoding="utf-8") as f:
    data = f.read().split("\n")
rounds = [(s[0], s[2]) for s in data]

# A = Rock
# B = Paper
# C = Scissors
# X = Rock (1 point)
# Y = Paper (2 points)
# Z = Scissors (3 points)

# Losing (0 points)
# Draw (3 points)
# Win (6 points)

total_score = 0

for opponent, you in rounds:
    match you:
        case "X":
            total_score += 1
            match opponent:
                case "A":
                    total_score += 3
                case "B":
                    pass
                case "C":
                    total_score += 6
        case "Y":
            total_score += 2
            match opponent:
                case "A":
                    total_score += 6
                case "B":
                    total_score += 3
                case "C":
                    pass
        case "Z":
            total_score += 3
            match opponent:
                case "A":
                    pass
                case "B":
                    total_score += 6
                case "C":
                    total_score += 3

print(total_score)

#%% part 2
# A = Rock
# B = Paper
# C = Scissors
# X = Losing (0 points)
# Y = Draw (3 points)
# Z = Win (6 points)

# Rock (1 point)
# Paper (2 points)
# Scissors (3 points)

total_score = 0

for opponent, you in rounds:
    match you:
        case "X": # lose, Rock
            total_score += 0
            match opponent:
                case "A":
                    total_score += 3 # Scissors
                case "B":
                    total_score += 1 # Rock
                case "C":
                    total_score += 2 # Paper
        case "Y": # draw
            total_score += 3
            match opponent:
                case "A":
                    total_score += 1 # Rock
                case "B":
                    total_score += 2 # Paper
                case "C":
                    total_score += 3 # Scissors
        case "Z": # win
            total_score += 6
            match opponent:
                case "A":
                    total_score += 2 # Paper
                case "B":
                    total_score += 3 # Scissors
                case "C":
                    total_score += 1 # Rock

print(total_score)
