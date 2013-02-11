set terminal postscript eps dashed color lw 2
set title "Fitness growth for mutation rate !MUTE!"
set xlabel "Number of generations"
set ylabel "Fitness"
set key bottom
set output "fitness_crossover_mute_!MUTE!_average.eps"
plot "data/task3-cross_0.025-mute_!MUTE!-average.dat" using 1:2 title "Crossover 0.025" with lines, \
"data/task3-cross_0.05-mute_!MUTE!-average.dat" using 1:2 title "Crossover 0.05" with lines, \
"data/task3-cross_0.1-mute_!MUTE!-average.dat" using 1:2 title "Crossover 0.1" with lines, \
"data/task3-cross_0.2-mute_!MUTE!-average.dat" using 1:2 title "Crossover 0.2" with lines, \
"data/task3-cross_0.3-mute_!MUTE!-average.dat" using 1:2 title "Crossover 0.3" with lines, \
"data/task3-cross_0.4-mute_!MUTE!-average.dat" using 1:2 title "Crossover 0.4" with lines, \
"data/task3-cross_0.5-mute_!MUTE!-average.dat" using 1:2 title "Crossover 0.5" with lines
