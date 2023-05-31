import pygame as pg

class Border():
    def __init__(self, x_pos, y_pos, surface, x_size, y_size):
        self.screen = surface
        self.x = x_pos
        self.y = y_pos
        self.x_size = x_size
        self.y_size = y_size
        self.image1 = pg.surface.Surface((10, self.y_size)) 
        self.image2 = pg.surface.Surface((10, self.y_size))
        self.image3 = pg.surface.Surface((self.x_size, 10))
        self.image4 = pg.surface.Surface((self.x_size, 10))
        self.rect1 = self.image1.get_rect(topleft = (self.x, self.y))
        self.rect2 = self.image2.get_rect(topright = (self.x + self.x_size, self.y))
        self.rect3 = self.image3.get_rect(topleft = (self.x, self.y))
        self.rect4 = self.image4.get_rect(bottomleft = (self.x, self.y+self.y_size)) 
        self.shrink_speed = 2
        self.shrink = False


    def update(self):
        self.screen.blit(self.image1, self.rect1)
        self.screen.blit(self.image2, self.rect2)
        self.screen.blit(self.image3, self.rect3)
        self.screen.blit(self.image4, self.rect4)
        self.image1 = pg.surface.Surface((10, self.y_size)) 
        self.image2 = pg.surface.Surface((10, self.y_size))
        self.image3 = pg.surface.Surface((self.x_size, 10))
        self.image4 = pg.surface.Surface((self.x_size, 10))
        self.rect1 = self.image1.get_rect(topleft = (self.x, self.y))
        self.rect2 = self.image2.get_rect(topright = (self.x + self.x_size, self.y))
        self.rect3 = self.image3.get_rect(topleft = (self.x, self.y))
        self.rect4 = self.image4.get_rect(bottomleft = (self.x, self.y+self.y_size)) 

        key = pg.key.get_pressed()
        if key[pg.K_DOWN]:
            self.shrink = True
            self.shrink_speed = 2
        elif key[pg.K_UP]:
            self.shrink = True 
            self.shrink_speed = -2
        else:
            self.shrink = False 
        if self.shrink == True:
            self.x += (self.shrink_speed/2)
            self.y +=(self.shrink_speed/2)
            self.x_size-= self.shrink_speed
            self.y_size -=self.shrink_speed
        
