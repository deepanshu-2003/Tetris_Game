import pygame
import sys
import random
from mono import Mono
from tri import Tri
from quad import Quad
from z_shape import ZShape
from t_shape import TShape
from l1_shape import LShape1
from l2_shape import LShape2
from utils import *
import os
pygame.init()
# --------------------Game Variables---------------------
# screen = pygame.display.set_mode((1280, 720))
window = pygame.display.set_mode((800,600)) # (width,height)
pygame.display.set_caption("Tetris game by Deepanshu Dixit ...")
icon_image = pygame.image.load(os.path.join("icon", "icon.png"))

# Set the icon for the Pygame window
pygame.display.set_icon(icon_image)
exit=False
MIN,MAX = 0,500

blocks = []

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
# Main game loop
over = False
start = False
font = pygame.font.SysFont(None,34,False,False) #type,size,bold,italic
instruction_font = pygame.font.SysFont(None,24,False,False) #type,size,bold,italic
alert_font = pygame.font.SysFont(None,50,False,False) #type,size,bold,italic
score = 0
change_sound = os.path.join("sounds", "change_sound.mp3")
start_sound = os.path.join("sounds","start_sound.mp3")
game_over_sound = os.path.join("sounds","game_over.mp3")
move_sound = os.path.join("sounds","move_sound1.mp3")
# drop_sound = os.path.join("sounds","drop_sound.mp3")


# --------------------Objects & Functions ---------------------------
objects = [Mono(window,MIN,MAX),Tri(window,MIN,MAX),Quad(window,MIN,MAX),ZShape(window,MIN,MAX),TShape(window,MIN,MAX),LShape1(window,MIN,MAX),LShape2(window,MIN,MAX)]
# objects = [LShape1(window,MIN,MAX)]
next = random.choice(objects)
current = random.choice(objects)
current.reset()

def handle_game_over():
    game_over_text = alert_font.render("Game Over !!! ",True,(240,0,0)) # (text,anti-aliasing,(color))
    score_show_text = alert_font.render(f"Score is {score} ",True,(240,0,0)) # (text,anti-aliasing,(color))
    press_enter_text = font.render("Press ENTER to restart.",True,(0,0,0)) # (text,anti-aliasing,(color))
    window.blit(game_over_text,(550,200))
    window.blit(score_show_text,(550,250))
    window.blit(press_enter_text,(520,300))
    
def restart():
    global blocks,over,score
    blocks = []
    over = False
    score = 0


def block_colide():
    global current,next,score,exit,over
    for i in range(5):
        score = resolve_line(blocks,MIN,MAX,score)
    if game_over(blocks):
        over = True
        handle_game_over()
    current = next
    current.reset()
    next = random.choice(objects)
    
def help_window():
    if not over:
        if start:
            next_text = font.render("Next Block",True,(0,0,0)) # (text,anti-aliasing,(color))
            score_text = font.render(f"Score : {score}",True,(0,122,0)) # (text,anti-aliasing,(color))
            instructions1 = instruction_font.render("press left <- arrow key to move left",True,(0,0,0))
            instructions2 = instruction_font.render("press right -> arrow key to move right",True,(0,0,0))
            instructions3 = instruction_font.render("press space key to change block form",True,(0,0,0))
            instructions4 = instruction_font.render("press down v arrow key to fall block",True,(0,0,0))
            instructions5 = font.render("Enjoy the game...",True,(122,111,45))
            pygame.draw.rect(window,(222,217,217),(500,0,300,600)) # (place,(color),(x,y,width,height))
            next.draw_demo(630,160)
            window.blit(score_text,(660,30))
            window.blit(next_text,(585,100))
            window.blit(font.render("Instructions",True,(122,111,45)),(585,360))
            window.blit(instructions1,(505,400))
            window.blit(instructions2,(505,420))
            window.blit(instructions3,(505,440))
            window.blit(instructions4,(505,460))
            window.blit(instructions5,(570,520))
        else:
            start_text = font.render("press ENTER to start",True,(0,0,0)) # (text,anti-aliasing,(color))
            start_text1 = font.render("the Tetris Game",True,(0,0,0)) # (text,anti-aliasing,(color))
            help_bar = ["Objective :-",
                        "     Arrange falling Geometrical shapes",
                        "    to create horizontal lines",
                        "    without gaps.",
                        "    complete lines to disappear",
                        "    boost score",
                        "Controls: -",
                        "    Use arrow keys: ->(Left),<-(Right),",
                        "    (Down) to move shape.",
                        "     Press (space) to change shape form.","Game Over :-",
                        "    Blocks reaching the top end the game."]
            y = 50
            for help in help_bar:
                window.blit(font.render(help,True,"#0C5839"),(40,y))
                y+=40
            window.blit(font.render("Enjoy: Have fun !!",True,(0,0,0)),(100,560))
            pygame.draw.rect(window,(222,217,217),(500,0,300,600)) # (place,(color),(x,y,width,height))
            window.blit(start_text,(550,200))
            window.blit(start_text1,(560,250))
            
    else:
        pygame.draw.rect(window,(222,217,217),(500,0,300,600)) # (place,(color),(x,y,width,height))
        
    

def draw_blocks():
    for block in blocks:
        pygame.draw.rect(window,"#5B015C",(block[0],block[1]-30,30,30))
        
# ------------------MainLoop-----------------------------------
while(not exit):
    for event in pygame.event.get():
        if event.type==pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                pygame.mixer.music.load(move_sound)
                pygame.mixer.music.play()
                current.move_left(blocks)
            if event.key == pygame.K_RIGHT:
                pygame.mixer.music.load(move_sound)
                pygame.mixer.music.play()
                current.move_right(blocks)
            if event.key == pygame.K_DOWN:
                # pygame.mixer.music.load(drop_sound)
                # pygame.mixer.music.play()
                current.fall()
            if event.key == pygame.K_SPACE:
                pygame.mixer.music.load(change_sound)
                pygame.mixer.music.play()
                current.change(blocks)
            if event.key == pygame.K_RETURN:
                if over:
                    restart()
                    pygame.mixer.music.load(start_sound)
                    pygame.mixer.music.play()
                if not start:
                    start = True
                    pygame.mixer.music.load(start_sound)
                    pygame.mixer.music.play()
                    
        if(event.type==pygame.QUIT):
            exit=True
    window.fill("#f0f5d7") #fill color // can also give (r,g,b)
    draw_blocks()
    help_window()
    if current.hit(blocks):
        block_colide()
    if not over:
        if start:
            current.draw()
    else:
        handle_game_over()
    pygame.display.flip()
pygame.quit()
sys.exit()