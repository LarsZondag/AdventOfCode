# %%
import numpy as np
f = open('input.txt')
lines = f.read()
f.close()

sections = lines.split('\n\n')

numbers_drawn = sections.pop(0).split(',')
numbers_drawn = [int(x) for x in numbers_drawn]
numbers_drawn


def parse_line(line): return [int(x) for x in line.split()]
def parse_board(x): return [parse_line(line) for line in x.split('\n')]


boards = [parse_board(x) for x in sections]
boards = np.array(boards)
matches = np.array(boards, dtype=np.bool)
matches.fill(False)

for number_drawn in numbers_drawn:
    matches[boards == number_drawn] = True
    horizontal = matches.all(axis=1).any(axis=1)
    vertical = matches.all(axis=2).any(axis=1)
    no_bingo = horizontal | vertical

    if no_bingo.any():
        winning_index = no_bingo.argmax()
        winning_board = boards[winning_index]
        winning_matches = matches[winning_index]

        undrawn = winning_board[~winning_matches].sum()
        score = undrawn * number_drawn
        print(score)
        break

# %% P2
matches = np.array(boards, dtype=np.bool)
matches.fill(False)
bingo = np.zeros(len(matches), dtype=np.bool)
for number_drawn in numbers_drawn:
    previous_matches = matches
    matches[boards == number_drawn] = True

    horizontal = matches.all(axis=1).any(axis=1)
    vertical = matches.all(axis=2).any(axis=1)
    new_bingo = horizontal | vertical
    if new_bingo.all():
        winning_index = bingo.argmin()
        winning_board = boards[winning_index]
        winning_matches = matches[winning_index]
        undrawn = winning_board[~winning_matches].sum()
        score = undrawn * number_drawn
        print(score)
        break
    bingo[new_bingo] = True
# %%
