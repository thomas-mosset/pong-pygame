"""
Centralized menus
"""
import pygame
import settings
from font import load_font

class ModeMenu:
    def __init__(self, screen):
        self.screen = screen
        self.font = load_font(50)
        self.options = ["Joueur vs Joueur", "Joueur vs Ordinateur"]
        self.selected_index = 0
    
    def show_menu(self):
        selecting = True
        
        while selecting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.selected_index = (self.selected_index - 1) % len(self.options)
                    elif event.key == pygame.K_DOWN:
                        self.selected_index = (self.selected_index + 1) % len(self.options)
                    elif event.key == pygame.K_RETURN:
                        # We return "1v1" if the selected index is 0, otherwise "1vAI"
                        return "1v1" if self.selected_index == 0 else "1vAI"
        
            self._render_menu()
    
    # _render_menu() and not render_menu() because it is a private method
    def _render_menu(self):
        title_font = load_font(settings.FONT_SIZE)
        subtitle_font = load_font(35)
    
        self.screen.fill((settings.BROWN))
        
        title = title_font.render("Choisir un mode :", True, (settings.WHITE))
        self.screen.blit(title, title.get_rect(center=(settings.SCREEN_WIDTH // 2, 200)))
        
        subtitle = subtitle_font.render("Appuyer sur la touche entrée pour valider", True, (settings.WHITE))
        self.screen.blit(subtitle, subtitle.get_rect(center=(settings.SCREEN_WIDTH // 2, 600)))

        # Looping on every menu's option with its index
        for i, option in enumerate(self.options):
            
            # If the option is selected, it will be yellow / orange. Otherwise, it will be white.
            color = (settings.YELLOWISH) if i == self.selected_index else (settings.WHITE)
            # We render it on screen
            rendered = self.font.render(option, True, color)
            self.screen.blit(rendered, rendered.get_rect(center=(settings.SCREEN_WIDTH // 2, 300 + i * 60)))

        pygame.display.flip()