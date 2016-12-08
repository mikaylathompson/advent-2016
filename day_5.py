from hashlib import md5


def hash_to_hex(s):
    return md5(s).hexdigest()


def next_index(door_id, starting_index=0):
    while True:
        hash = hash_to_hex("{}{}".format(door_id, starting_index).encode('utf-8'))
        if hash[:5]  == "00000":
            return hash[5], starting_index
        starting_index += 1
    return


if __name__ == "__main__":
    door_id = "abbhdwsy"
    password = []
    index = 0
    while len(password) < 8:
        new_char, index = next_index(door_id, index + 1)
        password.append(new_char)
        print(new_char, index)
    print(''.join(password))



