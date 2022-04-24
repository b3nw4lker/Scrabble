
from ast import Or
import pygame
from scrabbleproj.constants import ORANGE, WHITE



class Button():
    def __init__(self, colour, x,y,width,height, text=''):
        self.colour = colour
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.swap_count = 7

    def draw_button(self,win,outline=None):
        #Call this method to draw the button on the screen
        if outline:
            pygame.draw.rect(win, outline, (self.x-2,self.y-2,self.width+4,self.height+4),0)
            
        pygame.draw.rect(win, self.colour, (self.x,self.y,self.width,self.height),0)
        
        if self.text != '':
            font = pygame.font.SysFont('comicsans', 20)
            text = font.render(self.text, 1, (0,0,0))
            win.blit(text, (self.x + (self.width/2 - text.get_width()/2), self.y + (self.height/2 - text.get_height()/2)))

    def isOver(self, pos):
        #Pos is the mouse position or a tuple of (x,y) coordinates
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True
            
    


swapbutton = Button((ORANGE) , 620, 870, 110, 40, (f"Swap [7]"))
endturn = Button((ORANGE) , 400, 870, 100, 40,  'Play')
skipturn = Button((ORANGE) , 510, 870, 100, 40, 'Skip Turn')




               





