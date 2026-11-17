import numpy as np
import matplotlib.pyplot as plt

rng = np.random.default_rng(28)
n = 100_000
totals = rng.integers(1,7, size=n) + rng.integers(1,7, size=n)

values = np.arange(2, 13)
counts = np.bincount(totals, minlength=13)[2:]
exact = np.array([1,2,3,4,5,6,5,4,3,2,1]) / 36

plt.bar(values, counts / n, label="Simulated")
plt.plot(values, exact, "ro-", label="Exact")
plt.xlabel("Total of two dice")
plt.ylabel("Probability")
plt.title("Two dice: simulation vs exact")
plt.legend()
plt.show()