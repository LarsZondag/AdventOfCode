#%%
import functools
with open("input.txt") as f:
    lines = [s.strip() for s in f.readlines()]
# %% P1
matcher = {
    '(': ')',
    '[': ']',
    '{': '}',
    '<': '>',
    }
point_matcher = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137,
}
openers = set(matcher.keys())
closers = set(matcher.values())
def check_line(line: str):
    open_stack = []
    points = 0
    for s in line:
        if s in openers: 
            open_stack.append(s)
            continue
        last_opened = open_stack.pop()
        if matcher[last_opened] != s:
            # print(f"{line} - Expected {matcher[last_opened]}, but found {s} instead.")
            points = point_matcher[s]
            break
    return {'line': line, 'points': points, 'open_stack': open_stack}
    
lines_checked = [check_line(l) for l in lines]
corrupted_scores = [l['points'] for l in lines_checked]
print(sum(corrupted_scores))
# %% P2
incomplete = [l['open_stack'] for l in lines_checked if l['points'] == 0]
point_matcher = {
    '(': 1,
    '[': 2,
    '{': 3,
    '<': 4,
}

def get_autocomplete_score(open_stack):
    autocomplete_score = 0
    for s in reversed(open_stack):
        autocomplete_score *= 5
        autocomplete_score += point_matcher[s]
    return autocomplete_score

autocomplete_scores = [get_autocomplete_score(s) for s in incomplete]
autocomplete_scores.sort()
middle_score = autocomplete_scores[len(autocomplete_scores)//2]
middle_score




# %%
