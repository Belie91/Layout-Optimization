# Function to compute total cost based on the given equation
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

# Example input matrices
flows = [
    [0, 10, 5],
    [10, 0, 8],
    [5, 8, 0]
]

distances = [
    [0, 2, 3],
    [2, 0, 1],
    [3, 1, 0]
]

costs = [
    [0, 1, 2],
    [1, 0, 3],
    [2, 3, 0]
]

# Calculate total cost
total_cost_result = compute_total_cost(flows, distances, costs)
print("Total Cost:", total_cost_result)