set terminal postscript eps dashed color lw 2
set title "Fitness growth for different population sizes"
set xlabel "Number of generations"
set ylabel "Fitness"
set key bottom
set output "fitness_population_average.eps"
plot "data/task3-population_10-average.dat" using 1:2 title "Population size 10" with lines, \
"data/task3-population_11-average.dat" using 1:2 title "Population size 11" with lines, \
"data/task3-population_12-average.dat" using 1:2 title "Population size 12" with lines, \
"data/task3-population_13-average.dat" using 1:2 title "Population size 13" with lines, \
"data/task3-population_14-average.dat" using 1:2 title "Population size 14" with lines, \
"data/task3-population_15-average.dat" using 1:2 title "Population size 15" with lines, \
"data/task3-population_16-average.dat" using 1:2 title "Population size 16" with lines, \
"data/task3-population_17-average.dat" using 1:2 title "Population size 17" with lines, \
"data/task3-population_18-average.dat" using 1:2 title "Population size 18" with lines, \
"data/task3-population_19-average.dat" using 1:2 title "Population size 19" with lines, \
"data/task3-population_20-average.dat" using 1:2 title "Population size 20" with lines
