import pygame, sys

#player variables
player_image = pygame.image.load('images/sheets/player/idle/1.png').convert()
player_image.set_colorkey((255,255,255))
player_rect = pygame.Rect(100,100,5,13)

move_right = False
move_left = False
vertical_momentum = 0 # gravity
air_timer = 0

true_scroll = [0,0]
