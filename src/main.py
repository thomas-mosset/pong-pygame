"""
Main file for the game.
"""
import os
import pygame
import settings # import all settings from the settings.py file

from game import Paddle, Ball
from score import Score

from audio import play_goal_sound

# 44100 => most common frequency for audio files
# -16 => 16-bit signed sound
# 2 => stereo sound (left/right)
# 512 => buffer size
pygame.mixer.pre_init(44100, -16, 2, 512) 

# game init
pygame.init()

left_player = Paddle(50, settings.SCREEN_HEIGHT // 2 - 50)
right_player = Paddle(1210, settings.SCREEN_HEIGHT // 2 - 50)
ball = Ball(settings.SCREEN_WIDTH // 2 - 10, settings.SCREEN_HEIGHT // 2 - 10)
score = Score()

# game's screen
screen = pygame.display.set_mode((settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT))
pygame.display.set_caption(settings.GAME_TITLE)

image_path = os.path.join(os.path.dirname(__file__), '..', 'assets', 'images', 'freepik__bg.jpg')
background = pygame.image.load(image_path).convert() # .convert() -> optimization for bg image

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
    ball.bounce_on_paddle(left_player)
    ball.bounce_on_paddle(right_player)
    
    if ball.rect.left <= 0:
        score.point_right()
        play_goal_sound() # sound triggered when a point is added
        ball.reset()
    elif ball.rect.right >= settings.SCREEN_WIDTH:
        score.point_left()
        play_goal_sound() # sound triggered when a point is added
        ball.reset()
    
    # display player
    left_player.draw(screen)
    right_player.draw(screen)
    
    # display ball
    ball.draw(screen)
    
    # displai score
    score.draw(screen, settings.SCREEN_WIDTH)
    
    # update / refresh the display of the game
    pygame.display.flip()

# quit pygame
pygame.quit()