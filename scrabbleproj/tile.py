from re import A
from scrabbleproj.constants import POINTS, IMAGE



class Tile:
    def __init__(self, letter):
        self.letter = letter
        self.points = POINTS.get(letter, 0)
        self.image = IMAGE.get(letter, IMAGE.get("TileEmpty"))
        self.clicked = False
        self.player_assigned = None
        self.tile_location = (0, 0)
        self.is_fixed = False
        self.booster_value = 0
        self.disabled = False
        

    def update_tile_image(self, letter):
        self.image = IMAGE.get(letter)
        
        
        
    