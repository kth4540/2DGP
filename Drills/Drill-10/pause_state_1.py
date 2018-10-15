import game_framework
import main_state
import title_state
from pico2d import*
pause=None
image=None
class Pause:
    def __init__(self):
        self.image=load_image('pause.png')
    def draw(self):
        self.image.draw(400,300)

def enter():
    global pause
    pause=Pause()

def exit():
    global pause
    del(pause)

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