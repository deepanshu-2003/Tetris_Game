import pygame
import os
clear_sound = os.path.join("sounds","clear.mp3")

def clear_line(blocks,y):
    clearable_blocks=[]
    # checking for clearable box
    for block in blocks:
        if block[1] == y:
            clearable_blocks.append(block)
    # clearing blocks
    for block in clearable_blocks:
        blocks.remove(block)
        pygame.mixer.music.load(clear_sound)
        pygame.mixer.music.play()
    # shifting blocks
    for block in blocks:
        if block[1]<y:
            block[1]+=30
    
    
def resolve_line(blocks,min,max,score):
    x_blocks_required_for_line = []
    y_axis_present_in_blocks = []
    for x in range(10,max-30,30):
        x_blocks_required_for_line.append(x)
    for block in blocks:
        if block[1] not in y_axis_present_in_blocks:
            y_axis_present_in_blocks.append(block[1])
            
    
    
    # print(y_axis_present_in_blocks)
    for y in y_axis_present_in_blocks:
        block_with_this_y = []
        for block in blocks:
            if block[1]==y and block[0] not in block_with_this_y:
                block_with_this_y.append(block[0])
        block_with_this_y.sort()
        if block_with_this_y == x_blocks_required_for_line:
            clear_line(blocks,y)
            score+=10
    return score

def game_over(blocks):
    over = False
    for block in blocks:
        if block[1] == 30:
            over = True
    return over

