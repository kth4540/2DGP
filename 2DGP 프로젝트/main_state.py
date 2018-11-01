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
skeleton=None
cadence = None
bat=None


def enter():
    global cadence,heart,stick,skeleton,bat,map
    cadence=Cadence()
    heart=Heart()
    stick=Stick()
    map=Map()
    skeleton=Skeleton()
    bat=Bat()

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
    global cadence
    global skeleton
    global bat
    global map
    events=get_events()
    for event in events:
        if event.type==SDL_QUIT:
            game_framework.quit()
        elif event.type==SDL_KEYDOWN and event.key==SDLK_ESCAPE:
            game_framework.change_state(title_state)

        elif event.type==SDL_KEYDOWN and event.key==SDLK_LEFT:
            if(stick.x>300):
                if(cadence.x-24==bat.x and cadence.y==bat.y):
                    bat.life-=1
                    bat.x=0
                    bat.y=0
                    cadence.attack()

                elif(cadence.x-24==skeleton.x and cadence.y==skeleton.y):
                    skeleton.life-=1
                    skeleton.x=0
                    skeleton.y=0
                else:
                    cadence.x-=24

        elif event.type == SDL_KEYDOWN and event.key == SDLK_RIGHT:
            if (stick.x > 300):
                if (cadence.x + 24 == bat.x and cadence.y==bat.y):
                    bat.life -= 1
                    bat.x = 0
                    bat.y = 0


                elif (cadence.x + 24 == skeleton.x and cadence.y==skeleton.y):
                    skeleton.life -= 1
                    skeleton.x = 0
                    skeleton.y = 0
                else:
                    cadence.x += 24

        elif event.type == SDL_KEYDOWN and event.key == SDLK_UP:
            if (stick.x > 300):
                if (cadence.y + 24 == bat.y and cadence.x == bat.x):
                    bat.life -= 1
                    bat.x = 0
                    bat.y = 0
                elif (cadence.y + 24 == skeleton.y and cadence.x== skeleton.x):
                    skeleton.life -= 1
                    skeleton.x = 0
                    skeleton.y = 0
                else:
                    cadence.y += 24

        elif event.type == SDL_KEYDOWN and event.key == SDLK_DOWN:
            if (stick.x > 300):
                if (cadence.y - 24 == bat.y and cadence.x == bat.x):
                    bat.life -= 1
                    bat.x = 0
                    bat.y = 0
                elif (cadence.y - 24 == skeleton.y and cadence.x == skeleton.x):
                    skeleton.life -= 1
                    skeleton.x = 0
                    skeleton.y = 0
                else:
                    cadence.y -= 24


def update():
    global cadence, heart, stick, skeleton, bat, map
    heart.update()
    stick.update()
    cadence.update()
    if(skeleton.life!=0):
        skeleton.update()
    if(bat.life!=0):
        bat.update()

def draw():
    global cadence, heart, stick, skeleton, bat, map
    clear_canvas()
    map.draw()
    cadence.draw()
    heart.draw()
    stick.draw()
    skeleton.draw()
    bat.draw()
    update_canvas()
