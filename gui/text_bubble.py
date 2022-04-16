import pygame
from typing import Tuple

pygame.font.init()


class TextBubble:
    """ This class represent a text bubble GUI element for PyGame. """

    def __init__(
            self,
            pos_x: float,
            pos_y: float,
            width: float,
            height: float,
            text: str,
            bubble_color: str = '#AEC301',
            shadow_color: str = '#72788D',
            text_color: str = '#FFFFFF') -> None:
        # Define attributes
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.width = width
        self.height = height
        self.font = pygame.font.Font(
            'assets/fonts/CascadiaCode-SemiBold.ttf', 14)

        # Define colors
        self.bubble_color = bubble_color
        self.shadow_color = shadow_color
        self.text_color = text_color

        # Define bubble rect
        self.bubble_rect = pygame.Rect(
            (self.pos_x, self.pos_y), (self.width, self.height))

        # Define bubble shadow rect
        self.bubble_shadow_rect = self.bubble_rect.inflate(6, 6)

        # Define text rect
        self.text_surf = self.font.render(text, True, self.text_color)
        self.text_rect = self.text_surf.get_rect(
            center=self.bubble_rect.center)

    def center_button_from_position(self, position: Tuple[float, float]) -> None:
        """ This function center text bubble over provider position. """

        self.bubble_rect.center = position
        self.bubble_shadow_rect.center = position
        self.text_rect.center = position

    def draw(self, window: pygame.display) -> None:
        """ This function draws text bubble on window. """

        # Draw shadows
        pygame.draw.rect(window, self.shadow_color,
                         self.bubble_shadow_rect, border_radius=12)

        # Draw bubble and triangle
        pygame.draw.rect(window, self.bubble_color,
                         self.bubble_rect, border_radius=12)

        # Draw text
        window.blit(self.text_surf, self.text_rect)

    def change_text(self, new_text: str) -> None:
        """ This function changes text of text bubble. """

        self.text_surf = self.font.render(new_text, True, self.text_color)
        self.text_rect = self.text_surf.get_rect(
            center=self.bubble_rect.center)
