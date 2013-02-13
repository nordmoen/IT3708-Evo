#!/bin/bash

rand=26150
for battle in 5 20
do
	for r in 0.0 0.5 1.0
	do
		for l in 0.0 0.5 1.0
		do
			filename="blotto-battles_$battle-r_$r-l_$l.dat"
			
			python ../main.py 100 $battle 30 full_generational\
			tournament blotto_fit convert-blotto plotto\
			--cross_rate=0.8 --cover_rate=0.5 --mutation=0.01 --seed=$rand\
			--elite=3 --filename=$filename\
			--k=10 --e=0.05 --r=$r --l=$l
			
		done
	done
done

mv "blotto-battles_"* blotto/

echo "Random number used: $rand"
