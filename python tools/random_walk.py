import numpy as np
import matplotlib.pyplot as plt

rng = np.random.default_rng(28)

steps = rng.choice([1, -1], size=(5, 100))    #5 people, 100 steps
paths = np.cumsum(steps, axis=1)    #position after each step

for path in paths:
    plt.plot(path)
plt.xlabel("Step")
plt.ylabel("Position")
plt.xlim(0,100)
plt.title("5 random walks")
plt.show()