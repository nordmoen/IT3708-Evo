#!/usr/bin/python

import sys

def parse_file(file):
    result = []
    with open(file, 'r') as f:
        for line in f:
            dat = line.split(':')
            result.append(eval(dat[1]))
    return result

def check_redistr(data):
    data = data[::-1]
    result = []
    for i in range(50):
        for j in range(i + 1, 50):
            equal = True
            for k in range(len(data[i])):
                if data[i][k] > 0 and data[j][k] == 0:
                    equal = False
                    break
                elif data[i][k] == 0 and data[j][k] > 0:
                    equal = False
                    break
            if equal:
                result.append('{} == {}'.format(100 - i, 100 - j))
    return result

def main():
    file = sys.argv[1]
    content = parse_file(file)
    res = check_redistr(content)
    print '\n'.join(res)

if __name__ == '__main__':
    main()
