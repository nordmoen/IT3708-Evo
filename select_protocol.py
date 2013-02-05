#!/usr/bin/python

from random import sample

from population import Population

class SelectionProtocol(object):
    def __init__(self, select_alg, num_parents=0.5):
        assert select_alg, 'The selection algorithm must be something'
        assert 0.0 < num_parents, 'Must select some amount of parents'
        self.__select_alg = select_alg
        self.__num = num_parents

    def select(self, population):
        assert population, 'The population must contain something'
        size = len(population)
        next_pop = self.__select(population)
        assert len(next_pop) == size, 'The new population is smaller than requested'
        return next_pop

    def __select(self, population):
        pass

class FullReplacement(SelectionProtocol):
    def __select(self, population):
        selected_mates = self.__select_alg.sample(len(population)*self.__num, population.get())
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
