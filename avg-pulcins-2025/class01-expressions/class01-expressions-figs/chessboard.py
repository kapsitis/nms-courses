import matplotlib.pyplot as plt
import numpy as np
import random
from matplotlib.colors import ListedColormap

# Size of the chessboard
rows, cols = 4, 4

# Create a checkerboard pattern
chessboard = np.zeros((rows, cols))
for row in range(rows):
    for col in range(cols):
        if (row + col) % 2 == 0:
            chessboard[row, col] = 1  # White squares

colors = ['#999999', 'white']
listedCmap = ListedColormap(colors)

# Plot the chessboard
plt.imshow(chessboard, cmap=listedCmap, vmin=0, vmax=1)

# white_squares = [(i, j) for i in range(rows) for j in range(cols) if chessboard[i, j] == 1]
# a_index, b_index = random.sample(white_squares, 2)

a_index, b_index = (2,0),(3,3)

# Place the letters "A" and "B" on the chessboard
plt.text(a_index[0], a_index[1], 'A', color='black', ha='center', va='center', fontsize=48, fontweight='normal')
plt.text(b_index[0], b_index[1], 'B', color='black', ha='center', va='center', fontsize=48, fontweight='normal')

# Add grid lines
plt.xticks(np.arange(-0.5, cols, 1), [])
plt.yticks(np.arange(-0.5, rows, 1), [])
plt.grid(which='both', color='black', linestyle='-', linewidth=2)

# Adjust the plot
# plt.gca().set_xticks(np.arange(0.5, cols, 1), minor=True)
# plt.gca().set_yticks(np.arange(0.5, rows, 1), minor=True)
# plt.grid(which='minor', color='black', linestyle='-', linewidth=2)
# plt.tick_params(which='minor', size=0)

plt.xticks([])
plt.yticks([])
plt.tick_params(which='both', bottom=False, left=False)

# Show the plot
plt.show()