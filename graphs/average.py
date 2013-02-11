#!/usr/bin/python

import sys

def average(files):
    average_dat = {}
    sum_avg = {}
    for file in files:
        with open(file, 'r') as f:
            for line in f:
                data = line.split('\t')
                x_val = int(data[0])
                if x_val not in average_dat:
                    average_dat[x_val] = 0.0
                    sum_avg[x_val] = 0.0
                average_dat[x_val] += 1.0
                sum_avg[x_val] += float(data[3])
    for key, val in average_dat.items():
        sum_avg[key] = sum_avg[key] / val
    return sum_avg

def full_average(files):
    average_dat = {}
    sum_avg = {}
    for file in files:
        with open(file, 'r') as f:
            for line in f:
                data = line.split('\t')
                x_val = int(data[0])
                if x_val not in average_dat:
                    average_dat[x_val] = 0.0
                    sum_avg[x_val] = [0.0, 0.0, 0.0]
                average_dat[x_val] += 1.0
                sum_avg[x_val][0] += float(data[1])
                sum_avg[x_val][1] += float(data[2])
                sum_avg[x_val][2] += float(data[3])
    for key, val in average_dat.items():
        sum_avg[key] = (sum_avg[key][0] / val, sum_avg[key][1] / val,
                sum_avg[key][2] / val)
    return sum_avg

def write_full_average(filename, data):
    with open(filename, 'w') as f:
        for key, val in data.items():
            f.write('{}\t{}\t{}\t{}\n'.format(key, val[0], val[1], val[2]))

def write_average(filename, data):
    with open(filename, 'w') as f:
        for key, val in data.items():
            f.write('{}\t{}\n'.format(key, val))

def average_pop(size, files):
    average_data = average(files)
    write_average('task3-population_{}-average.dat'.format(size), average_data)

def average_crossover(cross, mute, files):
    data = average(files)
    write_average('task3-cross_{}-mute_{}-average.dat'.format(cross, mute), data)

def average_selection(select, files):
    data = average(files)
    write_average('task4-select_{}-average.dat'.format(select), data)

def average_target(target, files):
    data = full_average(files)
    write_full_average('task5-target_{}-average.dat'.format(target), data)

def main():
    command = sys.argv[1]
    if command == 'pop':
        average_pop(sys.argv[2], sys.argv[3:])
    elif command == 'cross':
        average_crossover(sys.argv[2], sys.argv[3], sys.argv[4:])
    elif command == 'selection':
        average_selection(sys.argv[2], sys.argv[3:])
    elif command == 'target':
        average_target(sys.argv[2], sys.argv[3:])


if __name__ == '__main__':
    main()
