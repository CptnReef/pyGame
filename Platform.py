import pygame, sys

tile_rects = []
#platform variables
corner0 =  pygame.image.load('images/tiles/surface/corner_dirt0.png')
corner1 =  pygame.image.load('images/tiles/surface/corner_dirt1.png')
corner2 =  pygame.image.load('images/tiles/surface/corner_dirt2.png')
corner3 =  pygame.image.load('images/tiles/surface/corner_dirt3.png')

surface_top =  pygame.image.load('images/tiles/surface/surface_dirt_top.png')
surface_left =  pygame.image.load('images/tiles/surface/surface_dirt_left.png')
surface_right =  pygame.image.load('images/tiles/surface/surface_dirt_right.png')
surface_bottom =  pygame.image.load('images/tiles/surface/surface_dirt_bottom.png')


dirt_imageRoot =  pygame.image.load('images/tiles/surface/dirt0.png')
TILE_SIZE = dirt_imageRoot.get_width()
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


