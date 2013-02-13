#!/bin/bash

for run in 1 2 3 4 5 6 7 8 9 10
do
	rand=$RANDOM
	for pop in 10 20 30 40 50 60 70 80 90 100
	do
		filename="task3-population_$pop-rand_$rand.dat"
		
		python ../main.py 100 40 $pop full_generational\
		proportionate max_fitness convert-genome plot\
		--cross_rate=1.0 --cover_rate=0.5 --mutation=0.025 --seed=$rand\
		--elite=3 --filename=$filename --stop_cond=40

	done
done

for pop in 10 20 30 40 50 60 70 80 90 100
do
	python average.py pop $pop task3-population_$pop-rand_*
	rm task3-population_$pop-rand_*
done

mv task3-population_* data/
gnuplot < plot_population_average.gnuplot
