import time
import random
import numpy as np


n = 1_000_000

#Plain python loop
start = time.perf_counter()
totals_loop = [random.randint(1,6) + random.randint(1,6) for _ in range(n)]
print("Loop: ", round(time.perf_counter()-start, 3), "seconds")

# Numpy
rng = np.random.default_rng(28)
start = time.perf_counter()
totals_np = rng.integers(1, 7, size = n) + rng.integers(1, 7, size = n)
print("Loops: ", round(time.perf_counter()-start, 3), "seconds")