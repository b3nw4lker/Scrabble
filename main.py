from pickle import TRUE
import pygame
from scrabbleproj.constants import WIDTH, HEIGHT
from scrabbleproj.game_manager import GameManager

#Ben Walker 
#Scrabble Project for NEA

# Example Link - https://github.com/cheukyin699/py-scrabble

FPS = 60

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Scrabble')


def main():
    run = True
    clock = pygame.time.Clock()
    game_manager = GameManager(WIN)

    # Move all this into a player state class and then instantiate that class in the while True Loop
    while run:
        # clock.tick(FPS)
        #
        # for event in pygame.event.get():
        #     if event.type == pygame.QUIT:
        #         run = False
        #
        #     if event.type == pygame.MOUSEBUTTONDOWN:
        #         mouse_position = pygame.mouse.get_pos()
        #         print(mouse_position)
        #
        # pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
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

main()