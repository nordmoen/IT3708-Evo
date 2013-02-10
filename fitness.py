#!/usr/bin/python

from bitarray import bitarray

class BitSequenceFitness(object):
    def __call__(self, pheno):
        assert pheno, 'The given phoneme sequence is None'
        return self.sub_eval(pheno)

    def sub_eval(self, pheno):
        pass

class OneMaxFitness(BitSequenceFitness):
    def sub_eval(self, pheno):
        return pheno.get_value().count()

class RandomBitSequenceFitness(BitSequenceFitness):
    def __init__(self, target):
        assert target, 'The target bit sequence is None'
        assert isinstance(target, bitarray), 'The target needs to be a bitarray'
        self.__target = target

    def sub_eval(self, pheno):
        assert len(pheno) == len(self.__target), ('The target sequence has a ' +
                'different length than the given gene')
        count = 0
        bitArr = pheno.get_value()
        for i in range(len(bitArr)):
            if bitArr[i] != self.__target[i]:
                count += 1
        return count
