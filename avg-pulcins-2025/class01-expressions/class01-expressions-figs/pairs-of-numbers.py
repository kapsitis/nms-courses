import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

# Positive divisors of 60
divisors = [1, 2, 3, 4, 5, 6, 10, 12, 15, 20, 30, 60]

# Setting up the plot
fig, ax = plt.subplots()

ax.set_xlim(0, 11)
ax.set_ylim(0, 2.4)
ax.set_aspect(1)  # Set aspect ratio

# ax.set_xlim(0, len(divisors) - 1)
# ax.set_ylim(6.7, 10)
ax.axis('off')

# Plotting the divisors as text without any commas
for i, divisor in enumerate(divisors):
    ax.text(i, 0, str(divisor), fontsize=16, ha='center')

# Connecting numbers into pairs with lines
# for i, divisor in enumerate(divisors):
#     if divisor <= 60 // divisor:
#         partner_index = divisors.index(60 // divisor)
#         ax.plot([i, partner_index], [7, 1], 'r-', lw=2)

for i, divisor in enumerate(divisors):
    if divisor <= 60 // divisor:
        partner_index = divisors.index(60 // divisor)
        # Calculate midpoint and width
        mid = (i + partner_index) / 2
        width = abs(partner_index - i)
        # Ellipse arc
        arc = patches.Arc((mid, 0.5), width, 3 - i*0.4, theta1=0, theta2=180, color='red', lw=2)
        ax.add_patch(arc)


plt.savefig('pairs-of-numbers.png', bbox_inches='tight', pad_inches=0)

# Show the plot
plt.show()