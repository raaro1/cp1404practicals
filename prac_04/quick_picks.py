import random

MAX = 45
MIN = 6
NUMBERS_PER_PICK = 6

quick_picks = int(input("How many quick picks? "))

for i in range(quick_picks):
    numbers = []
    while len(numbers) < NUMBERS_PER_PICK:
        random_number = random.randint(MIN, MAX)
        if random_number not in numbers:
            numbers.append(random_number)
    numbers.sort()
    print(" ".join(f"{num:2}" for num in numbers))

