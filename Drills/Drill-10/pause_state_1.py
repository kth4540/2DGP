import game_framework
import main_state
from pico2d import*
pause=None

class Pause:
    def __init__(self):
        self.image=load_image('pause.png')
    def draw(self):
        self.image.draw(400,300)

def enter():
    pass

def exit():
    pass

def handle_events():
    pass

def draw():
    pass

def update():
    pass

def pause():
    pass

def resume():
    pass