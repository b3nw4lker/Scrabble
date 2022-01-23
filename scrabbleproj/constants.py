
import pygame 

WIDTH, HEIGHT = 1000, 1000
ROWS, COLS = 15, 15
SQUARE_SIZE = 54
DECK_Y_AXIS = 870

# colours
RED = (255, 0, 0)
BLUE = (0,0,255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
ORANGE = (255, 165, 0, 255)
LIGHT_ORANGE = (255, 165, 0, 255)
LIGHT_BLUE = (173, 216, 230, 255)

#Tile Booster Images
DOUBLELETTERIMG = pygame.transform.scale(pygame.image.load('assets/doubleletter.png'), (54,54))
DOUBLEWORDIMG = pygame.transform.scale(pygame.image.load('assets/doubleword.png'), (54,54))
TRIPLELETTERIMG = pygame.transform.scale(pygame.image.load('assets/tripleletter.png'), (54,54))
TRIPLEWORDIMG = pygame.transform.scale(pygame.image.load('assets/tripleword.png'), (54,54))
STARTTILE = pygame.transform.scale(pygame.image.load('assets/starttile.png'), (54,54))

#Tile Images
ATILE = pygame.transform.scale(pygame.image.load('assets/TileA.png'), (54,54))
BTILE = pygame.transform.scale(pygame.image.load('assets/TileB.png'), (54,54))
CTILE = pygame.transform.scale(pygame.image.load('assets/TileC.png'), (54,54))
DTILE = pygame.transform.scale(pygame.image.load('assets/TileD.png'), (54,54))
ETILE = pygame.transform.scale(pygame.image.load('assets/TileE.png'), (54,54))
FTILE = pygame.transform.scale(pygame.image.load('assets/TileF.png'), (54,54))
GTILE = pygame.transform.scale(pygame.image.load('assets/TileG.png'), (54,54))
HTILE = pygame.transform.scale(pygame.image.load('assets/TileH.png'), (54,54))
ITILE = pygame.transform.scale(pygame.image.load('assets/TileI.png'), (54,54))
JTILE = pygame.transform.scale(pygame.image.load('assets/TileJ.png'), (54,54))
KTILE = pygame.transform.scale(pygame.image.load('assets/TileK.png'), (54,54))
LTILE = pygame.transform.scale(pygame.image.load('assets/TileL.png'), (54,54))
MTILE = pygame.transform.scale(pygame.image.load('assets/TileM.png'), (54,54))
NTILE = pygame.transform.scale(pygame.image.load('assets/TileN.png'), (54,54))
OTILE = pygame.transform.scale(pygame.image.load('assets/TileO.png'), (54,54))
PTILE = pygame.transform.scale(pygame.image.load('assets/TileP.png'), (54,54))
QTILE = pygame.transform.scale(pygame.image.load('assets/TileQ.png'), (54,54))
RTILE = pygame.transform.scale(pygame.image.load('assets/TileR.png'), (54,54))
STILE = pygame.transform.scale(pygame.image.load('assets/TileS.png'), (54,54))
TTILE = pygame.transform.scale(pygame.image.load('assets/TileT.png'), (54,54))
UTILE = pygame.transform.scale(pygame.image.load('assets/TileU.png'), (54,54))
VTILE = pygame.transform.scale(pygame.image.load('assets/TileV.png'), (54,54))
WTILE = pygame.transform.scale(pygame.image.load('assets/TileW.png'), (54,54))
XTILE = pygame.transform.scale(pygame.image.load('assets/TileX.png'), (54,54))
YTILE = pygame.transform.scale(pygame.image.load('assets/TileY.png'), (54,54))
ZTILE = pygame.transform.scale(pygame.image.load('assets/TileZ.png'), (54,54))
BLANK = pygame.transform.scale(pygame.image.load('assets/TileBlank.png'), (54,54))


TILE_VALUES = {
            "A": {"qty": 9, "value": 1},
            "B": {"qty": 2, "value": 3},
            "C": {"qty": 2, "value": 3},
            "D": {"qty": 4, "value": 2},
            "E": {"qty": 12, "value": 1},
            "F": {"qty": 2, "value": 4},
            "G": {"qty": 3, "value": 2},
            "H": {"qty": 2, "value": 1},
            "I": {"qty": 9, "value": 1},
            "J": {"qty": 1, "value": 8},
            "K": {"qty": 1, "value": 5},
            "L": {"qty": 4, "value": 1},
            "M": {"qty": 2, "value": 3},
            "N": {"qty": 6, "value": 1},
            "O": {"qty": 8, "value": 1},
            "P": {"qty": 2, "value": 3},
            "Q": {"qty": 1, "value": 10},
            "R": {"qty": 6, "value": 1},
            "S": {"qty": 4, "value": 1},
            "T": {"qty": 6, "value": 1},
            "U": {"qty": 4, "value": 1},
            "V": {"qty": 2, "value": 4},
            "W": {"qty": 2, "value": 4},
            "X": {"qty": 1, "value": 8},
            "Y": {"qty": 2, "value": 4},
            "Z": {"qty": 1, "value": 10},
            "BLANK": {"qty": 2}
        }

