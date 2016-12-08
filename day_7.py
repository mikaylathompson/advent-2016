import re

def is_abba(s):
    return s[0] != s[1] and s[0] == s[-1] and s[1] == s[2]


def supports_tls(line):
    hypernet = re.findall(r"\[([a-z_]+)\]", line)
    for word in hypernet:
        for i in range(len(word) - 3):
            if is_abba(word[i:i+4]):
                return False

    remaining = re.sub(r"\[([a-z_]+)\]", " ", line)

    for i in range(len(remaining) - 3):
        if is_abba(remaining[i:i+4]):
            return True

    return False


shorty = """abba[mnop]qrst
abcd[bddb]xyyx
aaaa[qwer]tyui
ioxxoj[asdfgh]zxcvbn"""

if __name__ == "__main__":
    # print(is_abba('abba'))
    # print(is_abba('aaaa'))
    # print(is_abba('oxxo'))
    with open('day_7_input.txt', 'r') as f:
        print(sum([1 for line in f if supports_tls(line.strip())]))
    # for line in shorty.split('\n'):
    #     print(supports_tls(line))