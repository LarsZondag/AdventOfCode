#%%
from typing import Any

with open("input.txt", "r", encoding="utf-8") as f:
    data = [int(number) for number in f.read().splitlines()]

total_numbers = len(data)
class Number():
    left: Any
    right: Any
    def __init__(self, number: int) -> None:
        self.original_number = number
        self.number = abs(number) % (total_numbers - 1)
        if number < 0:
            self.number *= -1

    def __str__(self) -> str:
        return f"{self.number} -- left: {self.left.number} -- right: {self.right.number}"

def get_decryption_number(data, numbers):
    decryption_numbers = []
    index_0 = data.index(0)
    cn = numbers[index_0]
    assert cn.number == 0
    for _ in range(3):
        for _ in range(1000):
            cn = cn.right
        decryption_numbers.append(cn.original_number)
    return sum(decryption_numbers)

def manipulate_the_numbers(numbers):
    for i in range(total_numbers):
        current_number = numbers[i]
    
        if current_number.number >= 0:
            for _ in range(current_number.number):
                swap_left = current_number
                swap_right = current_number.right
                right = swap_right.right
                left = swap_left.left

                left.right = swap_right
                right.left = swap_left

                swap_right.left = left
                swap_left.right = right

                swap_right.right = swap_left
                swap_left.left = swap_right
        else:
            for _ in range(abs(current_number.number)):
                swap_left = current_number.left
                swap_right = current_number
                right = swap_right.right
                left = swap_left.left

                left.right = swap_right
                right.left = swap_left

                swap_right.left = left
                swap_left.right = right

                swap_right.right = swap_left
                swap_left.left = swap_right

numbers: dict[int, Number] = {i: Number(number) for i, number in enumerate(data)}

for i, number in numbers.items():
    number.right = numbers[(i + 1) % total_numbers]
    if i > 0:
        number.left = numbers[(i-1)]
    else:
        number.left = numbers[total_numbers - 1]

manipulate_the_numbers(numbers)



decryption_number = get_decryption_number(data, numbers)

print("Part 1: ", decryption_number)

#%% Part 2
numbers = {i: Number(number * 811589153) for i, number in enumerate(data)}

for i, number in numbers.items():
    number.right = numbers[(i + 1) % total_numbers]
    if i > 0:
        number.left = numbers[(i-1)]
    else:
        number.left = numbers[total_numbers - 1]

for _ in range(10):
    manipulate_the_numbers(numbers)


decryption_number = get_decryption_number(data, numbers)

print("Part 2: ", decryption_number)