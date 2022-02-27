import pygame

WIDTH, HEIGHT = 1000, 1000
ROWS, COLS = 15, 15
SQUARE_SIZE = 54
DECK_Y_AXIS = 870

# colours
RED = (255, 0, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
ORANGE = (255, 165, 0, 255)
LIGHT_ORANGE = (255, 165, 0, 255)
LIGHT_BLUE = (173, 216, 230, 255)

# Tile Booster Images
DOUBLELETTERIMG = pygame.transform.scale(pygame.image.load('assets/doubleletter.png'), (54, 54))
DOUBLEWORDIMG = pygame.transform.scale(pygame.image.load('assets/doubleword.png'), (54, 54))
TRIPLELETTERIMG = pygame.transform.scale(pygame.image.load('assets/tripleletter.png'), (54, 54))
TRIPLEWORDIMG = pygame.transform.scale(pygame.image.load('assets/tripleword.png'), (54, 54))
STARTTILE = pygame.transform.scale(pygame.image.load('assets/starttile.png'), (54, 54))

POINTS = {"A": 1, "C": 3, "B": 3, "E": 1, "D": 2, "G": 2,
          "F": 4, "I": 1, "H": 4, "K": 5, "J": 8, "M": 3,
          "L": 1, "O": 1, "N": 1, "Q": 10, "P": 3, "S": 1,
          "R": 1, "U": 1, "T": 1, "W": 4, "V": 4, "Y": 4,
          "X": 8, "Z": 10, "BLANK": 0}

# Letter distribution should make 100there is 100 here so i think it may be running the distribution more than once as only 
DISTRIBUTION = {"BLANK": 2, "E": 12, "A": 9, "I": 9, "O": 8, "N": 6, "R": 6, "T": 6,     
                "L": 4, "S": 4, "U": 4, "D": 4, "G": 3, "B": 2, "C": 2, "M": 2,
                "P": 2, "F": 2, "H": 2, "V": 2, "W": 2, "Y": 2, "K": 1, "J": 1,
                "X": 1, "Q": 1, "Z": 1}

IMAGE = {
    "A": pygame.transform.scale(pygame.image.load('assets/TileA.png'), (54, 54)),
    "B": pygame.transform.scale(pygame.image.load('assets/TileB.png'), (54, 54)),
    "C": pygame.transform.scale(pygame.image.load('assets/TileC.png'), (54, 54)),
    "D": pygame.transform.scale(pygame.image.load('assets/TileD.png'), (54, 54)),
    "E": pygame.transform.scale(pygame.image.load('assets/TileE.png'), (54, 54)),
    "F": pygame.transform.scale(pygame.image.load('assets/TileF.png'), (54, 54)),
    "G": pygame.transform.scale(pygame.image.load('assets/TileG.png'), (54, 54)),
    "H": pygame.transform.scale(pygame.image.load('assets/TileH.png'), (54, 54)),
    "I": pygame.transform.scale(pygame.image.load('assets/TileI.png'), (54, 54)),
    "J": pygame.transform.scale(pygame.image.load('assets/TileJ.png'), (54, 54)),
    "K": pygame.transform.scale(pygame.image.load('assets/TileK.png'), (54, 54)),
    "L": pygame.transform.scale(pygame.image.load('assets/TileL.png'), (54, 54)),
    "M": pygame.transform.scale(pygame.image.load('assets/TileM.png'), (54, 54)),
    "N": pygame.transform.scale(pygame.image.load('assets/TileN.png'), (54, 54)),
    "O": pygame.transform.scale(pygame.image.load('assets/TileO.png'), (54, 54)),
    "P": pygame.transform.scale(pygame.image.load('assets/TileP.png'), (54, 54)),
    "Q": pygame.transform.scale(pygame.image.load('assets/TileQ.png'), (54, 54)),
    "R": pygame.transform.scale(pygame.image.load('assets/TileR.png'), (54, 54)),
    "S": pygame.transform.scale(pygame.image.load('assets/TileS.png'), (54, 54)),
    "T": pygame.transform.scale(pygame.image.load('assets/TileT.png'), (54, 54)),
    "U": pygame.transform.scale(pygame.image.load('assets/TileU.png'), (54, 54)),
    "V": pygame.transform.scale(pygame.image.load('assets/TileV.png'), (54, 54)),
    "W": pygame.transform.scale(pygame.image.load('assets/TileW.png'), (54, 54)),
    "X": pygame.transform.scale(pygame.image.load('assets/TileX.png'), (54, 54)),
    "Y": pygame.transform.scale(pygame.image.load('assets/TileY.png'), (54, 54)),
    "Z": pygame.transform.scale(pygame.image.load('assets/TileZ.png'), (54, 54)),
    "BLANK": pygame.transform.scale(pygame.image.load('assets/TileBlank.png'), (54, 54)),
    "TileEmpty": pygame.transform.scale(pygame.image.load('assets/TileEmpty.png'), (54, 54)),
}

BONUS_TILE_LOCATIONS = {
    TRIPLEWORDIMG: [(0, 0), (378, 0), (756, 0), (0, 756), (378, 756), (756, 756), (0, 378), (756, 378)],
    TRIPLELETTERIMG: [(54, 270), (54, 486), (270, 54), (270, 270), (270, 486), (270, 702), (486, 54), (486, 270),
                        (486, 486), (486, 702), (702, 270), (702, 486)],
    DOUBLELETTERIMG: [(0, 162), (0, 594), (108, 324), (108, 432), (162, 0), (162, 378), (162, 756), (324, 108),
                        (324, 324), (324, 432), (324, 648), (378, 162), (378, 594), (432, 108), (432, 324), (432, 432),
                        (432, 648), (594, 0), (594, 378), (594, 756), (648, 324), (648, 432), (756, 162), (756, 594)],
    DOUBLEWORDIMG: [(54, 54), (54, 702), (108, 108), (108, 648), (162, 162), (162, 594), (216, 216), (216, 540),
                      (540, 216), (540, 540), (594, 162), (594, 594), (648, 108), (648, 648), (702, 54), (702, 702)],
    STARTTILE: [(378, 378)]
}

# BOARD_LIST = []           
