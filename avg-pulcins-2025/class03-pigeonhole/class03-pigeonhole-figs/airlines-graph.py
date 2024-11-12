import matplotlib.pyplot as plt

# Coordinates for the vertices of the square
vertices = {
    'A': (0, 1),
    'B': (1, 1),
    'C': (1, 0),
    'D': (0, 0)
}

# Edges connecting the vertices
edges = [
    ('A', 'B'),
    ('B', 'C'),
    ('B', 'D'),
    ('C', 'D')
]

# Create a new figure
plt.figure(figsize=(5, 5))

# Plot each edge
for edge in edges:
    point1 = vertices[edge[0]]
    point2 = vertices[edge[1]]
    plt.plot([point1[0], point2[0]], [point1[1], point2[1]], 'r-', lw=2)

# Plot each vertex
for vertex in vertices.values():
    plt.plot(vertex[0], vertex[1], 'ro', markersize=24)

# Remove axes
plt.axis('off')

# Show plot
plt.show()