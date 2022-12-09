#%%
import numpy as np

with open("input.txt", "r", encoding="utf-8") as f:
    data = [(s[0], int(s[2:])) for s in f.read().splitlines()]


def n_positions_of_tail(
    all_steps: list[tuple[str, int]], n_knots: int, verbose=False
) -> int:
    knots = np.zeros((n_knots, 2), dtype=np.int64)

    visited = set()

    for to_dir, steps in all_steps:
        if verbose:
            print(f"== {to_dir} {steps} ==")
        for _ in range(steps):
            match to_dir:
                case "R":
                    knots[0, 0] += 1
                case "L":
                    knots[0, 0] -= 1
                case "U":
                    knots[0, 1] += 1
                case "D":
                    knots[0, 1] -= 1
            for i in range(1, knots.shape[0]):
                diff_x = knots[i - 1, 0] - knots[i, 0]
                diff_y = knots[i - 1, 1] - knots[i, 1]
                if abs(diff_x) >= 2 or abs(diff_y) >= 2:
                    # We can move!
                    knots[i, 0] += max(-1, min(1, diff_x))
                    knots[i, 1] += max(-1, min(1, diff_y))

            visited.add(tuple(knots[-1, :]))
    return len(visited)


print(f"Part 1: {n_positions_of_tail(data, 2)}")
print(f"Part 2: {n_positions_of_tail(data, 10)}")
