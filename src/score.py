"""
Score class for scoring
"""

import os
import pygame
import settings

from font import load_font

class Score:
    def __init__(self):
        self.left = 0
        self.right = 0
        self.font = load_font(settings.FONT_SIZE)
        self.color = settings.WHITE
    
    def draw(self, surface, screen_width):
        text = self.font.render(f"{self.left} | {self.right}", True, self.color)
        text_rect = text.get_rect(center=(screen_width // 2, 50))
        surface.blit(text, text_rect)
    
    def point_left(self):
        self.left += 1
    
    def point_right(self):
        self.right += 1
    
    def is_game_over(self):
        return self.left >= settings.MAX_SCORE or self.right >= settings.MAX_SCORE

    def get_winner(self):
        if self.left >= settings.MAX_SCORE:
            return "Joueur 1"
        elif self.right >= settings.MAX_SCORE:
            return 'Joueur 2'
        
        return None