import pygame

pygame.font.init()
GUI_FONT = pygame.font.Font('assets/fonts/CascadiaCode-SemiBold.ttf', 14)


class Input:
    """ This class represents a text input GUI element. """

    def __init__(
            self,
            pos_x: float,
            pos_y: float,
            width: float,
            height: float,
            border_radius: int = 10,
            text_color: str = '#475F77',
            input_color: str = '#CCE6EC',
            selected_color: str = '#FFFFFF',
            shadow_color: str = '#475F77') -> None:
        # Define attributes
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.width = width
        self.height = height
        self.is_active: bool = False

        # Input tracking variable
        self.input_text: str = ''

        # Define gui properties
        self.text_color = text_color
        self.input_color = input_color
        self.shadow_color = shadow_color
        self.border_radius = border_radius
        self.selected_color = selected_color
        self.current_input_color = input_color

        # Define text rect
        self.input_surf = GUI_FONT.render(
            self.input_text, True, self.text_color)
        self.input_rect = self.input_surf.get_rect(
            topleft=(self.pos_x, self.pos_y), width=self.width, height=self.height)

        # Define text rect shadow
        self.input_shadow_rect = self.input_rect.inflate(6, 6)

    def handle_input_events(self, event: pygame.event.Event):
        """
          This function handles text input events, such as
          keyboard typing and selected.
        """
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.input_rect.collidepoint(event.pos):
                self.is_active = True
                self.current_input_color = self.selected_color
            else:
                self.is_active = False
                self.current_input_color = self.input_color

        if self.is_active:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    self.input_text = self.input_text[:-1]
                else:
                    self.input_text += event.unicode

        self.update()

    def update(self) -> None:
        """ This function updates surf and rect with current input text. """

        self.input_surf = GUI_FONT.render(
            self.input_text, True, self.text_color)
        self.input_rect = self.input_surf.get_rect(
            topleft=(self.pos_x, self.pos_y), width=self.width, height=self.height)

    def draw(self, window: pygame.display) -> None:
        """ This function draws input element on window. """

        # Draw shadows
        pygame.draw.rect(window, self.shadow_color,
                         self.input_shadow_rect, border_radius=self.border_radius)

        # Draw input rect
        pygame.draw.rect(window, self.current_input_color,
                         self.input_rect, border_radius=self.border_radius)

        # Draw text
        window.blit(self.input_surf, self.input_rect)
