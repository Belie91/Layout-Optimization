# Redefine facility positions for center coordinates (same as before)
facility_positions = {
    "A": (5, 15), "B": (15, 15), "C": (25, 15),
    "D": (5, 5), "E": (15, 5), "F": (25, 5),
    "G": (35, 15), "H": (35, 5), "I": (45, 10)
}

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

# Define the objective function
def manhattan_distance(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

def compute_total_handling_cost(facility_positions, flows, costs, facility_order):
    total_cost = 0
    for i, fi in enumerate(facility_order):
        for j, fj in enumerate(facility_order):
            if i != j:
                d_ij = manhattan_distance(facility_positions[fi], facility_positions[fj])
                total_cost += flows[i][j] * d_ij * costs[i][j]
    return total_cost

# Define an initial population of chromosomes (example facility orders)
initial_population = [
    ["A", "B", "C", "D", "E", "F", "G", "H", "I"],  # Example chromosome
    ["I", "H", "G", "F", "E", "D", "C", "B", "A"],  # Another example chromosome
    # Add more chromosomes as needed
]

# Evaluate fitness for each chromosome
fitness_scores = [
    (chromosome, compute_total_handling_cost(facility_positions, flows, costs, chromosome))
    for chromosome in initial_population
]

fitness_scores
