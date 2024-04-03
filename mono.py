import pygame
import time
class Mono:
    def __init__(self,win,min,max):
        self.MAX = max
        self.MIN = min
        self.window = win
        self.rec = pygame.Rect(self.MAX//2,0,30,30)
        self.t = time.time()
        self.speed=0.8
    def draw(self):
        # moving from time
        if(time.time()>self.t+self.speed):
            self.rec.y+=30
            self.t=time.time()
        pygame.draw.rect(self.window,(0,255,0),self.rec) # rect(place,(color),rectangle)
    def draw_demo(self,x,y):
        pygame.draw.rect(self.window,(0,255,0),pygame.Rect(x,y,30,30))
    def check_collision(self,blocks):
        collision = False
        for block in blocks:
            if self.rec.y+30==block[1] and self.rec.x==block[0]:
                collision = True
        return collision
    def move_left(self,blocks):
        if(self.rec.left-30>self.MIN):
            self.rec.x-=30
            if  self.check_collision(blocks):
                self.rec.x+=30
    def move_right(self,blocks):
        if(self.rec.right+30<self.MAX):
            self.rec.x+=30
            if self.check_collision(blocks):
                self.rec.x-=30
    def fall(self):
        self.speed=0.07
    def hit(self,blocks):
        height = pygame.display.Info().current_h
        def write_in_blocks():
            if [self.rec.x,self.rec.y] not in blocks:
                blocks.append([self.rec.x,self.rec.y])
        Hit = False
        for rec in [self.rec]:
            for block in blocks:
                if rec.x==block[0] and rec.bottom==block[1]:
                    Hit=True
                    write_in_blocks()
            if rec.y==height:
                Hit = True
                write_in_blocks()
        return Hit
    def change(self,blocks):
        pass
    def set_form(self):
        pass
    def reset(self):
        self.rec.x = self.MAX//2
        self.rec.y = 0
        self.speed=0.8

