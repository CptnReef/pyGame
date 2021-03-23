import pygame, sys, os

os.getcwd()

# background
bg_objs = [[0.25,[120,10,70,400]],[0.25,[280,30,40,400]],[0.5,[30,40,40,400]],[0.5,[130,90,40,400]], ]

# platform variables
corner0 =  pygame.image.load('images/tiles/surface/corner_dirt0.png')
corner1 =  pygame.image.load('images/tiles/surface/corner_dirt1.png')
corner2 =  pygame.image.load('images/tiles/surface/corner_dirt2.png')
corner3 =  pygame.image.load('images/tiles/surface/corner_dirt3.png')

surface_top =  pygame.image.load('images/tiles/surface/surface_dirt_top.png')
surface_left =  pygame.image.load('images/tiles/surface/surface_dirt_left.png')
surface_right =  pygame.image.load('images/tiles/surface/surface_dirt_right.png')
surface_bottom =  pygame.image.load('images/tiles/surface/surface_dirt_bottom.png')

dirt_imageRoot =  pygame.image.load('images/tiles/surface/dirt0.png')
dirt_imageTopL =  pygame.image.load('images/tiles/surface/dirt1.png')
dirt_imageTopR =  pygame.image.load('images/tiles/surface/dirt2.png')
dirt_imageBotL =  pygame.image.load('images/tiles/surface/dirt3.png')
dirt_imageBotR =  pygame.image.load('images/tiles/surface/dirt4.png')
dirt_imageSqr =  pygame.image.load('images/tiles/surface/dirt5.png')
bold_dirt_imageSqr =  pygame.image.load('images/tiles/bold_dirt0.png')
sharp_dirt_imageSqr =  pygame.image.load('images/tiles/sharp_dirt0.png')
tough_dirt_imageSqr =  pygame.image.load('images/tiles/tough_dirt0.png')
royal_dirt_imageSqr =  pygame.image.load('images/tiles/royal_dirt0.png')
old_dirt_imageSqr =  pygame.image.load('images/tiles/old_dirt0.png')

# sound
jump_sound = pygame.mixer.Sound('sounds/jump.wav')
jump_sound.set_volume(0.3)
ground_sounds = pygame.mixer.Sound('sounds/thud.wav')
ground_sounds.set_volume(0.15)

# pygame.mixer.music.load('sounds/music1.wav')
# pygame.mixer.music.play(-1)
