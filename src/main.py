"""
Main file for the game.
"""
import os
import pygame
import settings # import all settings from the settings.py file

from game import Paddle, Ball
from score import Score

from font import load_font

from menu import ModeMenu
from mode import GameMode

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


# game's beginning menu
menu = ModeMenu(screen)
selected_mode = menu.show_menu()

AI_difficulty = None
if selected_mode == "1vAI":
    AI_difficulty = menu.choose_difficulty()

# game's mode (1v1 or 1vAI)
game_mode = GameMode(selected_mode, AI_difficulty)

def show_end_screen(winner):
    winner_font = load_font(60)
    replay_font = load_font(40)
    
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_r: # "r" key from the keyboard to replay
                waiting = False
        
        screen.fill(settings.BROWN)
        winner_text = winner_font.render(f"{winner} a gagné !", True, (settings.WHITE))
        replay_text = replay_font.render("Appuie sur la touche 'R' pour rejouer", True, (settings.WHITE))
        
        screen.blit(winner_text, winner_text.get_rect(center=(settings.SCREEN_WIDTH // 2, settings.SCREEN_HEIGHT // 2 - 40)))
        screen.blit(replay_text, replay_text.get_rect(center=(settings.SCREEN_WIDTH // 2, settings.SCREEN_HEIGHT // 2 + 30)))
        
        pygame.display.flip()

# main game's loop
running = True
while running:
    clock.tick(settings.FPS) # limit the game to 60 FPS
    
    # keys management
    keys = pygame.key.get_pressed()
    
    # Player 1
    if keys[pygame.K_z]: # Z keyboard key
        left_player.move_up()
    
    if keys[pygame.K_s]: # S keyboard key
        left_player.move_down()
    
    # Player 2 (actual player or AI), dealt in the mode.py file
    game_mode.control_right_paddle(right_player, ball, keys)
        
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False # quit the game, if player closes the game screen
    
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
    
    # if a player has 5 points : game is over
    if score.left >= 5 or score.right >= 5:
        winner = "Joueur 1" if score.left >= 5 else "Joueur 2"
        show_end_screen(winner)
        
        # Reset score et positions
        score = Score()
        ball.reset()
        left_player = Paddle(50, settings.SCREEN_HEIGHT // 2 - 50)
        right_player = Paddle(1210, settings.SCREEN_HEIGHT // 2 - 50)
    
    # display player
    left_player.draw(screen)
    right_player.draw(screen)
    
    # display ball
    ball.draw(screen)
    
    # display score
    score.draw(screen, settings.SCREEN_WIDTH)
    
    # update / refresh the display of the game
    pygame.display.flip()

# quit pygame
pygame.quit()