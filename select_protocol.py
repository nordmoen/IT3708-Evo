#!/usr/bin/python

from random import sample

from population import Population

class SelectionProtocol:
    def __init__(self, select_alg):
        assert select_alg, 'The selection algorithm must be something'
        self.__select_alg = select_alg

    def select(self, population):
        assert population, 'The population must contain something'
        size = len(population)
        next_pop = self.__select(population)
        assert len(next_pop) == size, 'The new population is smaller than requested'
        return next_pop

class FullReplacement(SelectionProtocol):
    def __select(self, population):
        selected_mates = self.select_alg.sample(len(population), population.get())
        mates = [sample(selected_mates, 2) for i in range(len(population)/2)]
        next_gen = []
        for mom, dad in mates:
            c1, c2 = mom.crossover(dad)
            next_gen.append(c1)
            next_gen.append(c2)
        return Population(next_gen)

class OverProduction(SelectionProtocol):
    def __select(self, population):
        pass

class GenerationalMixing(SelectionProtocol):
    def __select(self, population):
        pass
