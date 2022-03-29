import pygame
from scrabbleproj.constants import BLACK, ORANGE, SCRABBLEBACKGROUND, WIDTH, HEIGHT, WHITE
from scrabbleproj.game_manager import GameManager
from scrabbleproj.words import Words

#Ben Walker 
#Scrabble Project for NEA

# Example Link - https://github.com/cheukyin699/py-scrabble

FPS = 60

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Scrabble')



def play():
    run = True
    clock = pygame.time.Clock()
    game_manager = GameManager(WIN)
    words = Words()

    while run:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                main_menu()
            else:
                # print("Event being called")
                game_manager.handle(event)

            # Drawing the state
            # screen.fill((0, 0, 0))
            game_manager.draw()
            
            pygame.display.flip()

            # Updating the state
            game_manager.update(clock.tick(60) / 1e3)
    
    pygame.quit()

def rules():
    WIN.fill(BLACK)
    run = True
    while run is True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                main_menu()
        pygame.display.update()
        
def main_menu():
    WIN.blit(SCRABBLEBACKGROUND,(0,0))
    run = True
    while run is True:
        MENU_MOUSE_POS = pygame.mouse.get_pos()
        

        pygame.font.init()
        font = pygame.font.Font('freesansbold.ttf', 140)
        playtext = font.render(("  PLAY"),True, WHITE)
        WIN.blit(playtext,(300,100,150,500))
        playbutton = pygame.Rect(300,100, 500,120)
        pygame.draw.rect(WIN, WHITE, playbutton, 1,)
        
        font = pygame.font.Font('freesansbold.ttf', 140)
        quittext = font.render(("  QUIT"),True, WHITE)
        WIN.blit(quittext,(300,500,170,500))
        quitbutton = pygame.Rect(300,500, 500,120)
        pygame.draw.rect(WIN, WHITE, quitbutton, 1,)
        
        font = pygame.font.Font('freesansbold.ttf', 140)
        rulestext = font.render(("RULES"),True, WHITE)
        WIN.blit(rulestext,(300,300,170,500))
        rulesbutton = pygame.Rect(300,300, 500,120)
        pygame.draw.rect(WIN, WHITE, rulesbutton, 1,)
        
    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if playbutton.collidepoint(MENU_MOUSE_POS):
                    play()
                if rulesbutton.collidepoint(MENU_MOUSE_POS):
                    rules()
                if quitbutton.collidepoint(MENU_MOUSE_POS):
                    pygame.quit()
        
        pygame.display.update()
    
main_menu()      
            




