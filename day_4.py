from collections import Counter
import string

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


def shift(plaintext, shift, alphabet=string.ascii_lowercase):
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    cipher = plaintext.maketrans(alphabet, shifted_alphabet)
    return plaintext.translate(cipher)


def decode(line):
    if not verify_checksum(line):
        return
    secret_id = verify_checksum(line)
    letters = ''.join(line[:-7].split('-')[:-1])
    shift_val = secret_id % 26
    translated = shift(letters, shift_val)
    if 'north' in translated:
        print(secret_id, translated)



if __name__ == "__main__":
    # Part 1
    # with open('day_4_input.txt', 'r') as f:
    #     print(sum([verify_checksum(line.strip()) for line in f]))
    # Part 2
    with open('day_4_input.txt', 'r') as f:
        for line in f:
            decode(line.strip())
