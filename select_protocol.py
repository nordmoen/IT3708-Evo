#!/usr/bin/python

from random import sample
from math import ceil

from population import Population

class SelectionProtocol(object):
    def __init__(self, select_alg, num_parents=0.5):
        assert select_alg, 'The selection algorithm must be something'
        assert 0.0 < num_parents, 'Must select some amount of parents'
        self.select_alg = select_alg
        self.num = num_parents

    def select(self, population):
        assert population, 'The population must contain something'
        size = len(population)
        next_pop = self.sub_select(population)
        assert len(next_pop) == size, 'The new population size is different than requested'
        return next_pop

    def sub_select(self, population):
        pass

class FullReplacement(SelectionProtocol):
    def sub_select(self, population):
        amount = len(population) * self.num
        selected_mates = self.select_alg.sample(int(ceil(amount)), population.get())
        mates = [sample(selected_mates, 2) for i in range(len(population)/2 + 1)]
        next_gen = []
        for mom, dad in mates:
            c1, c2 = mom.crossover(dad)
            next_gen.append(c1)
            next_gen.append(c2)
        while len(next_gen) > len(population):
            next_gen.pop()
        map(lambda x: x.mutate(), next_gen)
        return Population(next_gen)

class OverProduction(SelectionProtocol):
    def __select(self, population):
        pass

class GenerationalMixing(SelectionProtocol):
    def __select(self, population):
        pass
