import pygame as pg
import random


class Particle(pg.sprite.Sprite):
    def __init__(self, screen, size, heat,color, border, particle_group, x_pos, y_pos):   #change pressure using box
        super().__init__()
        self.screen = screen
        self.size = size
        self.heat = heat
        self.speed = self.heat/2
        self.speed_x = self.speed * random.choice([-1, 1]) * random.choice([1, 2, 3])
        self.speed_y = self.speed * random.choice([-1, 1]) *random.choice([1, 2, 3])
        self.momentum = self.speed*self.size
        self.color = color
        self.particle_group = particle_group
        path = random.choice(["graphics/r_particle.png", "graphics/b_particle.png"])
        self.image = pg.transform.scale(pg.image.load(path), (self.size, self.size)).convert_alpha()
        self.x = x_pos
        self.y = y_pos
        self.rect = self.image.get_rect(center = (self.x, self.y))
        self.border = border
    def collision(self):
        if pg.sprite.spritecollide(self, self.particle_group, False) and pg.sprite.spritecollide(self, self.particle_group, False)[0] != self: #might always say "it's colliding with itself, bro all I had to tell it was make sure it isn't you"    #trying vector collision
            distance_x = abs(self.rect.center[0] - pg.sprite.spritecollide(self, self.particle_group, False)[0].rect.center[0])
            distance_y = abs(self.rect.center[1] - pg.sprite.spritecollide(self, self.particle_group, False)[0].rect.center[1])
        #prolly just gonna end up looking at all possible cases for collisions

        if pg.Rect.colliderect(self.rect, self.border.rect1) or pg.Rect.colliderect(self.rect, self.border.rect2) or pg.Rect.colliderect(self.rect, self.border.rect3) or pg.Rect.colliderect(self.rect, self.border.rect4):
            if (self.rect.top <= self.border.rect3.bottom) or (self.rect.bottom >= self.border.rect4.top):
                self.speed_y *= -1
                if (self.rect.top <= self.border.rect3.bottom) and self.border.shrink == True:
                    self.speed_y += (self.border.shrink_speed+(self.border.shrink_speed/self.border.shrink_speed)) #change negative or positive if top or bottom
                if (self.rect.bottom >= self.border.rect4.top) and self.border.shrink == True:
                    self.speed_y -= (self.border.shrink_speed+(self.border.shrink_speed/self.border.shrink_speed))
            if (self.rect.left <= self.border.rect1.right) or (self.rect.right >= self.border.rect2.left):  
                self.speed_x *= -1
                if  (self.rect.left <= self.border.rect1.right) and self.border.shrink == True:
                    self.speed_x += (self.border.shrink_speed +(self.border.shrink_speed/self.border.shrink_speed))
                if (self.rect.right >= self.border.rect2.left) and self.border.shrink == True:
                    self.speed_x -= (self.border.shrink_speed + (self.border.shrink_speed/self.border.shrink_speed))





    def update(self):
        self.screen.blit(self.image, self.rect)
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        self.collision()





