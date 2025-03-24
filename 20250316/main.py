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
    __polygon_radius: float = 75.0
    __polygon_sides: int = 10
    __polygon_width: int = 2
    __polygon_initial_coords: list[tuple[float, float]]
    __win: pygame.Surface = pygame.display.set_mode(
        (__window_width, __window_height)
    )
    __view_surface: pygame.Surface
    __rotate_value: int = 0
    __keydown_functions: dict[pygame.event.Event, Callable]
    __transformation_functions: dict[int, Callable]
    __transformation_selected: int = 1
    __surface_content_options: dict[int, Callable]
    __surface_selected_option: int = 0

    def __init__(self):
        global NIEBIESKI
        pygame.init()
        pygame.display.set_caption("First Game")

        self.__keydown_functions = {
            pygame.K_q: self.__rotate_left,
            pygame.K_e: self.__rotate_right,
            pygame.K_1: lambda: self.__set_tranformation(1),
            pygame.K_2: lambda: self.__set_tranformation(2),
            pygame.K_3: lambda: self.__set_tranformation(3),
            pygame.K_4: lambda: self.__set_tranformation(4),
            pygame.K_5: lambda: self.__set_tranformation(5),
            pygame.K_6: lambda: self.__set_tranformation(6),
            pygame.K_7: lambda: self.__set_tranformation(7),
            pygame.K_8: lambda: self.__set_tranformation(8),
            pygame.K_9: lambda: self.__set_tranformation(9),
            pygame.K_0: lambda: self.__reset_rotation(),
        }
        self.__transformation_functions = {
            1: self.__tranform_option1,
            2: self.__tranform_option2,
            3: self.__tranform_option3,
            4: self.__tranform_option4,
            5: self.__tranform_option5,
            6: self.__tranform_option6,
            7: self.__tranform_option7,
            8: self.__tranform_option8,
            9: self.__tranform_option9,
        }
        self.__surface_content_options = {
            0: self.__draw_polygon,
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

    def __tranform_option1(self):
        pass

    def __tranform_option2(self):
        self.__view_surface = pygame.transform.rotozoom(
            self.__view_surface, -45, 2.0)

    def __tranform_option3(self):
        self.__view_surface = pygame.transform.flip(
            self.__view_surface, 0, 1)
        self.__view_surface = pygame.transform.scale(
            self.__view_surface,
            (self.__window_width // 2, self.__window_height * 2))

    def __tranform_option4(self):
        raise NotImplementedError("Function not implemented")

    def __tranform_option5(self):
        raise NotImplementedError("Function not implemented")

    def __tranform_option6(self):
        raise NotImplementedError("Function not implemented")

    def __tranform_option7(self):
        raise NotImplementedError("Function not implemented")

    def __tranform_option8(self):
        raise NotImplementedError("Function not implemented")

    def __tranform_option9(self):
        raise NotImplementedError("Function not implemented")

    def __set_tranformation(self, option: int):
        self.__transformation_selected = option

    def __rotate_left(self):
        self.__rotate_value += 5

    def __rotate_right(self):
        self.__rotate_value -= 5

    def __reset_rotation(self):
        self.__rotate_value = 0

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
            if i % 3 == 0:
                point.x += 40
            result.append(point.coordinates)
        return result

    def __process_game_events(self) -> bool:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            elif event.type == pygame.KEYDOWN:
                self.__keydown_functions.get(
                    event.key, lambda: None
                )()
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

    def __draw_polygon(self):
        pygame.draw.polygon(
            self.__view_surface,
            NIEBIESKI,
            self.__polygon_initial_coords,
            self.__polygon_width
        )

    def create_surface(self):
        self.__view_surface = pygame.Surface(
            (
                self.__window_width,
                self.__window_height
            )
        )
        self.__surface_content_options.get(
            self.__surface_selected_option, self.__draw_polygon)()

    def run(self):
        run = True
        while run:
            self.create_surface()
            run = self.__process_game_events()
            self.__transformation_functions.get(
                self.__transformation_selected, lambda: None)()
            self.__update_surface()
            pygame.display.update()


if __name__ == "__main__":
    game = Game()
    game.run()
