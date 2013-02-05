#!/usr/bin/python

from math import sqrt
from random import sample, random
from types import IntType

from population import Population

def normalized(scaled):
    factor = float(sum(map(lambda x: x[1], scaled)))
    normalized = []
    for gene, val in scaled:
        normalized.append((gene, val/factor))
    return normalized

def roulette_select(amount, elite, normalized):
    ends = []
    s = 0
    for gene, val in normalized:
        s += val
        ends.append(s)
    selected = []
    norm_sorted = sorted(normalized, key=lambda x: x[1])
    if elite > 0:
        for i in range(elite):
            selected.append(norm_sorted[i][0])

    while len(selected) < amount:
        rand = random()
        for i, val in enumerate(ends):
            if rand < val:
                selected.append(normalized[i][0])
                break
    assert amount == len(selected), 'The amount selected does not equal the wanted amount'
    return selected

class SelectionMechanism(object):
    def sample(self, amount, population):
        assert amount > 0, 'The amount to select is to little'
        assert len(population) > 1, 'The population must have at least two individuals'
        assert type(amount) is IntType, 'The amount must be an integer'
        return self.sub_sample(amount, population)

    def sub_sample(self, amount, population):
        pass

class FitnessProportionate(SelectionMechanism):
    def __init__(self, eliteism_count):
        self.elite = eliteism_count

    def sub_sample(self, amount, population):
        gene_val = [(gene, gene.fitness()) for gene in population]
        return roulette_select(amount, self.elite, normalized(gene_val))

class SigmaScaling(SelectionMechanism):
    def sub_sample(self, amount, population):
        avg = (reduce(lambda acc,y: acc + y.fitness(), population, 0) /
                float(len(population)))
        stdev = sqrt(reduce(lambda acc, x: acc + (x - avg)**2, population, 0)/
                float(len(population)))
        scaled = []
        for gene in population:
            scaled.append((gene, 1 + (gene.fitness() - avg)/(2*stdev)))
        return roulette_select(amount, self.elite, normalized(scaled))

class TournamentSelection(SelectionMechanism):
    def __init__(self, elite, k=10, e=0.2):
        super(TournamentSelection, self).__init__(elite)
        assert k >= 1, 'Can\'t select with a tournament size less than 1'
        assert 1.0 > e >= 0.0, '"e" must be in the range [0.0, 1.0)'
        self.__k = k
        self.__e = e

    def sub_sample(self, amount, population):
        selected = []
        while len(selected) < amount:
            tournament = sample(population, self.__k)
            p = 1 - self.__e
            for i, gene in enumerate(tournament):
                if random() < p*((1-p)**i):
                    selected.append(gene)
                    break
        return selected

class RankSelection(SelectionMechanism):
    def __init__(self, elite, mini=0.5, maxi=1.5):
        super(RankSelection, self).__init__(elite)
        assert 0.0 <= mini <= 1.0, 'The min value must be within the range [0.0, 1.0]'
        assert 1.0 <= maxi <= 2.0, 'The max value must be within the range [1.0, 2.0]'
        self.__max = maxi
        self.__min = mini

    def sub_sample(self, amount, population):
        sort_pop = sorted(population, cmp=lambda x,y: cmp(x.fitness(), y.fitness()))
        size = len(sort_pop)
        scaled = []
        for i, gene in enumerate(sort_pop):
            scaled.append((gene, self.__min + (self.__max - self.__min)*((i-1)/(size - 1))))
        return roulette_select(amount, self.elite, normalized(scaled))
