import numpy as np

rng = np.random.default_rng(seed=28)

print(rng.random(2))
print(rng.integers(1,7, size = 5))
print(rng.normal(loc=170, scale=10, size=3)) #mean = 170, spread = 10
print(np.round(rng.exponential(scale=5, size=3), 4))      #waiting times, average 5
print(rng.choice(["red", "green", "blue"], size=4)) #random pick