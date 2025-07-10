"""
Fonts module
"""
import os
import pygame

def load_font(size):
    font_path = os.path.join(os.path.dirname(__file__), '..', 'assets', 'fonts', 'RocketCommand-OG5D8.otf')
    return pygame.font.Font(font_path, size)