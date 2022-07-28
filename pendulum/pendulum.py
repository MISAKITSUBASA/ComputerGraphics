import pygame
import math
import matplotlib.pyplot as plt

width, height = 640, 480
SIZE = (width, height)
pygame.init()
pygame.display.set_caption("Pendulum")
fps = 60
screen = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()


mass = 1
length = 200
frame_id = 0
theta = 3*math.pi/2+0.2
angle_velocity = 0
angle_acceleration = 0

prev_theta = 0
prev_angle_velocity = 0
prev_angle_acceleration = 0

Gravity = -1


# COLORS
BACKGROUND = (0, 0, 0)
MAINPOINT = (0, 255, 0)
SMALLPOINT = (0, 0, 255)
PENDULUMARM = (45, 140, 245)
ARMSTROKE = 10

starting_point = (width//2, height//3)

x_offset = starting_point[0]
y_offset = starting_point[1]

run = True
h = 1/20
use_prev_force = 0

theta_list = []
velocity_list = []

while run:
    clock.tick(fps)
    screen.fill(BACKGROUND)
    prev_angle_velocity = angle_velocity
    prev_theta = theta


   # main part
   # -------------------------------------------------------------------------------------------
    x1 = float(length * math.sin(theta)+x_offset)
    y1 = float(length * math.cos(theta)+y_offset)
    # =========================================================================================
    if use_prev_force == 0:
        theta = prev_theta + prev_angle_velocity * h
        angle_acceleration = Gravity * math.sin(theta)
        angle_velocity = prev_angle_velocity + angle_acceleration * h
    # ========================================================================================
    if use_prev_force == 1:
        theta = prev_theta + prev_angle_velocity * h
        angle_acceleration = Gravity * math.sin(prev_theta)
        angle_velocity = prev_angle_velocity + angle_acceleration * h
    # ----------------------------------------------------------------------------------------

    pygame.draw.line(screen, PENDULUMARM, starting_point, (x1, y1), ARMSTROKE)
    pygame.draw.circle(screen, SMALLPOINT, starting_point, 8)
    pygame.draw.circle(screen, MAINPOINT, (int(x1), int(y1)), 20)
    pygame.display.update()
    frame_id = frame_id+1

    theta_list.append(theta)
    velocity_list.append(angle_velocity)

    if frame_id >= 500:
        break


fig = plt.figure()
ax1 = fig.add_subplot(111)
ax1.set_title('plot')
plt.xlabel('theta')
plt.ylabel('velocity')
ax1.scatter(theta_list, velocity_list, c='r', marker='o')
plt.show()


pygame.quit()
