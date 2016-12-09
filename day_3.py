import numpy as np

def is_valid(a, b, c):
    return a + b > c


def is_valid_line(line):
    vals = [int(x) for x in line.strip().split()]
    return is_valid(*sorted(vals))


def count_valid_trianges(l1, l2, l3):
    vals = list(map(list, zip(*[[int(x) for x in line.strip().split()] for line in [l1, l2, l3]])))
    return sum([1 for row in vals if is_valid(*sorted(row))])


with open("day_3_input.txt", 'r') as f:
    # Part 1
    # truth = [1 for line in f if is_valid_line(line)]
    # print(sum(truth))

    # Part 2
    n_valid_tris = 0
    while True:
        line1 = f.readline()
        line2 = f.readline()
        line3 = f.readline()
        if not line3:
            print(n_valid_tris)
            break
        n_valid_tris += count_valid_trianges(line1, line2, line3)
