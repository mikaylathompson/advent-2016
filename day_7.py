import re

def is_abba(s):
    return s[0] != s[1] and s[0] == s[-1] and s[1] == s[2]

def is_aba(s):
    return s[0] != s[1] and s[0] == s[2]

def matching_aba(s1, s2):
    return is_aba(s1) and is_aba(s2) and s1[0] == s2[1] and s2[0] == s1[1]


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


def supports_ssl(line):
    hypernet = re.findall(r"\[([a-z_]+)\]", line)
    hyper_abas = []
    for word in hypernet:
        for i in range(len(word) - 2):
            if is_aba(word[i:i+3]):
                hyper_abas.append(word[i:i+3])
    remaining = re.sub(r"\[([a-z_]+)\]", " ", line)
    for i in range(len(remaining) - 2):
        cand = remaining[i:i+3]
        if is_aba(cand):
            for hyp_aba in hyper_abas:
                if matching_aba(cand, hyp_aba):
                    print(cand, hyp_aba)
                    return True
    return False


shorty = """aba[bab]xyz
xyx[xyx]xyx
aaa[kek]eke
zazbz[bzb]cdb"""
# 112 is too low
# 386 is too high
if __name__ == "__main__":
    # print(is_abba('abba'))
    # print(is_abba('aaaa'))
    # print(is_abba('oxxo'))
    # print([supports_ssl(l.strip()) for l in shorty.splitlines()])
    with open('day_7_input.txt', 'r') as f:
        print(sum([1 for line in f if supports_ssl(line.strip())]))
        # print(sum([1 for line in f if supports_tls(line.strip())]))
    # for line in shorty.split('\n'):
    #     print(supports_tls(line))