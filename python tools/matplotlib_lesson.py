import numpy as np
import matplotlib.pyplot as plt

rng = np.random.default_rng(28)
n = 100_000
totals = rng.integers(1,7, size=n) + rng.integers(1,7, size=n)

values = np.arange(2, 13)
counts = np.bincount(totals, minlength=13)[2:]
exact = np.array([1,2,3,4,5,6,5,4,3,2,1]) / 36

# plt.bar(values, counts / n, label="Simulated")
# plt.plot(values, exact, "ro-", label="Exact")
# plt.xlim(0, 100)
# plt.xlabel("Total of two dice")
# plt.ylabel("Probability")
# plt.title("Two dice: simulation vs exact")
# plt.legend()
# plt.show()

#probability of obtaining a sum of 7 with respect to each run
is_seven = (totals == 7)
running_estimate = np.cumsum(is_seven) / np.arange(1, n+1)

plt.figure()
plt.plot(running_estimate)
plt.axline(1/6, color="red", linestyle="--", label="Exact = 1/6")
plt.xscale("log")
plt.xlabel("Number of rolls (log scale)")
plt.ylabel("Estimated P(total = 7)")
plt.legend()
plt.show()