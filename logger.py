#!/usr/bin/python

class FitnessLogger(object):
    def __call__(self, i, population):
        assert population, 'Population can\'t be None'
        return self.sub_call(i, population)

    def finish(self):
        return self.sub_finish()

    def sub_call(self, i, population):
        pass

class CmdLogger(FitnessLogger):
    def sub_call(self, i, population):
        best, avg, stdev = population.get_stats()
        print '-'*30
        print 'Generation: {0:d}'.format(i)
        print 'Best: {0:s}'.format(best)
        print 'Average fitness: {0:f}, stdev:{1:f}'.format(avg, stdev)
        print '-'*30
    def __finish():
        pass

class PlotLogger(FitnessLogger):
    def __init__(self, name):
        assert name, 'Can\'t create a file without a name'
        self.__log = []
        self.__filename = name

    def sub_call(self, i, population):
        best, avg, stdev = population.get_stats()
        self.__log.append('{0:d}\t{1:f}\t{2:f}\n'.format(i, avg, stdev))

    def sub_finish(self):
        with open(self.__filename, 'w') as f:
            f.writelines(self.__log)
