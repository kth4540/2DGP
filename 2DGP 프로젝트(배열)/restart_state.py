import game_framework
import weapon_state
from pico2d import *


name = "TitleState"
death=None


def enter():
    global death
    death=load_wav('cadence_death.wav')
    death.play()

def exit():
    global death
    del(death)



def handle_events():
    events=get_events()
    for event in events:
        if event.type==SDL_QUIT:
            game_framework.quit()
        else:
            if(event.type,event.key)==(SDL_KEYDOWN,SDLK_ESCAPE):
                game_framework.quit()
            elif(event.type,event.key)==(SDL_KEYDOWN,SDLK_SPACE):
                game_framework.change_state(weapon_state)




def draw():
    clear_canvas()
    update_canvas()







def update():
    pass


def pause():
    pass


def resume():
    pass