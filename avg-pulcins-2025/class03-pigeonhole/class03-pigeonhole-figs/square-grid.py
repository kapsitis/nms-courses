import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(1, 4, 4)
y = np.linspace(1, 4, 4)
x, y = np.meshgrid(x, y)

x = x.flatten()
y = y.flatten()

plt.figure(figsize=(5, 5))

plt.axhline(y=1, color='gray', linestyle='--', linewidth=1)  # Horizontal line
plt.axhline(y=2, color='gray', linestyle='--', linewidth=1)  # Horizontal line
plt.axhline(y=3, color='gray', linestyle='--', linewidth=1)  # Horizontal line
plt.axhline(y=4, color='gray', linestyle='--', linewidth=1)  # Horizontal line

plt.axvline(x=1, color='gray', linestyle='--', linewidth=1)  # Vertical line
plt.axvline(x=2, color='gray', linestyle='--', linewidth=1)  # Vertical line
plt.axvline(x=3, color='gray', linestyle='--', linewidth=1)  # Vertical line
plt.axvline(x=4, color='gray', linestyle='--', linewidth=1)  # Vertical line

plt.scatter(x, y, s=300, edgecolor='black', facecolor='white', linewidth=2)

plt.grid(visible=True, linestyle='--', color='black')

plt.axis('off')

plt.show()
