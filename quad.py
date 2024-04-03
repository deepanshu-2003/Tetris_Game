import pygame
import time

class Quad():
    def __init__(self,win,min,max):
        self.window,self.MIN,self.MAX,self.t = win,min,max,time
        
        self.rec1 = pygame.Rect(self.MAX//2,0,30,30)
        self.rec2 = pygame.Rect((self.MAX//2)+30,0,30,30)
        self.rec3 = pygame.Rect(self.MAX//2,30,30,30)
        self.rec4 = pygame.Rect((self.MAX//2)+30,30,30,30)
        self.t = time.time()
        self.speed=0.8
    def draw(self):
        # moving from time
        if(time.time()>=self.t+self.speed):
            self.rec1.y+=30
            self.rec2.y+=30
            self.rec3.y+=30
            self.rec4.y+=30
            self.t=time.time()
        pygame.draw.rect(self.window,(0,0,240),self.rec1) # rect(place,(color),rectangle)
        pygame.draw.rect(self.window,(0,0,240),self.rec2) # rect(place,(color),rectangle)
        pygame.draw.rect(self.window,(0,0,240),self.rec3) # rect(place,(color),rectangle)
        pygame.draw.rect(self.window,(0,0,240),self.rec4) # rect(place,(color),rectangle)
    def draw_demo(self,x,y):
        pygame.draw.rect(self.window,(0,0,240),pygame.Rect(x,y,30,30))
        pygame.draw.rect(self.window,(0,0,240),pygame.Rect(x,y+30,30,30))
        pygame.draw.rect(self.window,(0,0,240),pygame.Rect(x+30,y,30,30))
        pygame.draw.rect(self.window,(0,0,240),pygame.Rect(x+30,y+30,30,30))
    
    def check_collision(self,blocks):
        collision = False
        for rec in [self.rec1,self.rec2,self.rec3,self.rec4]:
            for block in blocks:
                if rec.y+30==block[1] and rec.x==block[0]:
                    collision = True
        return collision        
        
    def move_left(self,blocks):
        if(self.rec1.left-30>self.MIN):
            self.rec1.x-=30
            self.rec2.x-=30
            self.rec3.x-=30
            self.rec4.x-=30
            if self.check_collision(blocks):
                self.rec1.x+=30
                self.rec2.x+=30
                self.rec3.x+=30
                self.rec4.x+=30
    def move_right(self,blocks):
        if(self.rec2.right+30<self.MAX):
            self.rec1.x+=30
            self.rec2.x+=30
            self.rec3.x+=30
            self.rec4.x+=30
            if self.check_collision(blocks):
                self.rec1.x-=30
                self.rec2.x-=30
                self.rec3.x-=30
                self.rec4.x-=30
    def fall(self):
        self.speed=0.07
    def hit(self,blocks):
        height = pygame.display.Info().current_h
        def write_in_blocks():
            if [self.rec1.x,self.rec1.y] not in blocks:
                blocks.append([self.rec1.x,self.rec1.y])
                blocks.append([self.rec2.x,self.rec2.y])
                blocks.append([self.rec3.x,self.rec3.y])
                blocks.append([self.rec4.x,self.rec4.y])
        Hit = False
        for rec in [self.rec1,self.rec2,self.rec3,self.rec4]:
            for block in blocks:
                if rec.x==block[0] and rec.bottom==block[1]:#left , right , 
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
        self.rec1.x,self.rec2.x,self.rec3.x,self.rec4.x = self.MAX//2,(self.MAX//2)+30,self.MAX//2,(self.MAX//2)+30
        self.rec1.y,self.rec2.y,self.rec3.y,self.rec4.y = 0,0,30,30
        self.speed=0.8
