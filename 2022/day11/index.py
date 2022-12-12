#%%
from copy import deepcopy

with open("input.txt", "r", encoding="utf-8") as f:
    data = [s.splitlines() for s in f.read().split("\n\n")]
data


def parse_monkey(raw: list[str]):
    monkey_number = int(raw[0][len("Monkey"): -1])
    items = list(map(int, raw[1][len("  Starting items:"):].split(", ")))
    operation = eval("lambda: " + raw[2].split(" = ")[1])
    test = int(raw[3][len("  Test: divisible by"):])
    if_true = int(raw[4][len("    If true: throw to monkey "):])
    if_false = int(raw[5][len("    If false: throw to monkey "):])

    return monkey_number, dict(
        items=items,
        operation = operation,
        test=test,
        if_true=if_true,
        if_false=if_false,
        n_inspects=0
    )
monkeys_raw = [parse_monkey(d) for d in data]

monkeys_initial = {mn: props for mn, props in monkeys_raw}

tests = [monkey["test"] for monkey in monkeys_initial.values()]
max_test = max(tests)
common_multiple = max_test
while True:
    if all(common_multiple % test == 0 for test in tests):
        break
    common_multiple += max_test

# Part 1
monkeys = deepcopy(monkeys_initial)
for i in range(20):
    for monkey in monkeys.values():
        for _ in range(len(monkey["items"])):
            monkey["n_inspects"] += 1
            old = monkey["items"].pop(0)
            new = monkey["operation"]()
            new = int(new/3)
            new %= common_multiple
            if new % monkey["test"] == 0:
                monkeys[monkey["if_true"]]["items"].append(new)
            else:
                monkeys[monkey["if_false"]]["items"].append(new)

n_inspects = [monkey["n_inspects"] for monkey in monkeys.values()]
n_inspects = sorted(n_inspects)
print("Part 1: ", n_inspects[-1] * n_inspects[-2])

# Part 2
monkeys = deepcopy(monkeys_initial)
for i in range(10000):
    for monkey in monkeys.values():
        for _ in range(len(monkey["items"])):
            monkey["n_inspects"] += 1
            old = monkey["items"].pop(0)
            new = monkey["operation"]()
            new %= common_multiple
            if new % monkey["test"] == 0:
                monkeys[monkey["if_true"]]["items"].append(new)
            else:
                monkeys[monkey["if_false"]]["items"].append(new)

n_inspects = [monkey["n_inspects"] for monkey in monkeys.values()]
n_inspects = sorted(n_inspects)
print("Part 2: ", n_inspects[-1] * n_inspects[-2])

# %%
