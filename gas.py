from random import random
import pygame as pg
import sys
from border import Border
from particles import Particle
import random

pg.init()
clock = pg.time.Clock()

screen_width = 500
screen_height = 500
color = (255, 255, 255)
screen = pg.display.set_mode((screen_width, screen_height))
pg.display.set_caption("Particle Physics")

#objects:
border = Border(50, 50, screen, 400, 400) #when decreasing the border, look at clear code's tutorial for that., nvm I found out how to do it anyway lol
particle_group = pg.sprite.Group()
number_of_particles = 100
for i in range(number_of_particles):
    particle_group.add(Particle(screen, 15, 2, 'blue', border, particle_group, random.randint(border.x + 20, border.x +border.x_size-20), random.randint(border.y+20, border.y + border.y_size-20)))
#can add dynamically
while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
    screen.fill(color)
    border.update()
    particle_group.update()


    pg.display.update()
    clock.tick(60)
