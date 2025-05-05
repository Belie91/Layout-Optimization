# Objective function for a facility location problem
def compute_total_cost(flows, distances, costs):
    n = len(flows)  # Number of facilities
    total_cost = 0
    for i in range(n):
        for j in range(n):
            fij = flows[i][j]  # Flow between facility i and j
            dij = distances[i][j]  # Distance between facility i and j
            cij = costs[i][j]  # Cost coefficient between facility i and j
            total_cost += fij * dij * cij
    return total_cost

# Objective function helpers
def manhattan_distance(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

# Input matrices based on the provided tables
flows = [
    [0, 25, 30, 5, 20, 3, 4, 0, 0],  # From A
    [0, 0, 0, 0, 0, 0, 0, 0, 0],   
    [0, 0, 0, 0, 0, 0, 0, 0, 0],     # Placeholder for other rows
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [15, 0, 0, 0, 0, 0, 0, 0, 0],        # From H
    [0, 0, 0, 0, 0, 0, 0, 0, 0]
]

distances = [
    [0, 23.5, 31, 31.5, 38, 15.5, 38, 19.5, 31.5],  # From A
    [23.5, 0, 8.5, 25, 31.5, 39, 61.5, 43, 55],     # From B
    [31, 8.5, 0, 16.5, 23, 30.5, 53, 41.5, 46.5],   # From C
    [31.5, 25, 16.5, 0, 6.5, 23, 36.5, 42, 30],     # From D
    [38, 31.5, 23, 6.5, 0, 29.5, 30, 48.5, 36.5],   # From E
    [15.5, 39, 30.5, 23, 29.5, 0, 22.5, 19, 16],    # From F
    [38, 61.5, 53, 36.5, 30, 22.5, 0, 18.5, 6.5],   # From G
    [19.5, 43, 41.5, 42, 48.5, 19, 18.5, 0, 12],    # From H
    [31.5, 55, 46.5, 30, 36.5, 16, 6.5, 12, 0]      # From I
]

costs = [
    [0, 1612500, 1867500, 315000, 1455000, 85500, 111000, 0, 0],  # From A
    [0, 0, 0, 0, 0, 0, 0, 0, 0],                            
    [0, 0, 0, 0, 0, 0, 0, 0, 0],                                 # Placeholder for other rows
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [438750, 0, 0, 0, 0, 0, 0, 0, 0],                           # From H
    [0, 0, 0, 0, 0, 0, 0, 0, 0]
]

# Calculate total cost
total_cost_result = compute_total_cost(flows, distances, costs)
print("Total Cost:", total_cost_result)