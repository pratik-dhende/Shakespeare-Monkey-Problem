from population import Population

def display(generations, max_fitness, mutation_rate, fittest_person):
    print(f'Generations = {generations} | Max Fitness = {max_fitness} | Mutation rate = {mutation_rate} | Fittest person = {fittest_person}')

#Create population.
target = 'To be or not be.'
population = Population(200, target, 1)
population.random_dna()

generations = 0

while(1):
    generations += 1

    #Calculate fitness of population and the mating pool.
    max_fitness = population.find_mating_pool()
    fittest_person = population.max_fitness()

    #Display generations and their rate.
    display(generations, max_fitness, population.mutation_rate, fittest_person)

    #Check if population has achieved their goal
    if(population.end()):
        break

    #Reproduce the population.
    population.reproduction()


