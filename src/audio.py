"""
Centralized audio loader
"""
import os
import pygame

pygame.mixer.init()

# path toward sounds
base_path = os.path.join(os.path.dirname(__file__), '..', 'assets', 'sounds')

# load sounds
goal_sound = pygame.mixer.Sound(os.path.join(base_path, 'goal_sound.wav'))
ball_bounce = pygame.mixer.Sound(os.path.join(base_path, 'ball_bounce.wav'))

# sounds volume
goal_sound.set_volume(0.5)
ball_bounce.set_volume(0.5)

def play_goal_sound():
    goal_sound.play()
    
def play_ball_bounce():
    ball_bounce.play()