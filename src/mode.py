"""
Centralized modes for the game
"""

import pygame

class GameMode:
    def __init__(self, mode_name, AI_difficulty="moyen"):
        self.mode = mode_name # "1v1" ou "1vAI"
        self.AI_difficulty = AI_difficulty
    
    def is_ai_enabled(self):
        return self.mode == "1vAI"

    def control_right_paddle(self, paddle, ball, keys):
        if self.is_ai_enabled():
            # Only reacts if the ball goes to the right player (ball.speed_x)
            if ball.speed_x > 0:
               AI_speed = self.get_AI_speed()
               paddle.move_ai_player(ball.rect.centery, AI_speed)
        else:
            # human player :
            # top arrow keyboard key
            if keys[pygame.K_UP]:
                paddle.move_up()
            # bottom arrow keyboard key
            if keys[pygame.K_DOWN]:
                paddle.move_down()
    
    def get_AI_speed(self):
        if self.AI_difficulty == "facile":
            return 4
        elif self.AI_difficulty == "moyen":
            return 6
        elif self.AI_difficulty == "difficile":
            return 8
        
        return 6 # fallback