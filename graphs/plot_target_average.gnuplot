set terminal postscript eps dashed color lw 2
set title "Fitness growth for different random targets"
set xlabel "Number of generations"
set ylabel "Fitness"
set key bottom
set output "fitness_target_average.eps"
plot "data/task5-target_1.dat" using 1:2 title "Random target #1" with lines, \
"data/task5-target_2.dat" using 1:2 title "Random target #2" with lines, \
"data/task5-target_3.dat" using 1:2 title "Random target #3" with lines, \
"data/task5-target_4.dat" using 1:2 title "Random target #4" with lines
