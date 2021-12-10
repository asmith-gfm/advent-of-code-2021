lines = []
overlap = []


class Line:

    def __init__(self, line):
        coords = line.split(" -> ")
        self._x1 = coords[0].split(",")[0]
        self._x2 = coords[1].split(",")[0]
        self._y1 = coords[0].split(",")[1]
        self._y2 = coords[1].split(",")[1]

    def overlaps(self, line):
        return False


with open('input', 'r') as f:
    for line in f.readlines():
        Line(line)
