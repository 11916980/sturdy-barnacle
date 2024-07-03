def chebyshev_distance(point1, point2):
    max_difference = 0
    for a, b in zip(point1, point2):
        difference = abs(a - b)
        if difference > max_difference:
            max_difference = difference
    return max_difference
