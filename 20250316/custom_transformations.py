import pygame
import math


class CustomTransformations:
    @staticmethod
    def shear_point_x(x: float,
                      y: float,
                      H_x: float) -> tuple[float, float]:
        x_new = H_x * y + x
        y_new = y
        return (x_new, y_new)

    @staticmethod
    def shear_point_y(x: float,
                      y: float,
                      H_y: float) -> tuple[float, float]:
        x_new = x
        y_new = H_y * x + y
        return (x_new, y_new)

    @staticmethod
    def shear_points_map_x(points_map: list[tuple[float, float]],
                           shear_factor: float) -> list[tuple[float, float]]:
        result = []
        for x, y in points_map:
            x_new, y_new = CustomTransformations.shear_point_x(
                x, y, shear_factor
            )
            result.append((x_new, y_new))
        return result

    @staticmethod
    def shear_points_map_y(points_map: list[tuple[float, float]],
                           shear_factor: float) -> list[tuple[float, float]]:
        result = []
        for x, y in points_map:
            x_new, y_new = CustomTransformations.shear_point_x(
                x, y, shear_factor
            )
            result.append((x_new, y_new))
        return result

    @staticmethod
    def shear_surface_x(shear_factor: float,
                        view_surface: pygame.Surface) -> pygame.Surface:
        width, height = view_surface.get_size()
        additional_width = int(width * abs(shear_factor))
        new_width = width + additional_width
        sheared_surface = pygame.Surface((new_width, height), pygame.SRCALPHA)
        sheared_surface.fill((0, 0, 0, 0))

        for y in range(height):
            for x in range(width):
                new_x, new_y = CustomTransformations.shear_point_x(
                    x, y, shear_factor
                )
                color = view_surface.get_at((x, y))
                direction = 1 if shear_factor <= 0 else 0
                sheared_surface.set_at(
                    ((direction * additional_width) + int(new_x), int(new_y)),
                    color
                )
        return sheared_surface

    @staticmethod
    def shear_surface_y(shear_factor: float,
                        view_surface: pygame.Surface) -> pygame.Surface:
        width, height = view_surface.get_size()
        additional_height = int(height * abs(shear_factor))
        new_height = height + additional_height
        sheared_surface = pygame.Surface((width, new_height), pygame.SRCALPHA)
        sheared_surface.fill((0, 0, 0, 0))

        for y in range(height):
            for x in range(width):
                new_x, new_y = CustomTransformations.shear_point_y(
                    x, y, shear_factor
                )
                color = view_surface.get_at((x, y))
                direction = 1 if shear_factor <= 0 else 0
                sheared_surface.set_at(
                    (int(new_x), (direction * additional_height) + int(new_y)),
                    color
                )
        return sheared_surface

    @staticmethod
    def move_point(point: tuple[int, int],
                   vector: tuple[int, int]) -> tuple[int, int]:
        return (point[0] + vector[0], point[1] + vector[1])

    @staticmethod
    def rotate_point(point: tuple[int, int],
                     angle: float) -> tuple[int, int]:
        cos = math.cos(angle)
        sin = math.sin(angle)
        x, y = point
        return (int(x * cos - y * sin), int(x * sin + y * cos))

    @staticmethod
    def rotate_surface(surface: pygame.Surface,
                       angle: float,
                       background_color: tuple[int, int, int] = (0, 0, 0)
                       ) -> pygame.Surface:
        width, height = surface.get_size()
        rect = surface.get_rect()

        new_topleft = CustomTransformations.rotate_point(
            rect.topleft, angle)
        new_topright = CustomTransformations.rotate_point(
            rect.topright, angle)
        new_botleft = CustomTransformations.rotate_point(
            rect.bottomleft, angle)
        new_botright = CustomTransformations.rotate_point(
            rect.bottomright, angle)

        new_width = max(
            abs(new_topleft[0] - new_botright[0]),
            abs(new_botleft[0] - new_topright[0])
        )
        new_height = max(
            abs(new_topleft[1] - new_botright[1]),
            abs(new_botleft[1] - new_topright[1])
        )

        min_x = min(
            new_topleft[0],
            new_botright[0],
            new_botleft[0],
            new_topright[0]
        )

        min_y = min(
            new_topleft[1],
            new_botright[1],
            new_botleft[1],
            new_topright[1]
        )

        min_x = abs(min_x) if min_x <= 0 else 0
        min_y = abs(min_y) if min_y <= 0 else 0
        new_surface = pygame.Surface((new_width, new_height))
        new_surface.fill(background_color)
        for x in range(width):
            for y in range(height):
                new_x, new_y = CustomTransformations.rotate_point(
                    (x, y), angle
                )
                new_x -= rect.topleft[0]
                new_y -= rect.topleft[1]
                color = surface.get_at((x, y))
                new_surface.set_at(
                    (new_x + min_x, new_y + min_y),
                    color
                )
        return new_surface
