from hashlib import md5


def hash_to_hex(s):
    return md5(s).hexdigest()


def next_index(door_id, starting_index=0):
    while True:
        hash = hash_to_hex("{}{}".format(door_id, starting_index).encode('utf-8'))
        if hash[:5] == "00000":
            print(hash[:7])
            return hash[5], hash[6], starting_index
        starting_index += 1
    return


if __name__ == "__main__":
    door_id = "abbhdwsy"
    password = [None] * 8
    # door_id = "abc"
    index = 0
    # while len(password) < 8:
    while not all(password):
        char_pos, new_char, index = next_index(door_id, index + 1)
        print(password)
        print(char_pos, new_char)
        try:
            if password[int(char_pos)] is None:
                password[int(char_pos)] = new_char
                print(char_pos, new_char, index)
                print(password)
        except IndexError:
            next
        except ValueError:
            next

        # except:
        #     pass
    print(''.join(password))



