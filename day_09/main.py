
class Marble:
    def __init__(self, value):
        self.prev = None
        self.next = None
        self.v = value


class MarbleList:
    def __init__(self):
        # Marble 2
        self.current = Marble(2)
        self.current.prev = Marble(0)
        self.current.next = Marble(1)

        # Marble 0
        self.current.prev.prev = self.current.next
        self.current.prev.next = self.current

        # Marble 1
        self.current.next.prev = self.current
        self.current.next.next = self.current.prev

    def add_marble(self, turn):
        # Add new marble
        marble_next = self.current.next.next
        self.current = Marble(turn)
        self.current.next = marble_next
        self.current.prev = marble_next.prev

        # Add new current marble to relations
        marble_next.prev.next = self.current
        marble_next.prev = self.current

    def extract_marble(self) -> int:
        self.current = self.current.prev.prev.prev.prev.prev.prev
        score = self.current.prev.v
        self.current.prev = self.current.prev.prev
        self.current.prev.next = self.current

        return score


def read_and_process(data_path: str):
    """
    Create list of input integers
    """

    f = open(data_path, "r")
    out = None
    for x in f:
        out = [c for c in x.strip().split()]
    return int(out[0]), int(out[6])


def solution(multiplier=1, data_path="input"):
    """
    Highest score after the last marble is played
    """
    players, last_marble = read_and_process(data_path)
    points = [0] * players
    turn = 3
    marbles = MarbleList()

    while turn <= multiplier * last_marble:
        if turn % 23 == 0:
            points_gain = marbles.extract_marble()
            points[turn % players] += points_gain + turn
        else:
            marbles.add_marble(turn)
        turn += 1

    return max(points)


if __name__ == "__main__":

    print(f"Highest score is {solution()}")
    print(f"Highest score if multiplied number of marbles is {solution(100)}")
