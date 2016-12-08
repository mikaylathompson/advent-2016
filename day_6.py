from collections import Counter

def decode(fname):
    with open(fname, 'r') as f:
        counters = []
        for i, line in enumerate(f):
            if i == 0:
                for letter in line.strip():
                    counters.append(Counter())
            for j, letter in enumerate(line.strip()):
                counters[j][letter] += 1

    for c in counters:
        print(c.most_common(1))

    return

if __name__ == "__main__":
    decode("day_6_input.txt")