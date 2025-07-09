"""
This is the main game file. It is responsible for the game loop and
changing states.
"""

import pygame
import time
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
        self.start_x = x
        self.start_y = y
        self.size = 20
        self.color = settings.WHITE
        self.speed_x = 5
        self.speed_y = 5
        self.rect = pygame.Rect(x, y, self.size, self.size)
        self.waiting = False
        self.wait_start_time = 0
    
    def move(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
    
    def draw(self, surface):
        pygame.draw.ellipse(surface, self.color, self.rect)
    
    def bounce_on_walls(self):
        if self.rect.top <= 0 or self.rect.bottom >= pygame.display.get_surface().get_height():
            self.speed_y *= -1
    
    # reverses the horizontal direction (speed_x) if the ball hits the paddle.
    def bounce_on_paddle(self, paddle):
        if self.rect.colliderect(paddle.rect):
            self.speed_x *= -1
            
            ## Realistic bounce
            # Calculate the distance between the center of the paddle and the center of the ball
            offset = (self.rect.centery - paddle.rect.centery) / (paddle.height / 2)

            # Change the vertical speed proportionally to the offset
            self.speed_y = offset * 5
            
            # If the ball gets out of control
            self.speed_y = max(-7, min(self.speed_y, 7))
            
            ## Increase ball's speed progressively
            if self.speed_x > 0:
                self.speed_x += 0.5
            else:
                self.speed_x -= 0.5

            if self.speed_y > 0:
                self.speed_y += 0.5
            else:
                self.speed_y -= 0.5

            # Limit the speed to avoid blowing up the game
            max_speed = 15
            self.speed_x = max(-max_speed, min(self.speed_x, max_speed))
            self.speed_y = max(-max_speed, min(self.speed_y, max_speed))
    
    def reset(self):
        self.rect.x = self.start_x
        self.rect.y = self.start_y
        self.speed_x = 5 * (-1 if self.speed_x > 0 else 1) # change direction
        self.speed_y *= 5
        self.waiting = True
        self.wait_start_time = time.time() # start the timer
    
    def update(self):
        if self.waiting:
            if time.time() - self.wait_start_time >= 2: # 2 seconds
                self.waiting = False
        else:
            self.move()