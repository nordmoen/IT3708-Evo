#!/bin/bash

function randomBitString () {
	rand=< /dev/urandom tr -dc 0-1 | head -c40
	rand=`echo $rand | cut -b 40`
	echo $rand
}

target1=$(randomBitString)
target2=$(randomBitString)
target3=$(randomBitString)
target4=$(randomBitString)

for run in 1 2 3 4 5 6 7 8 9 10
do
	rand=$RANDOM
	for target in $target1 $target2 $target3 $target4
	do
		filename="task5-target_$target-rand_$rand.dat"
		python ../main.py 100 40 40 full_generational\
		tournament random_fitness convert-genome plot\
		--cross_rate=1.0 --cover_rate=0.5 --mutation=0.01 --seed=$rand\
		--elite=3 --filename=$filename --stop_cond=40\
		--target=$target --k=10 --e=0.05
	done
	filename="task5-target-none-rand_$rand.dat"
	python ../main.py 100 40 40 full_generational\
	tournament max_fitness convert-genome plot\
	--cross_rate=1.0 --cover_rate=0.5 --mutation=0.01 --seed=$rand\
	--elite=3 --filename=$filename --stop_cond=40 --k=10 --e=0.05
done

for target in $target1 $target2 $target3 $target4
do
	python average.py target $target task5-target_$target-rand_*
	rm task5-target_$target-rand_*
done

python average.py target all task5-target_*

python average.py target one-max task5-target-none-rand_*
rm task5-target-none-rand_*

mv task5-target_all-average.dat data/
mv task5-target_one-max-average.dat data/

gnuplot < plot_target_average.gnuplot
gnuplot < plot_target_one.gnuplot
