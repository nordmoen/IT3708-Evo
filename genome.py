#!/usr/bin/python

from bitarray import bitarray
from random import randrange

class Genome:
    def __init__(self, val, fitness_func, cross_rate, mute_rate, convert_func=None):
        assert val, 'The value of the genome can\'t be None'
        assert 0.0 < cross_rate < 1.0, 'The crossover rate must be within the range (0.0, 1.0)'
        assert 0.0 <= mute_rate <= 1.0, 'The mutation rate must be within the range [0.0, 1.0]'
        self.__val = bitarray(val)
        self.__fit_func = fitness_func
        self.__cross_rate = cross_rate if cross_rate < 0.5 else 1 - cross_rate
        self.__mute_rate = mute_rate
        self.__convert_func = convert_func
        self.__len = len(self.__val)

    def fitness(self):
        return self.__fit_func(self.__val)

    def convert(self):
        if self.__convert_func:
            return self.__convert_func(self.get_value())

    def crossover(self, other):
        assert other, 'The other genome must not be None'
        if not self.__amount:
            self.__amount = int(self.__cross_rate * self.__len)
        point = randrange(self.__len - self.__amount)
        end = point + self.__amount
        my_val = self.get_value()
        other_val = other.get_value()
        my_val[point:end], other_val[point:end] = other_val[point:end], my_val[point:end]
        return (my_val, other_val)

    def mutate(self):
        if not self.__m_amount:
            self.__m_amount = int(self.__mute_rate * self.__len)
        for i in range(self.__m_amount):
            point = randrange(self.__len)
            self.__val[point] = not self.__val[point]

    def get_value(self):
        return bitarray(self.__val)

    def __repr__(self):
        return "Genome({!r},{},{!r},{!r},{})".format(self.__val, self.__fit_func,
                self.__cross_rate, self.__mute_rate, self.__convert_func)

    def __str__(self):
        return "Genome representing: {}".format(self.__val)
