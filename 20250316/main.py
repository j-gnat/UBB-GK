import pygame
import math
from coordinate import Coordinate


# Global constants
WINDOW_WIDTH: float = 600.0
WINDOW_HEIGHT: float = 600.0

# Color definition
CZERWONY = (255, 0, 0)
ZIELONY = (0, 255, 0)
ZOLTY = (255, 255, 0)
FIOLETOWY = (128, 0, 128)
JASNY_NIEBIESKI = (0, 255, 255)
POMARANCZOWY = (255, 165, 0)
NIEBIESKI = (0, 0, 255)
SZARY = (128, 128, 128)

# Global variables
polygon_middle = Coordinate(WINDOW_WIDTH/2, WINDOW_HEIGHT/2)
polygon_radius: float = 75.0
polygon_sides: int = 10
polygon_coords: list[tuple[float, float]]
win = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))


def get_polygon_coordinates(center: Coordinate,
                            radius: float,
                            sides: int) -> list[tuple[float, float]]:
    result = []
    angle_step = 2 * math.pi / sides
    for i in range(sides):
        x = center.x + radius * math.cos(i * angle_step)
        y = center.y + radius * math.sin(i * angle_step)
        coordinate = (x, y)
        result.append(coordinate)
    return result


def draw_polygon():
    global polygon_middle, polygon_radius, polygon_sides, polygon_coords
    polygon_coords = get_polygon_coordinates(
        polygon_middle,
        polygon_radius,
        polygon_sides
    )
    pygame.draw.polygon(win, NIEBIESKI, polygon_coords)


def main():
    pygame.init()
    pygame.display.set_caption("First Game")
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        pygame.display.update()


if __name__ == "__main__":
    main()
