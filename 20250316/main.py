import pygame
import math

pygame.init()
win = pygame.display.set_mode((600, 600))
polygonCoordinates = []
pygame.display.set_caption("First Game")

def GetPolygonCoordinates(center, radius, sides):
    pass

# deklarowanie kolorów
CZERWONY = (255, 0, 0)
ZIELONY = (0, 255, 0)
ZOLTY = (255, 255, 0)
FIOLETOWY = (128, 0, 128)
JASNY_NIEBIESKI = (0, 255, 255)
POMARANCZOWY = (255, 165, 0)
NIEBIESKI = (0, 0, 255)
SZARY = (128, 128, 128)

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    GetPolygonCoordinates(75, 10)

    pygame.display.update()