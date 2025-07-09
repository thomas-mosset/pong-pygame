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
        if self.rect.top > 0:
            self.rect.y -= self.speed
    
    def move_down(self):
        if self.rect.bottom < pygame.display.get_surface().get_height():
            self.rect.y += self.speed
    
    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)