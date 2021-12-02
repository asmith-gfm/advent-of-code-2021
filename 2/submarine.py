class Submarine:
    def __init__(self):
        self.distance = 0
        self.depth = 0
        self.directionHandlers = {
            "forward": self._forward,
            "up": self._up,
            "down": self._down
        }

    def drive(self, direction, length):
        self.directionHandlers[direction](length)

    def _forward(self, length):
        self.distance += length

    def _up(self, length):
        self.depth -= length

    def _down(self, length):
        self.depth += length


class AimingSubmarine(Submarine):

    def __init__(self):
        super().__init__()
        self.aim = 0

    def _forward(self, length):
        self.distance += length
        self.depth += length * self.aim

    def _up(self, length):
        self.aim -= length

    def _down(self, length):
        self.aim += length
