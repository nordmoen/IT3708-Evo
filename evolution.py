#!/usr/bin/python

def evolution_loop(protocol, logger, max_loop=100, pop_size=20):
    population = None
    for i in range(1, max_loop + 1):
        print 'Progress: {0:d}%'.format((i/float(max_loop))*100)
        logger(i, population)
        population = protocol.select(population)
    logger.finish()
