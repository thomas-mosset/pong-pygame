"""
This is the main game file. It is responsible for the game loop and
changing states.
"""

import pygame
import settings

class Paddle:
    def __init__(self, x, y):
        self.width = 20
        self.height = 100
        self.color = settings.WHITE
        self.speed = 5
        self.rect = pygame.Rect(x, y, self.width, self.height)
        
    def move_up(self):
        self.rect.y -= self.speed
    
    def move_down(self):
        self.rect.y += self.speed
    
    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)