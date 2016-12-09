
def is_valid(a, b, c):
    return a + b > c


def is_valid_line(line):
    vals = [int(x) for x in line.strip().split()]
    return is_valid(*sorted(vals))


with open("day_3_input.txt", 'r') as f:
    truth = [1 for line in f if is_valid_line(line)]
    print(sum(truth))