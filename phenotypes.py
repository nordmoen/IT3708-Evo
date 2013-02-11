#!/usr/bin/python

class Phenotype(object):
    def __init__(self, gene, fitness_func):
        self.__gene = gene
        self.__fit = fitness_func

    def get_gene(self):
        return self.__gene

    def fitness(self, pop):
        return self.__fit(self.__gene, pop)

    def __str__(self):
        return 'Phenotype({0!s}), fitness:{1:.1f}'.format(self.__gene, self.fitness(None))

    def __repr__(self):
        return 'Phenotype({0!r}, {1!r})'.format(self.__gene, self.__fit)

    def __eq__(self, other):
        try:
            return self.__gene == other.get_gene()
        except:
            return False

class ConvertGenome(object):
    def __init__(self, fitness):
        self.__fitness = fitness

    def __call__(self, gene):
        return self.convert(gene)

    def convert(self, gene):
        return Phenotype(gene, self.__fitness)
