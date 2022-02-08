from scrabbleproj.constants import POINTS, IMAGE


class Tile:
    def __init__(self, letter):
        self.letter = letter
        self.points = POINTS.get(letter)
        self.image = IMAGE.get(letter)
        self.clicked = False
        self.player_assigned = None
        self.tile_location = (0, 0)
        self.is_fixed = False

