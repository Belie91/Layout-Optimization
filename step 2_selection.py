# Re-import needed libraries after reset
import random

# Facility list
facility_labels = ["A", "B", "C", "D", "E", "F", "G", "H", "I"]

# Facility positions (mock slicing coordinates)
facility_positions = {
    "A": (5, 15), "B": (15, 15), "C": (25, 15),
    "D": (5, 5), "E": (15, 5), "F": (25, 5),
    "G": (35, 15), "H": (35, 5), "I": (45, 10)
}

# Flow matrix (fij)
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

# Distance matrix (dij)
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


# Cost matrix (cij)
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
# Objective function helpers
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

# Generate initial random population
def generate_random_population(facilities, population_size=10):
    population = []
    for _ in range(population_size):
        chromosome = facilities[:]
        random.shuffle(chromosome)
        population.append(chromosome)
    return population

initial_population = generate_random_population(facility_labels, 10)

# Compute fitness for each chromosome
fitness_scores = [
    (chromosome, compute_total_handling_cost(facility_positions, flows, costs, chromosome))
    for chromosome in initial_population
]

# Tournament selection
def tournament_selection(population, fitnesses, tournament_size=3, num_selected=5):
    selected = []
    for _ in range(num_selected):
        contenders = random.sample(list(zip(population, fitnesses)), tournament_size)
        winner = min(contenders, key=lambda x: x[1])
        selected.append(winner)
    return selected

population = [chrom for chrom, _ in fitness_scores]
fitness_values = [score for _, score in fitness_scores]

selected_for_mating = tournament_selection(population, fitness_values, tournament_size=3, num_selected=5)
selected_for_mating
