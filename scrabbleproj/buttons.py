
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
            
            
    def combine_text(win,text,position,font,max_width,colour):
        paragraph = [word.split(' ') for word in text.splitlines()]  #list of words
        space = font.size(' ')[0]  # the width of space 
        x, y = position # pos is tuple version of coords 
        for line in paragraph:
            for word in line:
                word_surface = font.render(word, 0, colour)
                word_width, word_height = word_surface.get_size()
                if x + word_width >= max_width:
                    x = position[0]  # reset the x
                    y += word_height  # starts text on new row
                win.blit(word_surface, (x, y))
                x += word_width + space
            x = position[0]  # resets x again
            y += word_height  # begins on new row        
    
    # class combine_text():
    #     def __init__(self,win,text,position,font,max_width,colour):
    #         self.win = win
    #         self.text = text
    #         self.position = position
    #         self.font = font 
    #         self.max_width = max_width
    #         self.colour = colour
        
        
        
        
        
        
        


swapbutton = Button((ORANGE) , 620, 870, 110, 40, (f"Swap [7]"))
endturn = Button((ORANGE) , 400, 870, 100, 40,  'Play')
skipturn = Button((ORANGE) , 510, 870, 100, 40, 'Skip Turn')
whowon = Button((ORANGE), 850, 650, 150, 40,  (f'Player 1 wins'))




               





