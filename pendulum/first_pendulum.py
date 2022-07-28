import pygame
import os
import math


class Points:
    def __int__(self, x, y, surface, colors, coordinates):
        self.x = x
        self.y = y
        self.surface = surface
        self.colors = colors
        self.coordinates = coordinates

    def draw(self):
        if len(self.coordinates) > 2:
            pygame.draw.lines(self.surface, self.colors, False, self.coordinates, 4)


os.environ['SDL_VIDEO_CENTERED'] = '1'

width, height = 640, 480
SIZE = (width, height)
pygame.init()
pygame.display.set_caption("Pendulum")
fps = 60
screen = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()

mass = 1
length = 200

Gravity = 9.18
scatter = []
restart = False
LIST_LIMIT = 100

# colors
BACKGROUND = (20, 20, 20)
SCATTERLINE1 = (255, 255, 255)
SCATTERLINE2 = (255, 255, 0)
MAINPOINT = (0, 255, 0)
SMALLPOINT = (0, 255, 255)
PENDULUMARM = (45, 140, 245)
ARMSTROKE = 10

starting_point = (width // 2, height // 2)
x_offset = starting_point[0]
y_offset = starting_point[1]

run = True
h = 1 / 120
frame_id = 0

while run:
    clock.tick(fps)
    screen.fill(BACKGROUND)

    # TODO calculate the acceleration

    # TODO calculate the pendulum mass position x_i and y_i
    x_1 = 0
    y_1 = 0

    scatter.insert(0, (x_1, y_1))
    pygame.draw.line(screen, PENDULUMARM, starting_point, (x_1, y_1), ARMSTROKE)
    pygame.draw.circle(screen, SMALLPOINT, starting_point, 8)

    if len(scatter) > 1:
        pygame.draw.line(screen, SCATTERLINE2, False, scatter, 1)

    pygame.draw.circle(screen, MAINPOINT, (int(x_1), int(y_1)), 20)

    pygame.display.update()
    frame_id += 1

pygame.quit()
