import pygame, sys

global animation_frames
animation_frames = {}

# player animation
def load_animation(path,frame_durations):
    global animation_frames
    animation_name = path.split('/')[-1]
    animation_frame_data = []
    n = 1
    for frame in frame_durations:
        animation_frame_id = animation_name + '_' + str(n)
        img_loc = path + '/' + animation_frame_id + '.png'
        animation_image = pygame.image.load(img_loc).convert()
        animation_image.set_colorkey((255,255,255))
        animation_frames[animation_frame_id] = animation_image.copy()
        for i in range(frame):
            animation_frame_data.append(animation_frame_id)
        n += 1
    return animation_frame_data

def change_action(action_var,frame,new_value):
    if action_var != new_value:
        action_var = new_value
        frame = 0
    return action_var, frame

animation_db = {}
animation_db['idle'] = load_animation('images/sheets/player/idle',[7,7])
animation_db['walk'] = load_animation('images/sheets/player/walk',[7,7,40])

player_action = 'idle'
player_frame = 0
player_flip = False

# player variables
player_rect = pygame.Rect(100,100,5,13)

move_right = False
move_left = False
vertical_momentum = 0 # gravity
air_timer = 0

true_scroll = [0,0]
