
class TileBoost:
    def __init__(self):
        # self.row = row
        # self.col = col
        # self.colour = colour
        self.double_letter = True
        self.double_word = False
        self.triple_letter = False
        self.triple_word = False
        self.starttile = False
        
        self.x = 0
        self.y = 0

    def make_double_letter(self):
        self.double_letter = True
    
    def make_double_word(self):
        self.double_word = True
        
    def make_triple_letter(self):
        self.triple_letter = True
    
    def make_triple_word(self):
        self.triple_word = True
    
    def create_tile_booster(self):
        pass

    def draw(self, win):
        if self.double_letter:
            pass
        if self.double_word:
            pass
            
        if self.triple_letter:
            pass
            
        if self.triple_word:
            pass
            
        if self.start_tile:
            pass
        