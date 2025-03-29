import pygame
import math
import os
from coordinate import Coordinate
from typing import Callable
from custom_transformations import CustomTransformations

# Color definition
CZERWONY = (255, 0, 0)
ZIELONY = (0, 255, 0)
ZOLTY = (255, 255, 0)
FIOLETOWY = (128, 0, 128)
JASNY_NIEBIESKI = (0, 255, 255)
POMARANCZOWY = (255, 165, 0)
NIEBIESKI = (0, 0, 255)
SZARY = (128, 128, 128)
CZARNY = (0, 0, 0)
BIALY = (255, 255, 255)


class Game:
    __window_width: int = 600
    __window_height: int = 600
    __polygon_radius: float = 75.0
    __polygon_sides: int = 10
    __polygon_width: int = 2
    __win: pygame.Surface = pygame.display.set_mode(
        (__window_width, __window_height)
    )
    __object_surface: pygame.Surface
    __rotate_value: int = 0
    __keydown_functions: dict[pygame.event.Event, Callable]
    __transformation_functions: dict[int, Callable]
    __transformation_selected: int = 1
    __surface_content_options: dict[int, Callable]
    __surface_selected_option: int = 0

    def __init__(self):
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
            pygame.K_TAB: lambda: self.__select_next_surface_content(),
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
            1: self.__get_test_picture,
            2: self.__draw_figure_1,
            3: self.__draw_figure_2,
            4: self.__draw_figure_3,
            5: self.__draw_figure_4,
        }

    def __select_next_surface_content(self):
        self.__surface_selected_option = (
            self.__surface_selected_option + 1
        ) % len(self.__surface_content_options)

    def __center_object_surface_on_window(self) -> pygame.Rect:
        rect = self.__object_surface.get_rect(
            center=(int(self.__window_width / 2),
                    int(self.__window_height / 2)))
        return rect

    def __tranform_option1(self) -> None:
        rect = self.__center_object_surface_on_window()
        self.__object_surface = self.__get_full_window_transformed_surface(
            self.__object_surface,
            rect.topleft
        )

    def __tranform_option2(self,
                           angle: float = 45) -> None:
        self.__object_surface = CustomTransformations.rotate_surface(
            self.__object_surface, angle)
        self.__object_surface = pygame.transform.scale(
            self.__object_surface,
            (self.__object_surface.get_width(), self.__window_height * 0.9)
        )
        rect = self.__center_object_surface_on_window()
        self.__object_surface = self.__get_full_window_transformed_surface(
            self.__object_surface,
            rect.topleft
        )

    def __tranform_option3(self) -> None:
        self.__object_surface = pygame.transform.flip(
            self.__object_surface, 0, 1)
        self.__object_surface = pygame.transform.scale(
            self.__object_surface,
            (self.__window_width / 2, self.__window_height * 2))
        rect = self.__center_object_surface_on_window()
        self.__object_surface = self.__get_full_window_transformed_surface(
            self.__object_surface,
            rect.topleft
        )

    def __tranform_option4(self,
                           shear_factor: float = 0.5) -> None:
        sheared_surface = CustomTransformations.shear_surface_x(
            shear_factor, self.__object_surface)
        self.__object_surface = sheared_surface
        rect = self.__center_object_surface_on_window()
        self.__object_surface = self.__get_full_window_transformed_surface(
            self.__object_surface,
            rect.topleft
        )

    def __tranform_option5(self) -> None:
        self.__object_surface = pygame.transform.scale(
            self.__object_surface,
            (self.__window_width / 2, self.__window_height / 4)
        )
        rect = self.__center_object_surface_on_window()
        rect.topleft = CustomTransformations.move_point(
            rect.topleft, (0, -rect.topleft[1])
        )
        self.__object_surface = self.__get_full_window_transformed_surface(
            self.__object_surface,
            rect.topleft
        )

    def __tranform_option6(self) -> None:
        self.__tranform_option4()
        self.__object_surface = pygame.transform.rotate(
            self.__object_surface, 270)
        rect = self.__center_object_surface_on_window()
        self.__object_surface = self.__get_full_window_transformed_surface(
            self.__object_surface,
            rect.topleft
        )

    def __tranform_option7(self) -> None:
        self.__object_surface = pygame.transform.flip(
            self.__object_surface, 1, 1)
        self.__object_surface = pygame.transform.scale(
            self.__object_surface,
            (self.__window_width / 2, self.__window_height))
        rect = self.__center_object_surface_on_window()
        self.__object_surface = self.__get_full_window_transformed_surface(
            self.__object_surface,
            rect.topleft
        )

    def __tranform_option8(self,
                           agnle: float = 60 * math.pi / 360) -> None:
        self.__object_surface = pygame.transform.scale(
            self.__object_surface,
            (self.__window_width / 2, self.__window_height / 6)
        )
        self.__object_surface = CustomTransformations.rotate_surface(
            self.__object_surface,
            agnle)
        rect = self.__center_object_surface_on_window()
        rect.topright = CustomTransformations.move_point(
            rect.topright, (0, rect.topright[1])
        )
        self.__object_surface = self.__get_full_window_transformed_surface(
            self.__object_surface,
            rect.topleft
        )

    def __tranform_option9(self,
                           shear_factor: float = 0.5) -> None:
        self.__object_surface = CustomTransformations.shear_surface_y(
            shear_factor, self.__object_surface)
        rect = self.__center_object_surface_on_window()
        rect2 = self.__win.get_rect()
        rect.topright = CustomTransformations.move_point(
            rect.topright, (rect2.topright[0] - rect.topright[0], 0)
        )
        self.__object_surface = self.__get_full_window_transformed_surface(
            self.__object_surface,
            rect.topleft
        )

    def __get_full_window_transformed_surface(self,
                                              surface: pygame.Surface,
                                              lefttop: tuple[int, int]
                                              ) -> pygame.Surface:
        temp_surf = pygame.Surface(
            (
                int(self.__window_width),
                int(self.__window_height)
            )
        )
        temp_surf.blit(self.__object_surface, lefttop)
        return temp_surf

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

# INITIAL SURFACES

    def __draw_polygon(self) -> pygame.Surface:
        rectangle_size = self.__polygon_radius * 2 + self.__polygon_width * 2
        surface = self.__get_empty_surface(
            round(rectangle_size + .5), round(rectangle_size + .5))
        polygon_coords = self.__get_polygon_coordinates(
            Coordinate(rectangle_size/2, rectangle_size/2),
            self.__polygon_radius,
            self.__polygon_sides
        )
        pygame.draw.polygon(
            surface,
            NIEBIESKI,
            polygon_coords,
            self.__polygon_width
        )
        return surface

    def __draw_figure_1(
            self,
            width: int = int(__window_width * 0.5),
            height: int = int(__window_height * 0.5)) -> pygame.Surface:
        global CZARNY
        surface = self.__get_empty_surface(width, height)
        rect_center = (width / 2, height / 2)
        rect = surface.get_rect(center=rect_center)
        pygame.draw.rect(surface,
                         ZOLTY,
                         rect)
        pygame.draw.circle(surface,
                           BIALY,
                           rect_center,
                           min(width, height) / 2 * 0.9)
        return surface

    def __draw_figure_2(self,
                        width: int = int(__window_width * 0.5),
                        height: int = int(__window_height * 0.5)
                        ) -> pygame.Surface:
        surface = self.__get_empty_surface(width, height)
        points = [(width / 2, height / 2),
                  (width, height),
                  (width, 0),
                  (0, 0),
                  (0, height)
                  ]
        pygame.draw.polygon(surface,
                            ZIELONY,
                            points)
        return surface

    def __draw_figure_3(self,
                        width: int = int(__window_width * 0.5),
                        height: int = int(__window_height * 0.75)
                        ) -> pygame.Surface:
        surface = self.__get_empty_surface(width, height)
        rect = surface.get_rect()
        rect_height = int(height / 5)
        rect.height = rect_height
        rect.center = (int(surface.get_width() / 2),
                       int(surface.get_height() / 2))
        pygame.draw.rect(surface,
                         NIEBIESKI,
                         rect)
        triangle_bottom_size = rect_height
        points = [(rect.centerx, rect.centery - rect_height / 2),
                  (rect.centerx - int(triangle_bottom_size * 0.5),
                   rect.centery - rect_height / 2 -
                   triangle_bottom_size),
                  (rect.centerx + int(triangle_bottom_size * 0.5),
                   rect.centery - rect_height / 2 -
                   triangle_bottom_size)
                  ]
        pygame.draw.polygon(surface,
                            NIEBIESKI,
                            points)
        points = [(rect.centerx, rect.centery + rect_height / 2),
                  (rect.centerx - int(triangle_bottom_size * 0.5),
                   rect.centery + rect_height / 2 +
                   triangle_bottom_size),
                  (rect.centerx + int(triangle_bottom_size * 0.5),
                   rect.centery + rect_height / 2 +
                   triangle_bottom_size)
                  ]
        pygame.draw.polygon(surface,
                            NIEBIESKI,
                            points)
        return surface

    def __draw_figure_4(self,
                        width: int = int(__window_width * 0.5),
                        height: int = int(__window_height * 0.5),
                        line_width: int = 10) -> pygame.Surface:
        surface = self.__get_empty_surface(width, height)
        point1 = (0 + line_width / 2, 0 + line_width / 2)
        point2 = (width - line_width / 2, 0 + line_width / 2)
        point3 = (0 + line_width / 2, height - line_width / 2)
        point4 = (width - line_width / 2, height - line_width / 2)
        pygame.draw.line(surface,
                         CZERWONY,
                         point1,
                         point2,
                         line_width)
        pygame.draw.line(surface,
                         CZERWONY,
                         point2,
                         point3,
                         line_width)
        pygame.draw.line(surface,
                         CZERWONY,
                         point3,
                         point4,
                         line_width)
        return surface

    def __get_test_picture(self) -> pygame.Surface:
        try:
            base_path = os.path.dirname(__file__)
            image_path = os.path.join(base_path, "TestPicture.png")
            if not os.path.exists(image_path):
                raise FileNotFoundError("Picture not found")

            surface = pygame.image.load(image_path)
            surface = pygame.transform.scale(
                surface,
                (int(self.__window_width / 2), int(self.__window_height / 2))
            )
        except FileNotFoundError as e:
            font = pygame.font.Font(None, 36)
            text_surface = font.render(str(e), True, CZERWONY, CZARNY)
            text_rect = text_surface.get_rect(
                center=(int(self.__window_width / 2),
                        int(self.__window_height / 2)))
            surface = self.__get_empty_surface(
                text_surface.get_width(), text_surface.get_height())
            surface.blit(text_surface, text_rect.topleft)
        finally:
            return surface

# UTILITY

    def create_surface(self):
        self.__object_surface = self.__surface_content_options.get(
            self.__surface_selected_option, self.__draw_polygon)()

    def __update_surface(self):
        temp = pygame.transform.rotate(
            self.__object_surface,
            self.__rotate_value,
        )
        rect = temp.get_rect(
            center=(self.__object_surface.get_width() / 2,
                    self.__object_surface.get_height() / 2)
        )
        self.__win.fill(CZARNY)
        self.__win.blit(temp, rect)

    def __get_empty_surface(self,
                            width: int,
                            height: int) -> pygame.Surface:
        result = pygame.Surface((abs(width), abs(height)))
        result.fill(CZARNY)
        return result

    def run(self):
        run = True
        while run:
            self.create_surface()
            run = self.__process_game_events()
            self.__transformation_functions.get(
                self.__transformation_selected, 1)()
            self.__update_surface()
            pygame.display.update()


if __name__ == "__main__":
    game = Game()
    game.run()
