from dna import DNA
import math
import random
from math import floor

class Population():
    def __init__(self, population = 0, goal = '', mutation_rate = 0):
        self.population = population
        self.goal = goal
        self.mutation_rate = mutation_rate
        self.goal_len = len(self.goal)
        self.population_dna = self.random_dna()
        self.mating_pool = []

    def __str__(self): 
        return (f'No. of dna = {self.population}\nGoal = {self.goal}\nGoal_len = {self.goal_len}\nMutation_rate = {self.mutation_rate}\n')

    def show(self):
        for dna in self.population_dna:
            print(dna)
            print('\n')

    def random_dna(self):
        population_dna = []

        for _ in range(self.population):
            dna = DNA(self.goal_len)
            dna.random_dna()
            population_dna.append(dna)

        return population_dna

    def find_fitness(self):
#       sum_fitness = 0
        max_f = 0
        for dna in self.population_dna:
            dna_p = 0
            fitness = 0
            score = 0

            for letter in self.goal:
                if dna.person[dna_p] == letter:
                    score = score + 1
                
                dna_p += 1
            
            fitness = score / self.goal_len
            #fitness = fitness ** 2
            dna.fitness = fitness

            if max_f <= dna.fitness:
                max_f = dna.fitness

#            sum_fitness = sum_fitness + fitness
#      avg_fitness = sum_fitness / self.population
        return max_f

    def max_fitness(self):
        max_f = 0
        max_f_person = ''
        for dna in self.population_dna:
            if max_f <= dna.fitness:
                max_f = dna.fitness
                max_f_person = dna.person

        return max_f_person
        

    def find_mating_pool(self):

        self.mating_pool = []
        max_f = self.find_fitness()

        # print('\n')
        # print(max_f)
        # print('\n')

        if max_f == 0:
            max_f = 0.01

        for dna in self.population_dna:
            normalized_fitness = dna.fitness / max_f
            probability = int(normalized_fitness * 100)
            repeat_dna = probability

            #print(f'Fitness = {normalized_fitness} Probability {dna.person} = {probability} that is repeat_dna = {repeat_dna}')

            for _ in range(repeat_dna):
                self.mating_pool.append(dna)

        if self.mating_pool == []:
            for dna in self.population_dna:
                self.mating_pool.append(dna)

        return max_f

    def reproduction(self):
        for dna in range(self.population):
            random_index1 = random.randint(0, len(self.mating_pool) - 1)
            random_index2 = random.randint(0, len(self.mating_pool) - 1)

            parent1 = self.mating_pool[random_index1]
            parent2 = self.mating_pool[random_index2]

            child = parent1.crossover(parent2)

            child.mutate(self.mutation_rate)

            self.population_dna[dna] = child
            
    def end(self):
        for dna in self.population_dna:
            if dna.person == self.goal:
                print(f'\nMy boy ---> {dna.person}\n')
                return True

# population = Population(10, 'lol', 1)
# # max_f = population.find_fitness()
# # population.show()
# # print('\n')
# # print(f'max_f = {max_f}')
# # print('\n')
# # print(f'population.max_fitness = {population.max_fitness()}')
# # print(fitness)

# population.find_mating_pool()
# # print(population.mating_pool)
# print(len(population.mating_pool))

# population.show()
    
