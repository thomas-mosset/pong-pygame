"""
Main file for the game.
"""
import os
import pygame
import settings # import all settings from the settings.py file

from game import Paddle, Ball

image_path = os.path.join(os.path.dirname(__file__), '..', 'assets', 'images', 'freepik__bg.png')
background = pygame.image.load(image_path)
background = pygame.transform.scale(background, (settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT)) # rescale and adapt the background to my screen size


# game init
pygame.init()

left_player = Paddle(50, settings.SCREEN_HEIGHT // 2 - 50)
right_player = Paddle(1210, settings.SCREEN_HEIGHT // 2 - 50)
ball = Ball(settings.SCREEN_WIDTH // 2 - 10, settings.SCREEN_HEIGHT // 2 - 10)

# game's screen
screen = pygame.display.set_mode((settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT))
pygame.display.set_caption(settings.GAME_TITLE)

# game's FPS
clock = pygame.time.Clock()

# main game's loop
running = True
while running:
    clock.tick(settings.FPS) # limit the game to 60 FPS
    
    # keys management
    keys = pygame.key.get_pressed()
    if keys[pygame.K_z]: # Z keyboard key
        left_player.move_up()
    
    if keys[pygame.K_s]: # S keyboard key
        left_player.move_down()
    
    if keys[pygame.K_UP]: # top arrow keyboard key
        right_player.move_up()
    
    if keys[pygame.K_DOWN]: # bottom arrow keyboard key
        right_player.move_down()
        
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False # quit the game, if player close the game screen
    
    # fill the screen with our image
    screen.blit(background, (0, 0))
    
    # ball movement / management
    ball.update()
    ball.bounce_on_walls()
    if ball.rect.left <= 0 or ball.rect.right >= settings.SCREEN_WIDTH:
        ball.reset()
    
    # display player
    left_player.draw(screen)
    right_player.draw(screen)
    
    # display ball
    ball.draw(screen)
    
    # update / refresh the display of the game
    pygame.display.flip()

# quit pygame
pygame.quit()