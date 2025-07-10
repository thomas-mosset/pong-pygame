"""
Centralized modes for the game
"""

import pygame

class GameMode:
    def __init__(self, mode_name):
        self.mode = mode_name # "1v1" ou "1vAI"
    
    def is_ai_enabled(self):
        return self.mode == "1vAI"

    def control_right_paddle(self, paddle, ball, keys):
        if self.is_ai_enabled():
            # Simple AI: Follows the ball vertically
            if ball.rect.centery < paddle.rect.centery:
                paddle.move_up()
            elif ball.rect.centery > paddle.rect.centery:
                paddle.move_down()
        else:
            # top arrow keyboard key
            if keys[pygame.K_UP]:
                paddle.move_up()
            # bottom arrow keyboard key
            if keys[pygame.K_DOWN]:
                paddle.move_down()