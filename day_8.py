import numpy as np

class ScreenData:
    def __init__(self):
        self.width = 50
        self.height = 6
        self.data = np.zeros([self.height, self.width])

    def __str__(self):
        print("\n")
        for row in self.data:
            for cell in row:
                if cell:
                    print("X", end="")
                else:
                    print(".", end="")
            print("\n")
        print("\n")
        return ""

    def add_rect(self, x_width, y_width):
        for y in range(y_width):
            for x in range(x_width):
                self.data[y, x] = 1

    def rotate_row(self, row_id, shift_value):
        self.data[row_id] = np.roll(self.data[row_id], shift_value, axis=0)

    def rotate_col(self, col_id, shift_value):
        self.data = np.transpose(self.data)
        self.rotate_row(col_id, shift_value)
        self.data = np.transpose(self.data)



def decode(fname):
    sd = ScreenData()
    with open(fname, 'r') as f:
        for line in f:
            # print(line)
            if line[0:4] == "rect":
                x, y = line[5:].split("x")
                sd.add_rect(int(x), int(y))
            elif line[7:10] == "row":
                _, _, row, _, shift_value = line.split(' ')
                sd.rotate_row(int(row.split('=')[-1]), int(shift_value))
            else:
                _, _, col, _, shift_value = line.split(' ')
                sd.rotate_col(int(col.split('=')[-1]), int(shift_value))

    return sd

def display(screen_data):
    print(screen_data)

def count(screen_data):
    return np.count_nonzero(screen_data.data)


if __name__ == "__main__":
    print("hello")
    screen_data = decode("day_8_input.txt")
    display(screen_data)
    print(count(screen_data))