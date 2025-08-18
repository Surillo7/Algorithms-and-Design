import math

# --- Helper Functions ---


def dist_sq(p1, p2):
    """Calculates the squared Euclidean distance between two points."""
    return (p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2


def brute_force_closest_pair(points):
    """
    Finds the closest pair of points by brute force.
    This is used as the base case for the recursion when n <= 3.
    """
    min_dist_sq = float("inf")
    best_pair = (None, None)
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            d_sq = dist_sq(points[i], points[j])
            if d_sq < min_dist_sq:
                min_dist_sq = d_sq
                best_pair = (points[i], points[j])
    return best_pair, min_dist_sq


# --- Main Recursive Algorithm ---


def closest_pair_recursive(Px, Py):
    """
    The recursive worker function that implements the divide and conquer logic.
    - Px: points sorted by x-coordinate.
    - Py: points sorted by y-coordinate.
    """
    num_points = len(Px)

    # 1. Base Case: If we have 3 or fewer points, solve directly.
    if num_points <= 3:
        return brute_force_closest_pair(Px)

    # 2. Divide: Split the point set in half.
    mid = num_points // 2
    mid_point = Px[mid]

    # Create sorted sub-lists for the left (Q) and right (R) halves.
    Qx = Px[:mid]
    Rx = Px[mid:]

    # Efficiently create Qy and Ry in O(n) time.
    Q_set = set(Qx)
    Qy, Ry = [], []
    for p in Py:
        if p in Q_set:
            Qy.append(p)
        else:
            Ry.append(p)

    # 3. Conquer: Recursively find the closest pairs in each half.
    (p1, q1), min_dist_sq1 = closest_pair_recursive(Qx, Qy)
    (p2, q2), min_dist_sq2 = closest_pair_recursive(Rx, Ry)

    # 4. Combine: Find the best of the two halves and check the center strip.
    if min_dist_sq1 <= min_dist_sq2:
        d_sq = min_dist_sq1
        best_pair = (p1, q1)
    else:
        d_sq = min_dist_sq2
        best_pair = (p2, q2)

    # Filter Py to create a "strip" of points within delta of the center line.
    Sy = []
    for p in Py:
        if (p[0] - mid_point[0]) ** 2 < d_sq:
            Sy.append(p)

    # Scan the strip and check for any closer pairs.
    for i in range(len(Sy)):
        # For each point, only check the next 7 points in the y-sorted strip.
        for j in range(i + 1, min(i + 8, len(Sy))):
            pair_p, pair_q = Sy[i], Sy[j]
            d_sq_strip = dist_sq(pair_p, pair_q)
            if d_sq_strip < d_sq:
                d_sq = d_sq_strip
                best_pair = (pair_p, pair_q)

    return best_pair, d_sq


# --- Wrapper Function ---


def closest_pair(points):
    """
    The main user-facing function.
    Handles initial checks and sorting, then calls the recursive helper.
    """
    if len(points) < 2:
        return None, float("inf")

    # Pre-sorting step
    Px = sorted(points, key=lambda p: p[0])
    Py = sorted(points, key=lambda p: p[1])

    (p1, p2), min_dist_sq = closest_pair_recursive(Px, Py)

    # Return the final pair and their actual distance.
    return (p1, p2), math.sqrt(min_dist_sq)


# --- Example Usage ---
points = [(2, 3), (12, 30), (40, 50), (5, 1), (12, 10), (3, 4)]
pair, distance = closest_pair(points)

# The closest pair in this set is (2, 3) and (3, 4)
print(f"The closest pair of points is {pair} with a distance of {distance:.3f}")
