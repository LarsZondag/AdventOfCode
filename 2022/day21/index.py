#%%
from copy import copy
from typing import cast
from typing import TypeAlias

with open("input.txt", "r", encoding="utf-8") as f:
    data = [s.split(" ") for s in f.read().splitlines()]

InstructionMonkey: TypeAlias = tuple[str, str, str]

monkeys: dict[str, str | InstructionMonkey] = {}
for items in data:
    key = items.pop(0)[:-1]
    if len(items) == 1:
        monkeys[key] = items[0]
    else:
        monkeys[key] = cast(InstructionMonkey, tuple(items))
original_monkeys = copy(monkeys)

def solve(monkeys, key="root") -> str:
    if isinstance(monkeys[key], str):
        return monkeys[key]
    left, op, right = monkeys[key]
    
    left = solve(monkeys, left)
    right = solve(monkeys, right)
    if left.isnumeric() and right.isnumeric():
        return str(int(eval(left + op + right)))

    return "(" + left + op + right + ")"

print("Part 1: ", int(eval(solve(monkeys))))

#%% Part 2
# The imaginary number trick is thanks to Reddit!
# Most other solutions seems to put this into a symbolic solver like wolfram.
new_monkeys = copy(original_monkeys)
assert isinstance(new_monkeys["humn"], str)
new_monkeys["humn"] = "-1j"
root_monkey = new_monkeys["root"]
assert not isinstance(root_monkey, str)
new_monkeys["root"] = (root_monkey[0], "-", root_monkey[2])
c = eval(solve(new_monkeys))
print("Part 2: ", int(c.real / c.imag))

# Example for the symbolic solver:
new_monkeys = copy(original_monkeys)
root_monkey = new_monkeys["root"]
assert not isinstance(root_monkey, str)
new_monkeys["root"] = (root_monkey[0], "-", root_monkey[2])
assert isinstance(new_monkeys["humn"], str)
new_monkeys["humn"] = "x"
print("Plug this into https://www.mathpapa.com/algebra-calculator.html")
print("0=" + solve(new_monkeys))
