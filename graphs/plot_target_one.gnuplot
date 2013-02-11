set terminal postscript eps enhanced dashed color lw 2
set title "Fitness growth for One-Max"
set xlabel "Number of generations"
set ylabel "Fitness"
set key bottom
set output "fitness_target_one.eps"
plot "data/task5-target_one-max-average.dat" using 1:($2+$3):($2-$3) notitle with filledcurves, \
"data/task5-target_one-max-average.dat" using 1:4 title "One-Max best" with lines, \
"data/task5-target_one-max-average.dat" using 1:2 title "One-Max average" with lines
