import os
import pygame
from typing import Tuple


class Grid:
    """
      This class represent a grid where the game
      is going to happen. Grid uses a fixed map image
      and its tile pixel size is 16. It means that every
      tile of map image is 16x16.

      Grid image size is 320x320, so game grid is a 20x20
      2D array.
    """

    def __init__(self, pos_x: float, pos_y: float) -> None:
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.image = pygame.image.load(
            os.path.join('assets', 'map', 'tiled_sea.png'))

        self.tile_size = 16
        self.game_grid_cols = 20
        self.game_grid_rows = 20

        self.game_grid = [
            [0 for i in range(self.game_grid_cols)] for j in range(self.game_grid_rows)]
        self.enemy_game_grid = [
            [0 for i in range(self.game_grid_cols)] for j in range(self.game_grid_rows)]

        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y

        # Inflate rect width to handle 'is_ship_inside' validation at boundaries
        self.rect = self.rect.inflate(12, 10)

    def get_tile_under_mouse(self) -> Tuple[int, int]:
        """
          This method calculates the current selected tile
          of the grid by mouse.
        """

        # Translate mouse position to grid space
        x, y = self.translate_position(pygame.mouse.get_pos())
        if self.__is_valid_position((x, y)):
            return x, y
        else:
            return None, None

    def draw(self, window: pygame.display) -> None:
        """
          This method draws grid on window.
        """
        # Image is drawed using initial position due to self.rect is inflated
        window.blit(self.image, (self.pos_x, self.pos_y))

    def draw_hitbot(self, window: pygame.display) -> None:
        """
          This method draws grid rect on window.
        """
        pygame.draw.rect(window, (255, 0, 0), (self.rect.x, self.rect.y,
                         self.rect.width, self.rect.height), 1, border_radius=1)

    def draw_selected_tile(self, window: pygame.display) -> None:
        """
          This method draws current selected tile
          if mouse is over grid on window.
        """

        square_x, square_y = self.get_tile_under_mouse()
        if square_x is not None:
            square_color = (255, 0, 0)
            square_pos = (self.pos_x + square_x * self.tile_size,
                          self.pos_y + square_y * self.tile_size)
            square_size = (self.tile_size, self.tile_size)
            pygame.draw.rect(window, square_color,
                             (square_pos, square_size), 2)

    def get_rescaled_dimensions(self) -> Tuple[float, float]:
        """
          This method re-scales grid dimension using tile_size in order
          to standardize coordinates.
        """
        return int(self.image.get_width() // self.tile_size), int(self.image.get_height() // self.tile_size)

    def translate_position(self, position: Tuple[int, int]) -> Tuple[float, float]:
        """
          This method translates (x, y) position into re-scaled grid.
        """

        grid_offset = (self.pos_x, self.pos_y)
        position_with_offset = pygame.Vector2(position) - grid_offset
        return int(position_with_offset[0] // self.tile_size), int(position_with_offset[1] // self.tile_size)

    def locate_ships_into_game_grid(self, ships: list) -> None:
        """
          This method locates ships into game grid in order
          to manage game state.

          The main idea is to use ship.rect.center as a pivot in order to
          locate the ship on the game grid around this position. The number
          of tiles used by the ship on the grid is calculated by dividing its
          collision_rect height or width (depeding on orientation) by tile_size.
          This value is used together with translated ship.rec.center position
          to fill the game grid.
        """

        for ship in ships:
            x, y = self.translate_position(ship.rect.center)

            if ship.is_vertical:
                collision_rect_height = ship.collision_rect.height
                number_of_tiles = int(collision_rect_height // self.tile_size)

                # Locate ship vertically by using translated position as a pivot
                for i in range(int(number_of_tiles // 2)):
                    if y - i >= 0:
                        self.game_grid[y - i][x] = ship.name

                    if y + i < self.game_grid_rows:
                        self.game_grid[y + i][x] = ship.name
            else:
                collision_rect_width = ship.collision_rect.width
                number_of_tiles = int(collision_rect_width // self.tile_size)

                # Locate ship horizontally by using translated position as a pivot
                for i in range(int(number_of_tiles // 2)):
                    if x - i >= 0:
                        self.game_grid[y][x - i] = ship.name

                    if x + i < self.game_grid_cols:
                        self.game_grid[y][x + i] = ship.name

    def attack_enemy(self) -> bool:
        # Translate mouse position to grid space
        x, y = self.translate_position(pygame.mouse.get_pos())
        
        if self.__is_valid_position((x, y)):
          pass

    def receive_attack_from_enemy(self, position: Tuple[float, float]) -> None:
        pass

    def __is_valid_position(self, position: Tuple[float, float]) -> bool:
        """
          This private method validates if provided position is
          inside re-scaled grid.
        """
        
        final_x, final_y = self.get_rescaled_dimensions()
        return (position[0] >= 0 and position[1] >= 0 and
                position[0] < final_x and position[1] < final_y)
