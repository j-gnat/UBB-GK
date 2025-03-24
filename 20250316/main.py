import pygame
import math
from coordinate import Coordinate
from typing import Callable

# Color definition
CZERWONY = (255, 0, 0)
ZIELONY = (0, 255, 0)
ZOLTY = (255, 255, 0)
FIOLETOWY = (128, 0, 128)
JASNY_NIEBIESKI = (0, 255, 255)
POMARANCZOWY = (255, 165, 0)
NIEBIESKI = (0, 0, 255)
SZARY = (128, 128, 128)


class Game:
    __window_width: float = 600.0
    __window_height: float = 600.0
    __polygon_middle: Coordinate = Coordinate(
        __window_width / 2,
        __window_height / 2
    )
    __polygon_radius: float = 150.0
    __polygon_sides: int = 10
    __polygon_width: int = 2
    __polygon_initial_coords: list[tuple[float, float]]
    __win: pygame.Surface = pygame.display.set_mode(
        (__window_width, __window_height)
    )
    __view_surface: pygame.Surface
    __rotate_value: int = 0
    __keydown_functions: dict[pygame.event.Event, Callable]

    def __init__(self):
        global NIEBIESKI
        pygame.init()
        pygame.display.set_caption("First Game")

        self.__keydown_functions = {
            pygame.K_q: self.__rotate_left,
            pygame.K_e: self.__rotate_right
        }
        self.__polygon_initial_coords = self.__get_polygon_coordinates(
            self.__polygon_middle,
            self.__polygon_radius,
            self.__polygon_sides
        )
        self.__view_surface = pygame.Surface(
            (
                self.__window_width,
                self.__window_height
            )
        )

    def __rotate_left(self):
        self.__rotate_value += 5

    def __rotate_right(self):
        self.__rotate_value -= 5

    def __get_polygon_coordinates(self, center: Coordinate,
                                  radius: float,
                                  sides: int) -> list[tuple[float, float]]:
        result = []
        angle_step = 2 * math.pi / sides
        for i in range(sides):
            point = Coordinate(
                center.x + radius * math.cos(i * angle_step),
                center.y + radius * math.sin(i * angle_step)
            )
            # if i % 3 == 0:
            #     point.x += 40
            result.append(point.coordinates)
        return result

    def __process_game_events(self) -> bool:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            elif event.type == pygame.KEYDOWN:
                self.__keydown_functions.get(event.key, lambda: None)()
        return True

    def __update_surface(self):
        self.__view_surface = pygame.transform.rotate(
            self.__view_surface,
            self.__rotate_value
        )
        self.__win.fill(NIEBIESKI)
        surface_rect = self.__view_surface.get_rect(
            center=(self.__window_width/2, self.__window_height/2))
        self.__win.blit(self.__view_surface, surface_rect.topleft)

    def create_surface(self):
        self.__view_surface = pygame.Surface(
            (
                self.__window_width,
                self.__window_height
            )
        )
        pygame.draw.polygon(
            self.__view_surface,
            NIEBIESKI,
            self.__polygon_initial_coords,
            self.__polygon_width
        )

    def run(self):
        run = True
        while run:
            self.create_surface()
            run = self.__process_game_events()
            self.__update_surface()
            pygame.display.update()


if __name__ == "__main__":
    game = Game()
    game.run()
