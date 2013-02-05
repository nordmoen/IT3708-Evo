#!/usr/bin/python

class BitSequenceFitness(object):
    def __call__(self, gene):
        assert gene, 'The given gene sequence is None'
        return self.sub_eval(gene)

    def sub_eval(self, gene):
        pass

class OneMaxFitness(BitSequenceFitness):
    def sub_eval(self, gene):
        return gene.count()

class RandomBitSequenceFitness(BitSequenceFitness):
    def __init__(self, target):
        assert target, 'The target bit sequence is None'
        self.__target = target

    def sub_eval(self, gene):
        assert len(gene) == len(self.__target), ('The target sequence has a ' +
                'different length than the given gene')
        count = 0
        for i in range(len(gene)):
            if gene[i] != self.__target[i]:
                count += 1
        return count
