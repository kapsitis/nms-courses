import numpy as np
import matplotlib.pyplot as plt

k_values = np.arange(1, 101)
probabilities = np.zeros(len(k_values))
n = 365
for k in k_values:
    probs = np.arange(n, n - k, -1) / n
    prob_not_shared = np.prod(probs)
    probabilities[k - 1] = 1 - prob_not_shared

plt.step(k_values, probabilities, where='post', color='red')
plt.xlabel("Cilvēku skaits (k)")
plt.ylabel("Varbūtiba")
plt.grid(True)
plt.show()