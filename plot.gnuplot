set terminal postscript eps solid color lw 2
set title "Fitness growth over several generations"
set xlabel "Number of generations"
set ylabel "Fitness"
set output "fitness.eps"
plot "output.dat" using 1:2:3 title "Average" with lines, \
"output.dat" using 1:2:3 notitle with yerrorbars, \
"output.dat" using 1:4 title "Best individual" with lines
