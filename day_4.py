from collections import Counter

def generate_checksum(c):
    # ordered = sorted(commonality_list, key=lambda x: )
    lst = c.most_common()
    lst.sort(key=lambda x: x[0])
    lst.sort(key=lambda x: x[1], reverse=True)
    return ''.join([x[0] for x in lst[0:5]])

def verify_checksum(line):
    checksum = line[-6:-1]
    secret_id = line[:-7].split('-')[-1]
    letters = ''.join(line[:-7].split('-')[:-1])
    c = Counter(letters)
    if generate_checksum(c) == checksum:
        return int(secret_id)
    else:
        return 0



if __name__ == "__main__":
    with open('day_4_input.txt', 'r') as f:
        print(sum([verify_checksum(line.strip()) for line in f]))