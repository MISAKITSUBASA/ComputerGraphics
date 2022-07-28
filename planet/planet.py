import numpy as np
import pygame
import math
import matplotlib.pyplot as plt

width, height = 800, 800
SIZE = (width, height)
pygame.init()
pygame.display.set_caption("planet")
fps = 60
screen = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()


G = 1*10**-5
x0 = width*2//4
y0 = height*2//4

x1 = x0
y1 = x0 - 200

x1_v = 3000
y1_v = 0
x1_a = 0
y1_a = 0

prev_x1 = 0
prev_y1 = 0
prev_x1_v = 0
prev_y1_v = 0
prev_x1_a = 0
prev_y1_a = 0

m0 = 1
m1 = 1
frame_id = 0

# COLORS
BACKGROUND = (0, 0, 0)
MAINPOINT = (0, 255, 0)
SMALLPOINT = (0, 0, 255)

x_point = []
y_point = []

run = True

h = 0.001

use_prev_force = 1


while run:
    clock.tick(fps)
    screen.fill(BACKGROUND)

    prev_x1_v = x1_v
    prev_y1_v = y1_v
    prev_x1 = x1
    prev_y1 = y1

    # Main part
    # ============================================================
    if use_prev_force == 0:

        distance_x = x1 - x0
        distance_y = y1 - y0
    else:
        distance_x = prev_x1 - x0
        distance_y = prev_y1 - y0

    distance = math.sqrt(distance_x ** 2 + distance_y ** 2)
    force = G * m0 * m1 / distance ** 2
    theta = math.atan2(distance_y, distance_x)
    # force_x = math.cos(theta) * force
    # force_y = math.sin(theta) * force

    force_x = -distance_x * np.sqrt(distance_x**2 + distance_y**2)**3 * G * m0 * m1
    force_y = -distance_y * np.sqrt(distance_x**2 + distance_y**2)**3 * G * m0 * m1

    x1_a = force_x/m1
    y1_a = force_y/m1

    x1 = prev_x1 + prev_x1_v * h
    y1 = prev_y1 + prev_y1_v * h

    x1_v = prev_x1_v + x1_a * h
    y1_v = prev_y1_v + y1_a * h
    # ============================================================

    pygame.draw.circle(screen, SMALLPOINT, (x0, y0), 8)
    pygame.draw.circle(screen, MAINPOINT, (int(x1), int(y1)), 20)
    pygame.display.update()
    frame_id = frame_id+1

    x_point.append(int(x1))
    y_point.append(int(y1))

    if frame_id >= 2000:
        break


fig = plt.figure()
ax1 = fig.add_subplot(111)
ax1.set_title('plot')
plt.xlabel('x')
plt.ylabel('y')
ax1.scatter(np.array(x_point), np.array(y_point), c='r', marker='o')
plt.show()


pygame.quit()
