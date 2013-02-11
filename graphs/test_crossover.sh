#!/bin/bash

for run in 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20
do
	rand=$RANDOM
	for cross in 0.025 0.05 0.1 0.2 0.3 0.4 0.5
	do
		for mute in 0.005 0.01 0.015 0.02 0.025 0.03
		do
			filename="task3-crossover_$cross-mute_$mute-rand_$rand.dat"
			python ../main.py 100 40 15 full_generational\
			proportionate max_fitness convert-genome plot\
			--crossover=$cross --mutation=$mute --seed=$rand\
			--elite=5 --filename=$filename --stop_cond=40
		done
	done
done
for cross in 0.025 0.05 0.1 0.2 0.3 0.4 0.5
do
	for mute in 0.005 0.01 0.015 0.02 0.025 0.03
	do
		filename="task3-crossover_$cross-mute_$mute-rand_*"
		python average.py "cross" $cross $mute\
		task3-crossover_$cross-mute_$mute-rand_*
		rm task3-crossover_$cross-mute_$mute-rand_*
	done
done

mv task3-cross* data/

for mute in 0.005 0.01 0.015 0.02 0.025 0.03
do
	cp plot_crossover_average.gnuplot plot_$mute.gnuplot
	sed -i "s/!MUTE!/$mute/g" plot_$mute.gnuplot
	gnuplot < plot_$mute.gnuplot
	rm plot_$mute.gnuplot
done
