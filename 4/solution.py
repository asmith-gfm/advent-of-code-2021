from board import Board


def part1(markers, boards):
    for marker in markers:
        for board in boards:
            if board.add_marker(marker):
                print("Bingo on board!")
                board.print()
                unsolved_score = board.get_unsolved()
                print(unsolved_score * int(marker))
                return


def part2(markers, boards):
    last_board: Board
    last_marker = ''
    for marker in markers:
        for board in boards:
            if board.is_in_play():
                if board.add_marker(marker):
                    last_board = board
                    last_marker = marker
    last_board.print()
    print(int(last_marker) * last_board.get_unsolved())


with open('input', 'r') as f:
    markers = []
    boards = []
    boardLines = []
    for line in f.readlines():
        if len(markers) == 0:
            markers = line.split(",")
            continue
        if len(boardLines) == 5:
            boards.append(Board(boardLines))
            boardLines = []
        stripped = line.replace("\n", "")
        if len(stripped) != 0:
            boardLines.append(stripped)
    part1(markers, boards)
    part2(markers, boards)
