import pygame, sys

#player variables
player_image = pygame.image.load('images/gifs/player.gif')
move_right = False
move_left = False
playerY_momentum = 0 # gravity
player_rect = pygame.Rect(player_location[0],player_location[1],player_image.get_width(),player_image.get_height())
