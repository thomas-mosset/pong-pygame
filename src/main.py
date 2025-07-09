"""
Main file for the game.
"""
import os
import pygame
import settings # import all settings from the settings.py file

image_path = os.path.join(os.path.dirname(__file__), '..', 'assets', 'images', 'freepik__bg.png')
background = pygame.image.load(image_path)
background = pygame.transform.scale(background, (settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT)) # rescale and adapt the background to my screen size


# game init
pygame.init()

# game's screen
screen = pygame.display.set_mode((settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT))
pygame.display.set_caption(settings.GAME_TITLE)

# game's FPS
clock = pygame.time.Clock()

# main game's loop
running = True
while running:
    clock.tick(settings.FPS) # limit the game to 60 FPS
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False # quit the game, if player close the game screen
    
    # fill the screen with our image
    screen.blit(background, (0, 0))
    
    # update / refresh the display of the game
    pygame.display.flip()

# quit pygame
pygame.quit()