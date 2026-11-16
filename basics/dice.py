import random

random.seed(28)

def roll_two_dice():
    return random.randint(1, 6) + random.randint(1, 6)

for runs in [100, 10_000, 1_000_000]:
    sevens = sum(1 for _ in range(runs) if roll_two_dice() == 7)
    print(f"{runs:>9} runs -> estimate: {sevens/runs:.4f}")

print("Exact answer: 6/36 =", round(6 / 36, 4))