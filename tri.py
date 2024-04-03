import pygame
import time
import random

class Tri():
    def __init__(self,win,min,max):
        self.window,self.MIN,self.MAX,self.t,self.color = win,min,max,time,'#BE7F09'
        # -----------forms-------------------------
        self.forms = {
                'horizontal': [(self.MAX//2,0),((self.MAX//2)-30,0),((self.MAX//2)+30,0)],
                'vertical' :[(self.MAX//2,0),(self.MAX//2,-30),(self.MAX//2,30)]
        }
        self.form=random.choice(list(self.forms.keys()))
        self.rec1_x,self.rec2_x,self.rec3_x = self.forms[self.form][0][0],self.forms[self.form][1][0],self.forms[self.form][2][0]
        self.rec1_y,self.rec2_y,self.rec3_y = self.forms[self.form][0][1],self.forms[self.form][1][1],self.forms[self.form][2][1]
        
        self.rec1 = pygame.Rect(self.rec1_x,self.rec1_y,30,30)
        self.rec2 = pygame.Rect(self.rec2_x,self.rec2_y,30,30)
        self.rec3 = pygame.Rect(self.rec3_x,self.rec3_y,30,30)
        self.t = time.time()
        self.speed=0.8
        self.next_form = random.choice(list(self.forms.keys()))
    def draw(self):
        # moving from time
        if(time.time()>=self.t+self.speed):
            self.rec1.y+=30
            self.rec2.y+=30
            self.rec3.y+=30
            self.t=time.time()
        pygame.draw.rect(self.window,self.color,self.rec1) # rect(place,(color),rectangle)
        pygame.draw.rect(self.window,self.color,self.rec2) # rect(place,(color),rectangle)
        pygame.draw.rect(self.window,self.color,self.rec3) # rect(place,(color),rectangle)
    def draw_demo(self,x,y):
        if self.next_form == "horizontal":
            pygame.draw.rect(self.window,self.color,pygame.Rect(x,y,30,30))
            pygame.draw.rect(self.window,self.color,pygame.Rect(x-30,y,30,30))
            pygame.draw.rect(self.window,self.color,pygame.Rect(x+30,y,30,30))
        else:
            pygame.draw.rect(self.window,self.color,pygame.Rect(x,y,30,30))
            pygame.draw.rect(self.window,self.color,pygame.Rect(x,y-30,30,30))
            pygame.draw.rect(self.window,self.color,pygame.Rect(x,y+30,30,30))
            
    def check_collision(self,blocks):
        collision = False
        for rec in [self.rec1,self.rec2,self.rec3]:
            for block in blocks:
                if rec.y+30==block[1] and rec.x==block[0]:
                    collision = True
        return collision
    def move_left(self,blocks):
        if(self.rec2.left-30>self.MIN):
            self.rec1.x-=30
            self.rec2.x-=30
            self.rec3.x-=30
            if self.check_collision(blocks):
                self.rec1.x+=30
                self.rec2.x+=30
                self.rec3.x+=30
    def move_right(self,blocks):
        if(self.rec3.right+30<self.MAX):
            self.rec1.x+=30
            self.rec2.x+=30
            self.rec3.x+=30
            if self.check_collision(blocks):
                self.rec1.x-=30
                self.rec2.x-=30
                self.rec3.x-=30
    def fall(self):
        self.speed=0.07
    def hit(self,blocks):
        height = pygame.display.Info().current_h
        def write_in_blocks():
            if [self.rec1.x,self.rec1.y] not in blocks:
                blocks.append([self.rec1.x,self.rec1.y])
                blocks.append([self.rec2.x,self.rec2.y])
                blocks.append([self.rec3.x,self.rec3.y])
        Hit = False
        for rec in [self.rec1,self.rec2,self.rec3]:
            for block in blocks:
                if rec.x==block[0] and rec.bottom==block[1]:#left , right , 
                    Hit=True
                    write_in_blocks()
            if rec.y==height:
                Hit = True
                write_in_blocks()
        return Hit
    def change(self,blocks):
        def collide_walls():
            collide = False
            for rec in [self.rec1,self.rec2,self.rec3]:
                if rec.left<self.MIN or rec.right>self.MAX:
                    collide = True
                for block in blocks:
                    if rec.x==block[0] and rec.bottom==block[1]:
                        collide=True
            return collide
        def switch_it(f):
            if f == "horizontal":
                self.rec2.x-=30
                self.rec2.y+=30
                self.rec3.x+=30
                self.rec3.y-=30
                self.form = "horizontal"
            if f == "vertical":
                self.rec2.x+=30
                self.rec2.y-=30
                self.rec3.x-=30
                self.rec3.y+=30
                self.form="vertical"
        if(self.form=="horizontal"):
            previous = self.form
            switch_it("vertical")
            if collide_walls():
                switch_it(previous)
        else:
            previous = self.form
            switch_it("horizontal")
            if collide_walls():
                switch_it(previous)
    def set_form(self):
        pass
    def reset(self):
        self.form=self.next_form
        self.rec1.x,self.rec2.x,self.rec3.x = self.forms[self.form][0][0],self.forms[self.form][1][0],self.forms[self.form][2][0]
        self.rec1.y,self.rec2.y,self.rec3.y = self.forms[self.form][0][1],self.forms[self.form][1][1],self.forms[self.form][2][1]
        self.speed=0.8
        self.next_form = random.choice(list(self.forms.keys()))
