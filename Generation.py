import random

# Departments including facility 'I'
machines = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']
population = []

def generate_population():
    for _ in range(30):  # assuming population size is 30
        chromosome = machines.copy()
        random.shuffle(chromosome)
        population.append(chromosome)
    return population

# Call the function to generate the population
generated_population = generate_population()
print("Generated Population:")
for i, chromosome in enumerate(generated_population, start=1):
    print(f"{i}: {chromosome}")