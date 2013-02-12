#!/usr/bin/python

import math

import phenotypes
import fitness

class ConvertBlotto(phenotypes.ConvertGenome):
    def __init__(self, fitness, b):
        super(ConvertBlotto, self).__init__(fitness)
        self.__b = b

    def convert(self, gene):
        strategies = []
        bits = gene.get_value().to01()
        for i in range(self.__b):
            strategies.append(int(bits[i*5:i*5 + 5], 2) / 3)
        norm = float(sum(strategies))
        strats = strategies[:]
        for i in range(len(strategies)):
            strategies[i] /= norm
        return BlottoPheno(gene, self.fitness, strategies, strats)

class BlottoPheno(phenotypes.Phenotype):
    def __init__(self, gene, fit, strat, orig_strat):
        super(BlottoPheno, self).__init__(gene, fit)
        self.__strat = strat
        self.__orig_strat = orig_strat

    def __repr__(self):
        return 'BlottoPheno({0!r}, {1!r}, {2!r}, {3!r})'.format(self.gene, self.fit,
                self.__strat, self.__orig_strat)

    def __str__(self):
        return 'Blotto: {0!s}'.format(self.__orig_strat)

    def get_strategy(self):
        return self.__strat[:]

    def __getitem__(self, key):
        return self.__strat[key]

    def get_entropy(self):
        return -reduce(lambda acc, x: acc + (x*math.log(x, 2) if x > 0 else 0), self.__strat, 0)

class BlottoFitness(fitness.BitSequenceFitness):
    def __init__(self, b, r, l):
        assert 0 < b, 'B must be larger than 0'
        assert 0 <= r <= 1, 'Redeploy fraction is outside of range [0,1]'
        assert 0 <= l <= 1, 'Loss fraction is outside of range [0,1]'
        self.__b = b
        self.__r = r
        self.__l = l
        self.__pop = None
        self.__fits = {}

    def sub_eval(self, pheno, population):
        if pheno in self.__fits:
            if self.__pop == population:
                return self.__fits[pheno]
        self.__pop = population
        self.__fits = {phenotype:0 for phenotype in self.__pop}
        for i in range(len(population) - 1):
            for j in range(i + 1, len(population)):
                diff = 0
                i_strh= 1.0
                i_ext = 0.0
                j_strh = 1.0
                j_ext = 0.0
                for k in range(self.__b):
                    i_pow = self.__pop[i][k]*i_strh + i_ext
                    j_pow = self.__pop[j][k]*j_strh + j_ext
                    if i_pow > j_pow:
                        diff += 1
                        j_strh *= self.__l
                        i_ext = ((self.__pop[i][k] - self.__pop[j][k]) * self.__r) / (self.__b - k)
                    elif i_pow < j_pow:
                        diff -= 1
                        i_strh *= self.__l
                        j_ext = ((self.__pop[j][k] - self.__pop[i][k]) * self.__r) / (self.__b - k)
                if diff > 0:
                    self.__fits[self.__pop[i]] += 2
                elif diff < 0:
                    self.__fits[self.__pop[j]] += 2
                else:
                    self.__fits[self.__pop[i]] += 1
                    self.__fits[self.__pop[j]] += 1
        return self.__fits[pheno]
