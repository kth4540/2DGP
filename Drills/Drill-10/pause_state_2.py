import game_framework
import main_state
import title_state
from pico2d import*
pause=None
image=None
count=0
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
    events=get_events()
    for event in events:
        if event.type==SDL_QUIT:
            game_framework.quit()
        elif event.type==SDL_KEYDOWN and event.key==SDLK_ESCAPE:
            game_framework.change_state(title_state)
        elif event.type==SDL_KEYDOWN and event.key==SDLK_p:
            game_framework.pop_state()

def draw():
    global image
    global count
    clear_canvas()
    if(count<1):
        pause.draw()
    update_canvas()

def update():
    global count
    count=(count+1)%2

def pause():
    pass

def resume():
    pass