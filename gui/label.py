import pygame
from typing import Tuple

pygame.font.init()


class Label:
    """ This class represent a label GUI element. """

    def __init__(
            self,
            pos_x: float,
            pos_y: float,
            text: str,
            font_size: int = 14,
            text_color: str = '#72788D') -> None:
        # Define attributes
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.font_size = font_size
        self.font = pygame.font.Font(
            'assets/fonts/CascadiaCode-SemiBold.ttf', self.font_size)

        # Define colors
        self.text_color = text_color

        # Define text rect
        self.text_surf = self.font.render(text, True, self.text_color)
        self.text_rect = self.text_surf.get_rect(
            topleft=(self.pos_x, self.pos_y))

    def move_label(self, delta: Tuple[float, float]) -> None:
        """ This function movel label.. """
        
        self.text_rect.x += delta[0]
        self.text_rect.y += delta[1]

    def draw(self, window: pygame.display) -> None:
        """ This function draws label on window. """
        window.blit(self.text_surf, self.text_rect)

    def change_text(self, new_text: str) -> None:
        """ This function changes text of label. """
        
        self.text_surf = self.font.render(new_text, True, self.text_color)
        self.text_rect = self.text_surf.get_rect(
            topleft=(self.pos_x, self.pos_y))
