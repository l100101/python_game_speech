import pygame
import sys

class Menu:
    def __init__(self, screen, options):
        self.screen = screen
        self.options = options
        self.font = pygame.font.Font(None, 36)
        self.selected = 0
        self.rect = 0,0
    def draw(self, surface, x, y):
        for i, option in enumerate(self.options):
            text = self.font.render(option, True, (255, 255, 255))
            text_rect = text.get_rect(center=(x, y + i * 50))
            if i == self.selected:
                pygame.draw.rect(surface, (255, 0, 0), text_rect.inflate(10, 10))
            surface.blit(text, text_rect)
# Usage example
# pygame.init()
# screen = pygame.display.set_mode((800, 600))
# menu = Menu(screen, ["Play", "Level Selection", "Settings", "Exit"])
# selected_option = menu.display_menu()
# print("Selected option:", menu.options[selected_option])