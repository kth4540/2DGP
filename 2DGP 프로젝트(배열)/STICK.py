from pico2d import*
import game_framework
import main_state
class Stick():
    def __init__(self):
        self.x,self.y=0,50
        self.image=load_image('stick.png')

    def update(self):
        self.x+=400*130/60*game_framework.frame_time
        if(self.x>=400):
            self.x=0

    def draw(self):
        self.image.draw(self.x,self.y)
        self.image.draw(800-self.x,self.y)