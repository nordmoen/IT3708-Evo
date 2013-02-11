set terminal postscript eps dashed color lw 2
set title "Fitness growth for different selection mechanisms"
set xlabel "Number of generations"
set ylabel "Fitness"
set key bottom
set output "fitness_selection_average.eps"
plot "data/task4-select_proportionate-average.dat" using 1:2 title "Fitness proportionate" with lines, \
"data/task4-select_sigma-average.dat" using 1:2 title "Sigma scaling" with lines, \
"data/task4-select_rank-average.dat" using 1:2 title "Rank scaling" with lines, \
"data/task4-select_tournament-average.dat" using 1:2 title "Tournament selection" with lines
