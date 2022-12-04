# %%
from collections import defaultdict
with open('input.txt') as f:
    p1, p2 = [int(x.strip().split(": ")[1]) for x in f.readlines()]

# %%
dice_rolls = 0
def wrap(x: int, base=10): return (x-1) % base + 1
def get_dice_rolls(current: int, n_dice_rolls): return (wrap(current+1, 100), wrap(current+2, 100), wrap(current+3, 100)), n_dice_rolls + 3

score_p1 = 0
score_p2 = 0
current_p1 = p1
current_p2 = p2
current_dice = 0
while True:
    dices , dice_rolls = get_dice_rolls(current_dice, dice_rolls)
    current_dice = dices[-1]
    moves = sum(dices)
    current_p1 = wrap(current_p1 + moves)
    score_p1 += current_p1
    if score_p1 >= 1000: break
    dices , dice_rolls = get_dice_rolls(current_dice, dice_rolls)
    current_dice = dices[-1]
    moves = sum(dices)
    current_p2 = wrap(current_p2 + moves)
    score_p2 += current_p2
    if score_p2 >= 1000: break

print(min(score_p1, score_p2) * dice_rolls)



# %% P2
def get_wins_and_playing(starting_pos:int):
    N_score_pos = defaultdict(int)
    N_score_pos[(0,starting_pos)] = 1
    N_score_pos_by_steps = {0: N_score_pos}
    N_wins_at_step = defaultdict(int)
    N_playing_at_step = defaultdict(int)
    N_playing_at_step[0] = 1
    i = 1
    while N_playing_at_step[i-1] - N_wins_at_step[i-1] > 0:
        new_score_pos = defaultdict(int)
        N_wins = 0
        N_playing = 0
        for (score, pos), N in N_score_pos_by_steps[i-1].items():
            for roll1 in range(1,4):
                for roll2 in range(1,4):
                    for roll3 in range(1,4):
                        new_pos = wrap(pos + roll1 + roll2 + roll3)
                        new_score = score + new_pos
                        N_playing += N
                        if new_score < 21:
                            new_score_pos[(new_score, new_pos)] += N
                        else:
                            N_wins += N
        N_score_pos_by_steps[i] = new_score_pos
        N_wins_at_step[i] = N_wins
        N_playing_at_step[i] = N_playing
        i+=1
    return N_playing_at_step, N_wins_at_step

P1s_playing_at_step, P1s_winning_at_step = get_wins_and_playing(p1)
P2s_playing_at_step, P2s_winning_at_step = get_wins_and_playing(p2)
universes_with_P1_winning = 0
universes_with_P2_winning = 0
for i in range(100):
    p1s_winning = P1s_winning_at_step[i]
    p1s_not_winning = P1s_playing_at_step[i] - p1s_winning
    p2s_playing = P2s_playing_at_step[i-1] - P2s_winning_at_step[i-1]
    p2s_winning = P2s_winning_at_step[i]
    
    p1s_actually_winning = p1s_winning * p2s_playing
    universes_with_P1_winning += p1s_actually_winning

    p2s_actually_winning = p2s_winning * p1s_not_winning
    universes_with_P2_winning += p2s_actually_winning

print(max(universes_with_P1_winning, universes_with_P2_winning))




# %% Reddit solution:
import functools

@functools.cache
def play(pos1, pos2, score1=0, score2=0):
  if score2 >= 21: return 0, 1

  wins1, wins2 = 0, 0
  for move, n in (3,1),(4,3),(5,6),(6,7),(7,6),(8,3),(9,1):
      pos1_ = (pos1 + move) % 10 or 10
      w2, w1 = play(pos2, pos1_, score2, score1 + pos1_)
      wins1, wins2 = wins1 + n*w1, wins2 + n*w2
  return wins1, wins2

print(max(play(4, 8)))

# %%
