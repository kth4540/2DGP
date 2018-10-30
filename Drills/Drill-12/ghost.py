from pico2d import *
import math
import time
import game_world
import main_state
import boy

rad_time=0.0

class Ghost:
    image = None

    def __init__(self):
        if Ghost.image == None:
            Ghost.image = load_image('ball21x21.png')
        self.x, self.y = main_state.boy.x,main_state.boy.y
        self.rad=-90
    def draw(self):
        if(main_state.boy.cur_state==boy.SleepState):
            self.image.draw(self.x, self.y)

    def update(self):
        global rad_time

        if (main_state.boy.cur_state == boy.IdleState):
            self.x, self.y = main_state.boy.x, main_state.boy.y
        elif(main_state.boy.cur_state==boy.SleepState):
            self.x=main_state.boy.x+300*math.cos(math.pi/180*self.rad)
            self.y =390+ 300 * math.sin(math.pi / 180 * self.rad)
            #if((get_time()-rad_time)):
            self.rad+=1


        if self.x < 25 or self.x > 1600 - 25:
            game_world.remove_object(self)
