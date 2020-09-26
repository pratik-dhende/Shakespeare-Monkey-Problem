from string import ascii_lowercase, ascii_uppercase
import random

class DNA():
    alphabets = ascii_lowercase + ascii_uppercase + " ,.!'-?()"

    def __init__(self, goal_len = 0):
        self.fitness = 0
        self.length = goal_len
        self.person = ''

    def __str__(self):
        return (f'DNA_person = {self.person}\nDNA_length = {self.length}\nDNA_fitness = {self.fitness}%')

    def random_dna(self):
        person = ''

        for _ in range(self.length):
            random_index = random.randint(0, len(self.alphabets) - 1)
            person = person + self.alphabets[random_index]

        self.person = person

    def crossover(self, dna):
        index1 = random.randint(0, self.length - 1)

        #print(f'\nDna1 = {self.person} and Dna2 = {dna.person}')

        child = DNA(self.length)

        child.person = self.person[:index1] + dna.person[index1:]

        #print(f'Child = {child.person}\n')

        return child

    def mutate(self, mutation_rate = 0):
        for letter_p in range(self.length):
            if random.random() < (mutation_rate / 100):
                index_alphabet = random.randint(0, len(self.alphabets) - 1)
                random_gene = self.alphabets[index_alphabet]

                self.person = self.person[:letter_p]+ random_gene + self.person[letter_p + 1:]

            # print(f'self.person = {self.person}\n')

# dna1 = DNA(5)
# dna1.random_dna()
# print(dna1)
# print('\n')

# dna2 = DNA(5)
# dna2.random_dna()
# print(dna1)
# print('\n')

# print(dna.alphabets

