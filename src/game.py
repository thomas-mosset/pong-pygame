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

class Ball:
    def __init__(self, x, y):
        self.size = 20
        self.color = settings.WHITE
        self.speed_x = 5
        self.speed_y = 5
        self.rect = pygame.Rect(x, y, self.size, self.size)
    
    def move(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
    
    def draw(self, surface):
        pygame.draw.ellipse(surface, self.color, self.rect)
    
    def bounce_on_walls(self):
        if self.rect.top <= 0 or self.rect.bottom >= pygame.display.get_surface().get_height():
            self.speed_y *= -1