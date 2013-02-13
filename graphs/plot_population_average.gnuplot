set terminal pdfcairo  rounded

# Line style for axes
set style line 80 lt rgb "#808080"

# Line style for grid
set style line 81 lt 0  # dashed
set style line 81 lt rgb "#808080"  # grey

set grid back linestyle 81
set border 3 back linestyle 80 # Remove border on top and right.  These
             # borders are useless and make it harder
             # to see plotted lines near the border.
    # Also, put it in grey; no need for so much emphasis on a border.
set xtics nomirror
set ytics nomirror

#set log x
#set mxtics 10    # Makes logscale look good.

# Line styles: try to pick pleasing colors, rather
# than strictly primary colors or hard-to-see colors
# like gnuplot's default yellow.  Make the lines thick
# so they're easy to see in small plots in papers.
set style line 1 lt rgb "#A00000" lw 2 pt 1
set style line 2 lt rgb "#00A000" lw 2 pt 6
set style line 3 lt rgb "#5060D0" lw 2 pt 2
set style line 4 lt rgb "#F25900" lw 2 pt 9

set title "Fitness growth for different population sizes"
set xlabel "Number of generations"
set ylabel "Fitness"
set key bottom right
set output "fitness_population_average.pdf"

plot "data/task3-population_10-average.dat" using 1:2 title "Population size 10" with lines ls 1, \
"data/task3-population_20-average.dat" using 1:2 title "Population size 20" with lines ls 2, \
"data/task3-population_30-average.dat" using 1:2 title "Population size 30" with lines ls 3, \
"data/task3-population_40-average.dat" using 1:2 title "Population size 40" with lines ls 4, \
"data/task3-population_50-average.dat" using 1:2 title "Population size 50" with lines, \
"data/task3-population_60-average.dat" using 1:2 title "Population size 60" with lines, \
"data/task3-population_70-average.dat" using 1:2 title "Population size 70" with lines, \
"data/task3-population_80-average.dat" using 1:2 title "Population size 80" with lines, \
"data/task3-population_90-average.dat" using 1:2 title "Population size 90" with lines, \
"data/task3-population_100-average.dat" using 1:2 title "Population size 100" with lines
