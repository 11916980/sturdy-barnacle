def chebyshev_distance(point1, point2):
    differences = [abs(a - b) for a, b in zip(point1, point2)]
    return max(differences)
