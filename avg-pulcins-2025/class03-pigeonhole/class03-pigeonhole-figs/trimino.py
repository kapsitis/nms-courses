import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Create a new figure and axes
fig, ax = plt.subplots(figsize=(4, 4))

# Define the positions and sizes of the squares
squares = [
    (0, 1),   # Top left square
    (0, 0),   # Top right square
    (1, 0)    # Bottom right square
]

# Add squares to the plot
for (x, y) in squares:
    rect = patches.Rectangle((x, y), 1, 1, linewidth=2, edgecolor='black', facecolor='none')
    ax.add_patch(rect)

# Set the limits and aspect
ax.set_xlim(-0.5, 2.5)
ax.set_ylim(-0.5, 2.5)
ax.set_aspect('equal')

# Remove axes
ax.axis('off')

# Show the plot
plt.show()