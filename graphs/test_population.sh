#!/bin/bash

for run in 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20
do
	rand=$RANDOM
	for pop in 5 10 11 12 13 14 15 16 17 18 19 20
	do
		filename="task3-population_$pop-rand_$rand.dat"
		
		python ../main.py 100 40 $pop full_generational\
		proportionate max_fitness convert-genome plot\
		--crossover=0.5 --mutation=0.025 --seed=$rand\
		--elite=5 --filename=$filename --stop_cond=40

	done
done

for pop in 5 10 11 12 13 14 15 16 17 18 19 20
do
	python average.py pop $pop task3-population_$pop-rand_*
	rm task3-population_$pop-rand_*
done

mv task3-population_* data/
gnuplot < plot_population_average.gnuplot
