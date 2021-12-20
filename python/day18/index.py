# %%
import numpy as np
import regex as re

with open('input.txt') as f:
    snail_numbers = [x.strip() for x in f.readlines()]
# %%


def parse_string(string: str):  # string = int | [string, string]
    if string.isnumeric():
        return int(string)
    string = string[1:-1]
    depth = 0
    for i, char in enumerate(string):
        if char == '[':
            depth += 1
        elif char == ']':
            depth -= 1
        elif char == ',' and depth == 0:
            first, second = string[:i], string[i+1:]
            break

    return [parse_string(first), parse_string(second)]

# %%

import regex as re
def explode(string: str):
    regex_pair = r"^\[(\-?\d+),?(\-?\d+)?\]"
    regex_digit = r"(\-?\d+)"
    depth = 0
    to_scan = string
    scanned = ''
    remaining = ''
    exploded = False
    while len(to_scan) > 1:
        matches = re.match(regex_pair, to_scan)
        if matches and depth >= 4:
            exploded = True
            add_to_left, add_to_right = matches.groups()
            add_to_left, add_to_right = int(add_to_left), int(add_to_right)
            _, end = matches.span()
            remaining = to_scan[end:]
            break
        
        char, to_scan = to_scan[0], to_scan[1:]
        scanned += char
        if char == '[': depth += 1
        elif char == ']': depth -= 1
    if not exploded: return False, string
    
    left_digits = re.finditer(regex_digit, scanned)
    left_digits = list(left_digits)
    if left_digits:
        left_digit = left_digits[-1]
        start, end = left_digit.span()
        if end !=  len(scanned) - 1: scanned = scanned + '0'
        to_the_left = scanned[:start]
        to_the_right = scanned[end:]
        left_number = int(left_digit.group())
        new_number = left_number + add_to_left
        scanned = f"{to_the_left}{new_number}{to_the_right}"
    else:
        scanned += '0'
    right_digits = re.finditer(regex_digit, remaining)
    right_digits = list(right_digits)
    if right_digits:
        right_digit = right_digits[0]
        start, end = right_digit.span()
        to_the_left = remaining[:start]
        to_the_right = remaining[end:]
        right_number = int(right_digit.group())
        new_number = right_number + add_to_right
        remaining = f"{to_the_left}{new_number}{to_the_right}"
        if start != 1: remaining = '0' + remaining
    else:
        remaining = '0' + remaining
    return True, scanned + remaining
explode("[[[[0,7],4],[[7,8],[4,[6,7]]]],[1,1]]")

#%%
def split(string: str):
    regex_double_digits = r"(\-?\d{2,})"
    double_digits = re.finditer(regex_double_digits, string)
    double_digits = list(double_digits)
    if len(double_digits) == 0: return False, string
    double_digits = double_digits[0]
    start, end = double_digits.span()
    to_the_left = string[:start]
    to_the_right = string[end:]
    number = int(double_digits.group())
    left, right = int(np.floor(number/2)), int(np.ceil(number/2))
    new_element = f"[{left},{right}]"
    return True, to_the_left + new_element + to_the_right


# %%
def reduce(string: str):
    while True:
        exploded = splitted = False
        exploded, string = explode(string)
        if not exploded: splitted, string = split(string)
        if not exploded and not splitted: break
    return string

print(reduce("[[[[[4,3],4],4],[7,[[8,4],9]]],[1,1]]"))


#%%
def add_snailfish_number(a: str, b: str):
    new_number =  f"[{a},{b}]"
    return reduce(new_number)

def get_magnitude_of_array(elem: np.ndarray or int):
    if type(elem) == int: return elem
    left = elem[0]
    right = elem[1]
    return 3*get_magnitude_of_array(left) + 2*get_magnitude_of_array(right)

def get_magnitude_of_string(string: str):
    arr = parse_string(string)
    return get_magnitude_of_array(arr)

# %%
sum = snail_numbers[0]
for snail_number in snail_numbers[1:]:
    sum = add_snailfish_number(sum, snail_number)
print(sum)
print(get_magnitude_of_string(sum))
# %%

largest_magnitude = -np.inf
tested = set()
i = 0
for n1 in snail_numbers:
    i += 1
    print(i)
    for n2 in snail_numbers:
        combi1 = (n1, n2)
        combi2 = (n2, n1)
        if combi1 not in tested:
            number1 = add_snailfish_number(*combi1)
            mag1 = get_magnitude_of_string(number1)
            if mag1 > largest_magnitude: largest_magnitude = mag1
            tested.add(combi1)
        if combi2 not in tested:
            number2 = add_snailfish_number(*combi2)
            mag2 = get_magnitude_of_string(number2)
            if mag2 > largest_magnitude: largest_magnitude = mag2
            tested.add(combi2)

print(largest_magnitude)



# %%
