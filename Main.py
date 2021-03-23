import pygame, sys

clock = pygame.time.Clock()

from pygame.locals import *
pygame.init()
pygame.display.set_caption('Snack-A-Sauras!')

WINDOW_SIZE = (600,400)
screen = pygame.display.set_mode(WINDOW_SIZE,0,32) # game window
display = pygame.Surface((300, 200))

from Stages import *
from Player import *
from Platform import *

while True: # game loop
    display.fill((146,244,255))

    # camera
    true_scroll[0] += (player_rect.x-true_scroll[0]-152)/20
    true_scroll[1] += (player_rect.y-true_scroll[1]-106)/20
    scroll = true_scroll.copy()
    scroll[0] = int(scroll[0])
    scroll[1] = int(scroll[1])

    # parallax background
    pygame.draw.rect(display, (7,80,75),pygame.Rect(0,120,300,80))
    for bg_obj in bg_objs:
        obj_rect = pygame.Rect(bg_obj[1][0]-scroll[0]*bg_obj[0],bg_obj[1][1]-scroll[1]*bg_obj[0],bg_obj[1][2],bg_obj[1][3])
        if bg_obj[0] == 0.5:
            pygame.draw.rect(display, (14,222,150), obj_rect)
        else:
            pygame.draw.rect(display, (9,91,85), obj_rect)
    ############################################################################################################################ 
    # LEVEL EVENTS
    ############################################################################################################################
    tile_rects = []
    y = 0
    for layer in game_map:
        x = 0
        for tile in layer:
            if tile == '1':
                display.blit(dirt_imageRoot,(x*16-scroll[0],y*16-scroll[1]))
            if tile == '2':
                display.blit(dirt_imageSqr,(x*16-scroll[0],y*16-scroll[1]))
            if tile == '3':
                display.blit(surface_top,(x*16-scroll[0],y*16-scroll[1]))
            if tile == '4':
                display.blit(dirt_imageTopR,(x*16-scroll[0],y*16-scroll[1]))
            if tile == '5':
                display.blit(dirt_imageTopL,(x*16-scroll[0],y*16-scroll[1]))
            if tile == '6':
                display.blit(corner1,(x*16-scroll[0],y*16-scroll[1]))
            if tile == '7':
                display.blit(corner0,(x*16-scroll[0],y*16-scroll[1]))
            if tile != '0':
                tile_rects.append(pygame.Rect(x*16,y*16,16,16))
            x += 1
        y += 1

            

    ############################################################################################################################ 
    # PLAYER EVENTS
    ############################################################################################################################
    player_movement = [0,0]
    if move_right == True:
        player_movement[0] += 2
    if move_left == True:
        player_movement[0] -= 2
    player_movement[1] += vertical_momentum
    vertical_momentum += 0.2
    if vertical_momentum > 3:
        vertical_momentum = 3

    if player_movement[0] > 0:
        player_action,player_frame = change_action(player_action,player_frame,'walk')
        player_flip = False
    if player_movement[0] < 0:
        player_action,player_frame = change_action(player_action,player_frame,'walk')
        player_flip = True
    if player_movement[0] == 0:
        player_action,player_frame = change_action(player_action,player_frame,'idle')

    player_rect, collisions = move(player_rect, player_movement, tile_rects)
    if collisions['bottom'] == True:
        vertical_momentum = 0
        air_timer = 0
    else:
        air_timer += 1
    
    player_frame += 1
    if player_frame >= len(animation_db[player_action]):
        player_frame = 0
    player_img_id = animation_db[player_action][player_frame]
    player_image = animation_frames[player_img_id]
    display.blit(pygame.transform.flip(player_image,player_flip,False),(player_rect.x-scroll[0],player_rect.y-scroll[1]))

    ############################################################################################################################ 
    # GAME EVENTS
    ############################################################################################################################ 
    for event in pygame.event.get(): # loop events
        if event.type == QUIT: # checking for quit
            pygame.quit() # end game
            sys.exit() # end script
        if event.type == KEYDOWN: # Key Input
            if event.key == K_RIGHT:
                move_right = True
            if event.key == K_LEFT:
                move_left = True
            if event.key == K_UP:
                if air_timer < 6:
                    vertical_momentum = -5
        if event.type == KEYUP: # Key Input
            if event.key == K_RIGHT:
                move_right = False
            if event.key == K_LEFT:
                move_left = False

    rockslide = pygame.transform.scale(display, WINDOW_SIZE) # Scaling objects with Game Window
    screen.blit(rockslide, (0,0))
    pygame.display.update()
    clock.tick(60)