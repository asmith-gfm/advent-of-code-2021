class InvalidBoard(Exception):
    pass


class Board:

    def __init__(self, lines):
        self._board = []
        self._size = len(lines)
        self._bingod = False
        for line in lines:
            split = line.split()
            if len(split) != self._size:
                raise InvalidBoard("Expected board to be square, it was not.")
            spaces = list(map(Space, split))
            self._board.append(spaces)

    def add_marker(self, number):
        for row in range(0, self._size):
            for column in range(0, self._size):
                space = self.get_space(row, column)
                if space.get_number() == number:
                    space.mark()
                    if self.check_bingo(row, column):
                        self._bingod = True
                        return True
        return False

    def check_bingo(self, row, column):
        row_count = 0
        column_count = 0
        top_diagonal_count = 0
        bottom_diagonal_count = 0
        for i in range(0, self._size):
            if not self.get_space(row, i).is_marked():
                row_count = 0
            else:
                row_count += 1
            if not self.get_space(i, column).is_marked():
                column_count = 0
            else:
                column_count += 1
            if not self.get_space(i, i).is_marked():
                top_diagonal_count = 0
            else:
                top_diagonal_count += 1
            if not self.get_space(i, self._size - (i + 1)).is_marked():
                bottom_diagonal_count = 0
            else:
                bottom_diagonal_count += 1
        if row_count == self._size \
                or column_count == self._size \
                or top_diagonal_count == self._size \
                or bottom_diagonal_count == self._size:
            return True

    def print(self):
        for row in range(0, self._size):
            line = ''
            for column in range(0, self._size):
                space = self.get_space(row, column)
                line += '<' + space.get_number() + ">" if space.is_marked() else ' ' + space.get_number() + ' '
            print(line)
            print('')

    def get_unsolved(self):
        total = 0
        for row in range(0, self._size):
            for column in range(0, self._size):
                if not self.get_space(row, column).is_marked():
                    total += int(self.get_space(row, column).get_number())
        return total

    def get_space(self, row, column):
        return self._board[row][column]

    def is_in_play(self):
        return not self._bingod


class Space:

    def __init__(self, number):
        self._number = number
        self._marked = False

    def mark(self):
        self._marked = True

    def is_marked(self):
        return self._marked

    def get_number(self):
        return self._number
