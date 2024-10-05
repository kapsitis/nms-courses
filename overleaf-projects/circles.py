import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle

# Constants
RADIUS_LARGE_CIRCLE = 1  # Radius of the large circle
RADIUS_SMALL_CIRCLE = 0.1  # Radius of the small circles
ANGLE_STEP = 2 * np.pi / 12  # Angle step for arranging small circles

# Generate the numbers to place in the small circles
numbers = [2**k % 13 for k in range(0, 12)]

# Create a figure and a single subplot
fig, ax = plt.subplots()

# Draw the large circle
large_circle = plt.Circle((0, 0), RADIUS_LARGE_CIRCLE, color='blue', fill=False)
ax.add_artist(large_circle)

# Calculate positions for small circles and place them along with the numbers
for i, number in enumerate(numbers):
    # Angle for the current small circle (like the position on a clock face)
    angle = ANGLE_STEP * i
    
    # Determine the coordinates on the large circle
    x = RADIUS_LARGE_CIRCLE * np.cos(angle)
    y = RADIUS_LARGE_CIRCLE * np.sin(angle)
    
    # Create the small circle and add it to the plot
    # small_circle = Circle((x, y), RADIUS_SMALL_CIRCLE, color='white', fill=True)
    small_circle = Circle((x, y), RADIUS_SMALL_CIRCLE, facecolor='white', edgecolor='gray', linewidth=1, fill=True)
    ax.add_artist(small_circle)
    
    # Place the number text inside the small circle
    ax.text(x, y, str(number), fontsize=12, ha='center', va='center')

# Set the aspect of the plot to be equal
ax.set_aspect('equal')

# Remove axes for better visual
plt.axis('off')

# Set limits to slightly larger than the large circle's radius
plt.xlim(-1.2 * RADIUS_LARGE_CIRCLE, 1.2 * RADIUS_LARGE_CIRCLE)
plt.ylim(-1.2 * RADIUS_LARGE_CIRCLE, 1.2 * RADIUS_LARGE_CIRCLE)

# Display the plot
# plt.show()
plt.savefig('myplot.pdf')