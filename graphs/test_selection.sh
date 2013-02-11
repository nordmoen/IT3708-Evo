#!/bin/bash

for run in 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20
do
	rand=$RANDOM
	for mech in "proportionate" "sigma" "tournament" "rank"
	do
		filename="task4-select_$mech-rand_$rand.dat"
		python ../main.py 100 40 15 full_generational\
		$mech max_fitness convert-genome plot\
		--crossover=0.5 --mutation=0.015 --seed=$rand\
		--elite=5 --filename=$filename --stop_cond=40\
		--k=5 --e=0.05
	done
done

for mech in "proportionate" "sigma" "tournament" "rank"
do
	python average.py selection $mech task4-select_$mech-rand_*
	rm task4-select_$mech-rand_*
done

mv task4-select_* data/
gnuplot < plot_selection_average.gnuplot
