from pico2d import *

import game_framework
import title_state

from MAP import Map
from HEART import Heart
from STICK import Stick
from CADENCE import Cadence
from SKELETON import Skeleton
from BAT import Bat


name = "MainState"

map=None
heart=None
stick=None
skeleton=[]
cadence = None
bat=[]


def enter():
    global cadence,heart,stick,skeleton,bat,map
    cadence=Cadence()
    heart=Heart()
    stick=Stick()
    map=Map()
    skeleton.append(Skeleton())
    bat.append(Bat())
    skeleton.append(Skeleton())
    bat.append(Bat())

def exit():
    global cadence,heart,stick,skeleton,bat,map
    del(cadence)
    del(heart)
    del(stick)
    del(skeleton)
    del(bat)
    del(map)



def pause():
    pass


def resume():
    pass


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        else:
            cadence.handle_event(event)


def update():
    heart.update()
    stick.update()
    cadence.update()
    for i in range(2):
        if(skeleton[i].life>0):
            skeleton[i].update()
    for i in range(2):
        if(bat[i].life>0):
            bat[i].update()

def draw():
    clear_canvas()
    map.draw()
    cadence.draw()
    heart.draw()
    stick.draw()
    for i in range(2):
        skeleton[i].draw()
    for i in range(2):
        bat[i].draw()
    update_canvas()
