from pico2d import *
import game_world
import main_state
import boy

class Ghost:
    image = None

    def __init__(self):
        if Ghost.image == None:
            Ghost.image = load_image('ball21x21.png')
        self.x, self.y = main_state.boy.x,main_state.boy.y

    def draw(self):
        if(main_state.boy.cur_state==boy.SleepState):
            self.image.draw(self.x, self.y)

    def update(self):
        pass

        if self.x < 25 or self.x > 1600 - 25:
            game_world.remove_object(self)
