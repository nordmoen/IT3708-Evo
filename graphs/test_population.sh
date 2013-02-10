#!/bin/bash

popSize="10 15 20 25 30 35 40 50 60 70 80 90 100"
crossover="0.01 0.02 0.03 0.04 0.05 0.1 0.15 0.2 0.25 0.3 0.35 0.4 0.45"
mutation="0.01 0.02 0.03 0.04 0.05 0.1 0.15 0.2 0.25 0.3 0.35 0.4 0.45"
elite="0 1 2 3 4 5 10 15"

for pop in 10 15 20 25 30 35 40 50 60 70 80 90 100
do
	filename="task3-population_$pop.dat"
	
	python main.py 100 40 $pop full_generational\
	proportionate max_fitness convert-genome plot\
	--crossover=0.08 --mutation=0.1 --seed=42\
	--elite=3 --filename=$filename
done
