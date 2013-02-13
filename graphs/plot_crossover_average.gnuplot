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

set title "Fitness growth for mutation rate !MUTE!"
set xlabel "Number of generations"
set ylabel "Fitness"
set key bottom right
set output "fitness_crossover_mute_!MUTE!_average.pdf"

plot "data/task3-cross_0.0-mute_!MUTE!-average.dat" using 1:2 title "Crossover 0.0" with lines, \
"data/task3-cross_0.1-mute_!MUTE!-average.dat" using 1:2 title "Crossover 0.1" with lines, \
"data/task3-cross_0.3-mute_!MUTE!-average.dat" using 1:2 title "Crossover 0.3" with lines, \
"data/task3-cross_0.5-mute_!MUTE!-average.dat" using 1:2 title "Crossover 0.5" with lines, \
"data/task3-cross_0.6-mute_!MUTE!-average.dat" using 1:2 title "Crossover 0.6" with lines, \
"data/task3-cross_0.8-mute_!MUTE!-average.dat" using 1:2 title "Crossover 0.8" with lines, \
"data/task3-cross_1.0-mute_!MUTE!-average.dat" using 1:2 title "Crossover 1.0" with lines
