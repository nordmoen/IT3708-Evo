#!/usr/bin/python

def evolution_loop(pop, protocol, logger, max_loop=100):
    population = pop
    for i in range(1, max_loop + 1):
        print 'Progress: {0:%}'.format(i/float(max_loop))
        best, avg, stdev = population.get_stats()
        logger(i, best, avg, stdev)
        if best.fitness() == len(best):
            break
        population = protocol.select(population)
    logger.finish()
