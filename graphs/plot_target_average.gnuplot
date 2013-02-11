set terminal postscript eps enhanced dashed color lw 2
set title "Fitness growth of a random target"
set xlabel "Number of generations"
set ylabel "Fitness"
set key bottom
set output "fitness_target_random.eps"
plot "data/task5-target_all-average.dat" using 1:($2+$3):($2-$3) notitle with filledcurves, \
"data/task5-target_all-average.dat" using 1:4 title "Random target best" with lines, \
"data/task5-target_all-average.dat" using 1:2 title "Random target average" with lines
