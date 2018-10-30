from pico2d import *
import math
import random
import game_world
import game_framework
import main_state
import boy

PIXEL_PER_METER = (10.0/0.3)
RUN_SPEED_KMPH = 20.0
RUN_SPEED_MPM = (RUN_SPEED_KMPH*1000.0/60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM/60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS*PIXEL_PER_METER)

ghost_time=get_time()
class Ghost:
    image = None

    def __init__(self):
        if Ghost.image == None:
            Ghost.image = load_image('animation_sheet.png')
        self.x, self.y = main_state.boy.x,main_state.boy.y
        self.rad=-90
        self.up=90
    def draw(self):
        if(main_state.boy.cur_state==boy.SleepState):
            self.image.opacify(random.randint(0,6)/10)
            self.image.clip_draw(0,300,100,100,self.x,self.y)

    def update(self):
        global rad_time

        if (main_state.boy.cur_state == boy.IdleState):
            self.x, self.y = main_state.boy.x, main_state.boy.y
        elif(main_state.boy.cur_state==boy.SleepState):
            self.x=main_state.boy.x+150*math.cos(math.radians(self.rad))
            self.y =240+150 * math.sin(math.radians(self.rad))
            self.rad+=720*game_framework.frame_time


        if self.x < 25 or self.x > 1600 - 25:
            game_world.remove_object(self)
