import re

decompress_code = r"\((?P<length>\d+)x(?P<reps>\d+)\)"

def decode(str):
    if str == "":
        return 0
    if re.match("\s", str):
        return decode(str[1:])
    if re.match(decompress_code, str):
        m = re.match(decompress_code, str)
        length = int(m.group('length'))
        reps = int(m.group('reps'))
        return (decode(str[len(m.group(0)):len(m.group(0)) + length]) * reps) +\
                        decode(str[len(m.group(0)) + length:])
    else:
        return 1 + decode(str[1:])

samples = """ADVENT
A(1x5)BC
(3x3)XYZ
A(2x2)BCD(2x2)EFG
(6x1)(1x3)A
X(8x2)(3x3)ABCY
"""

if __name__ == "__main__":
    for line in samples.splitlines():
        print(decode(line.strip()))
    print()
    with open('day_9_input.txt', 'r') as f:
        all_text = f.read().replace(" ", "")
        print(decode(all_text))
