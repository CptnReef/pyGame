import pygame, sys, random, os
clock = pygame.time.Clock()

from pygame.locals import *
pygame.mixer.pre_init(44100,-16,2,512)
pygame.init()
pygame.mixer.set_num_channels(64)


pygame.display.set_caption('Snack-A-Sauras!')

WINDOW_SIZE = (600,400)
screen = pygame.display.set_mode(WINDOW_SIZE,0,32) # game window
display = pygame.Surface((300, 200))

# WHITE = (255, 255, 255)
# BLACK = (0, 0, 0)
# RED = (255, 0, 0)
# GREEN = (0, 255, 0)
# BLUE = (0, 0, 255)
# all_sprites = pygame.sprite.Group()

from Stages import *
from Player import *
from Platform import *


class Enemy:
    def __init__(self, x, y, direction):
        self.x = x
        self.y = y
        self.direction = direction
        self.stepIndex = 0

    def step(self):
        if self.stepIndex >= 33:
            self.stepIndex = 0

    def draw(self, enm):
        self.step()
        if self.direction == 'images/sheets/player/run/18.png':
            enm.blit(left_enemy[self.stepIndex//3], (self.x, self.y))
        if self.direction == right:
            enm.blit(right_enemy[self.stepIndex // 3], (self.x, self.y))
        self.stepIndex += 1

    def move(self):
        if self.direction == 'images/sheets/player/run/18.png':
            self.x -= 3
        if self.direction == right:
            self.x += 3

    def off_screen(self):
        return not(self.x >= -50 and self.x <= enm_width + 50)
    


while True: # game loop
    display.fill((146,244,255))

    if ground_sound_timer > 0:
        ground_sound_timer -= 1

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
            pygame.draw.rect(display,(20,170,150),obj_rect)
        else:
            pygame.draw.rect(display,(15,76,73),obj_rect)
    ############################################################################################################################ 
    # LEVEL EVENTS
    ############################################################################################################################
    tile_rects = []

    # tile rendering goes here
    for y in range(3):
        for x in range(4):
            target_x = x - 1 + int(round(scroll[0]/(CHUNK_SIZE*16)))
            target_y = y - 1 + int(round(scroll[1]/(CHUNK_SIZE*16)))
            target_chunk = str(target_x) + ';' + str(target_y)
            if target_chunk not in game_map:
                game_map[target_chunk] = generate_chunk(target_x,target_y)
            for tile in game_map[target_chunk]:
                display.blit(tile_index[tile[1]],(tile[0][0]*16-scroll[0],tile[0][1]*16-scroll[1]))
                if tile[1] in [1,2]:
                    tile_rects.append(pygame.Rect(tile[0][0]*16,tile[0][1]*16,16,16))

    # y = 0
    # for layer in game_map:
    #     x = 0
    #     for tile in layer:
    #         if tile == '1':
    #             display.blit(dirt_imageRoot,(x*16-scroll[0],y*16-scroll[1]))
    #         if tile == '2':
    #             display.blit(dirt_imageSqr,(x*16-scroll[0],y*16-scroll[1]))
    #         if tile == '3':
    #             display.blit(surface_top,(x*16-scroll[0],y*16-scroll[1]))
    #         if tile == '4':
    #             display.blit(dirt_imageTopR,(x*16-scroll[0],y*16-scroll[1]))
    #         if tile == '5':
    #             display.blit(dirt_imageTopL,(x*16-scroll[0],y*16-scroll[1]))
    #         if tile == '6':
    #             display.blit(corner1,(x*16-scroll[0],y*16-scroll[1]))
    #         if tile == '7':
    #             display.blit(corner0,(x*16-scroll[0],y*16-scroll[1]))
    #         if tile != '0':
    #             tile_rects.append(pygame.Rect(x*16,y*16,16,16))
    #         x += 1
    #     y += 1

            

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
        if player_movement[0] != 0:
            if ground_sound_timer == 0:
                ground_sound_timer = 30
                ground_sounds.play()
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
            if event.key == K_w:
                pygame.mixer.music.fadeout(1000)             
            if event.key == K_RIGHT:
                move_right = True
            if event.key == K_LEFT:
                move_left = True
            if event.key == K_UP:
                if air_timer < 6:
                    jump_sound.play()
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