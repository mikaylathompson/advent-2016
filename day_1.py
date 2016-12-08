from enum import Enum

class Orientation(Enum):
    north = 0
    east = 1
    south = 2
    west = 3

class Walker:
    def __init__(self):
        self.ns = 0
        self.ew = 0
        self.orientation = Orientation.north
        self.visited = set()

    def turn_right(self):
        self.orientation = Orientation((self.orientation.value + 1) % 4)

    def turn_left(self):
        self.orientation = Orientation((self.orientation.value - 1) % 4)

    def walk(self, steps):
        for step in range(steps):
            self.walk_s()

    def walk_s(self):
        steps = 1
        if self.orientation == Orientation.north:
            self.ns += steps
        elif self.orientation == Orientation.south:
            self.ns -= steps
        elif self.orientation == Orientation.east:
            self.ew += steps
        elif self.orientation == Orientation.west:
            self.ew -= steps
        pos = (self.ns, self.ew)
        if pos not in self.visited:
            self.visited.add(pos)
        else:
            print("HEADQUARTERS:", pos, "distance:", self.distance())


    def distance(self):
        return abs(self.ns) + abs(self.ew)

def follow(steps):
    w = Walker()
    for step in steps.strip().split(', '):
        if step[0] == 'R':
            w.turn_right()
        else:
            w.turn_left()
        w.walk(int(step[1:]))
    return w

steps = "R4, R4, L1, R3, L5, R2, R5, R1, L4, R3, L5, R2, L3, L4, L3, R1, R5, R1, L3, L1, R3, L1, R2, R2, L2, R5, L3, L4, R4, R4, R2, L4, L1, R5, L1, L4, R4, L1, R1, L2, R5, L2, L3, R2, R1, L194, R2, L4, R49, R1, R3, L5, L4, L1, R4, R2, R1, L5, R3, L5, L4, R4, R4, L2, L3, R78, L5, R4, R191, R4, R3, R1, L2, R1, R3, L1, R3, R4, R2, L2, R1, R4, L5, R2, L2, L4, L2, R1, R2, L3, R5, R2, L3, L3, R3, L1, L1, R5, L4, L4, L2, R5, R1, R4, L3, L5, L4, R5, L4, R5, R4, L3, L2, L5, R4, R3, L3, R1, L5, R5, R1, L3, R2, L5, R5, L3, R1, R4, L5, R4, R2, R3, L4, L5, R3, R4, L5, L5, R4, L4, L4, R1, R5, R3, L1, L4, L3, L4, R1, L5, L1, R2, R2, R4, R4, L5, R4, R1, L1, L1, L3, L5, L2, R4, L3, L5, L4, L1, R3"

short_input = "R8, R4, R4, R8" # 12

# 184 is too high
if __name__ == "__main__":
    w = follow(steps)
    # w = follow(short_input)
    print(w.distance())
    # print(w.ns, w.ew, w.orientation)
