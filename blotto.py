#!/usr/bin/python

import phenotypes
import fitness

class ConvertBlotto(phenotypes.ConvertGenome):
    def __init__(self, fitness, b, s):
        super(ConvertBlotto, self).__init__(fitness)
        self.__b = b
        self.__s = s

    def convert(self, gene):
        strategies = []
        bits = gene.get_value()
        for i in range(self.__b):
            strategies.append(int(bits[i:i+5].to01(), 2) / 3)
        norm = float(sum(strategies))
        for i in range(len(strategies)):
            strategies[i] /= norm
            strategies *= self.__s

class BlottoPheno(phenotypes.Phenotype):
    def __init__(self, gene, fit, 
