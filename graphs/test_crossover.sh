#!/bin/bash

for run in 1 2 3 4 5 6 7 8 9 10
do
	rand=$RANDOM
	for cross in 0.0 0.1 0.3 0.5 0.6 0.8 1.0
	do
		for mute in 0.005 0.01 0.015 0.02 0.025 0.03
		do
			filename="task3-crossover_$cross-mute_$mute-rand_$rand.dat"
			python ../main.py 100 40 40 full_generational\
			proportionate max_fitness convert-genome plot\
			--cross_rate=$cross --cover_rate=0.5 --mutation=$mute --seed=$rand\
			--elite=3 --filename=$filename --stop_cond=40
		done
	done
done
for cross in 0.0 0.1 0.3 0.5 0.6 0.8 1.0
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
