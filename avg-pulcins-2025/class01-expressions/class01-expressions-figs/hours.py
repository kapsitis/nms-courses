import matplotlib.pyplot as plt
import numpy as np
import matplotlib.colors as mcolors

# Režģa izmērs
rows, cols = 24, 60

# Izveido matricu, ko piepilda ar nullēm
grid = np.zeros((rows, cols))

# Saraksta vieniniekus tur, kur stundas-minūtes dalās ar 7
for row in range(0,24): 
    for col in range(0,60):
        if (row - col) % 7 == 0: 
            grid[row,col] = 1

# Nokrāso: 0 -> white, 1 -> blue
cmap = mcolors.ListedColormap(['white', 'blue'])

# Uzzīmē režģi
fig, ax = plt.subplots(figsize=(15, 6))
ax.imshow(grid, cmap=cmap)

# Uzzīmē asis
ax.set_xticks(np.arange(-0.5, cols, 1), minor=True)
ax.set_yticks(np.arange(-0.5, rows, 1), minor=True)
ax.grid(which='minor', color='gray', linestyle='-', linewidth=1)

# plt.xticks([])
# plt.yticks([])

# Novāc uzrakstus no asīm
ax.set_xticklabels([])
ax.set_yticklabels([])

plt.show()