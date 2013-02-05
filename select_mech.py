#!/usr/bin/python

from math import sqrt
from random import sample, random

from population import Population

def normalized(scaled):
    factor = float(sum(map(lambda x: x[1], scaled)))
    normalized = []
    for gene, val in scaled:
        normalized.append((gene, val/factor))
    return normalized

def roulette_select(amount, normalized):
    ends = []
    s = 0
    for gene, val in normalized:
        s += val
        ends.append(s)
    selected = []
    while len(selected) < amount:
        rand = random()
        for i, val in enumerate(ends):
            if rand < val:
                selected.append(normalized[i][0])
                break
    assert amount == len(selected), 'The amount selected does not equal the wanted amount'
    return selected

class SelectionMechanism:
    def sample(self, amount, population):
        assert amount > 0, 'The amount to select is to little'
        assert len(population) > 1, 'The population must have at least two individuals'
        return self.__sample(amount, population)

class FitnessProportionate(SelectionMechanism):
    def __sample(self, amount, population):
        gene_val = [(gene, gene.fitness()) for gene in population]
        return roulette_select(amount, normalized(gene_val))

class SigmaScaling(SelectionMechanism):
    def __sample(self, amount, population):
        avg = (reduce(lambda acc,y: acc + y.fitness(), population, 0) /
                float(len(population)))
        stdev = sqrt(reduce(lambda acc, x: acc + (x - avg)**2, population, 0)/
                float(len(population)))
        scaled = []
        for gene in population:
            scaled.append((gene, 1 + (gene.fitness() - avg)/(2*stdev)))
        return roulette_select(amount, normalized(scaled))

class TournamentSelection(SelectionMechanism):
    def __init__(self, k=10, e=0.2):
        assert k >= 1, 'Can\'t select with a tournament size less than 1'
        assert 1.0 > e >= 0.0, '"e" must be in the range [0.0, 1.0)'
        self.__k = k
        self.__e = e

    def __sample(self, amount, population):
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
    def __init__(self, mini=0.5, maxi=1.5):
        assert 0.0 <= mini <= 1.0, 'The min value must be within the range [0.0, 1.0]'
        assert 1.0 <= maxi <= 2.0, 'The max value must be within the range [1.0, 2.0]'
        self.__max = maxi
        self.__min = mini

    def __sample(self, amount, population):
        sort_pop = sorted(population, cmp=lambda x,y: cmp(x.fitness(), y.fitness()))
        size = len(sort_pop)
        scaled = []
        for i, gene in enumerate(sort_pop):
            scaled.append((gene, self.__min + (self.__max - self.__min)*((i-1)/(size - 1))))
        return roulette_select(amount, normalized(scaled))
