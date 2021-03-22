import pygame, sys
clock = pygame.time.Clock()
from pygame.locals import *
from Player import *
from Platform import *
from Level1 import *

#game variables
pygame.init()
pygame.display.set_caption('Snack Attack!')
WINDOW_SIZE = (600,400)
screen = pygame.display.set_mode(WINDOW_SIZE,0,32) # game window
display = pygame.Surface((300, 200))

#test variables
test_rect = pygame.Rect(100,100,100,50)

while True: # game loop
    display.fill((146,244,255))

    ############################################################################################################################ 
    # LEVEL EVENTS
    ############################################################################################################################
    y = 0
    for row in game_map:
        x = 0
        for tile in row:
            if tile == '1':
                display.blit(dirt_imageRoot,(x * TILE_SIZE, y * TILE_SIZE))
            if tile == '2':
                display.blit(dirt_imageSqr,(x * 16, y * 16))
            if tile == '3':
                display.blit(surface_top,(x * 16, y * 16))
            if tile == '4':
                display.blit(dirt_imageTopR,(x * 16, y * 16))
            if tile == '5':
                display.blit(dirt_imageTopL,(x * 16, y * 16))
            if tile == '6':
                display.blit(corner1,(x * 16, y * 16))
            if tile == '7':
                display.blit(corner0,(x * 16, y * 16))
            if tile != '0':
                tile_rects.append(pygame.Rect(x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE))
            x += 1
        y += 1

            

    ############################################################################################################################ 
    # PLAYER EVENTS
    ############################################################################################################################
    display.blit(player_image,player_location)

    player_movement = [0,0]
    if move_right:
        player_movement[0] += 2
    if move_left:
        player_movement[0] -= 2

    player_movement[1] += player_y_momentum
    playerY_momentum += 0.2
    if playerY_momentum > 3:
        playerY_momentum = 3

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
        if event.type == KEYUP: # Key Input
            if event.key == K_RIGHT:
                move_right = False
            if event.key == K_LEFT:
                move_left = False

    rockslide = pygame.transform.scale(display, WINDOW_SIZE) # Scaling objects with Game Window
    screen.blit(rockslide, (0,0))
    pygame.display.update()
    clock.tick(60)
