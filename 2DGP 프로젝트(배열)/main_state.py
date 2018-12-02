from pico2d import *

import game_framework
import title_state

from MAP import Map
from HEART import Heart
from STICK import Stick
from CADENCE import Cadence
from SKELETON import Skeleton
from BAT import Bat
from DRAGON import Dragon

respawn_time=0
respawn_check=0
skel_respawn=True
bat_respawn=True
dragon_respawn=True

respawn_shorten=0

name = "MainState"

map=None
heart=None
stick=None

skeleton=[]
skel_num=2


bat=[]
bat_num=2

dragon=[]
dragon_num=1

cadence = None



def enter():
    global cadence,heart,stick,skeleton,bat,dragon,map
    cadence=Cadence()
    heart=Heart()
    stick=Stick()
    map=Map()
    for i in range(skel_num):
        skeleton.append(Skeleton())
    for i in range(skel_num):
        bat.append(Bat())
    for i in range(dragon_num):
        dragon.append(Dragon())

def exit():
    global cadence,heart,stick,skeleton,bat,dragon,map
    del(cadence)
    del(heart)
    del(stick)
    del(skeleton)
    del(bat)
    del(dragon)
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
    global respawn_time,respawn_check,skel_num,bat_num,dragon_num,skel_respawn,bat_respawn,dragon_respawn,respawn_shorten
    heart.update()
    stick.update()
    cadence.update()
    for i in range(skel_num):
        if(skeleton[i].life>0):
            skeleton[i].update()
    for i in range(bat_num):
        if(bat[i].life>0):
            bat[i].update()
    for i in range(dragon_num):
        if (dragon[i].life > 0):
            dragon[i].update()



    respawn_time+=400 * 130 / 60 * game_framework.frame_time

    if respawn_time>=800:
        respawn_time=0
        respawn_check+=1
        skel_respawn=False
        bat_respawn=False
        dragon_respawn=False

    if (respawn_check%(10-respawn_shorten) == 0 and skel_respawn==False):
        skeleton.append(Skeleton())
        skel_num += 1
        skel_respawn=True

    if (respawn_check%(8-respawn_shorten) == 0 and bat_respawn==False):
        bat.append(Bat())
        bat_num += 1
        bat_respawn=True

    if (respawn_check%(60-(respawn_shorten*5)) == 0 and dragon_respawn==False):
        dragon.append(Dragon())
        dragon_num += 1
        dragon_respawn=True
        respawn_shorten+=1






def draw():
    clear_canvas()
    map.draw()
    cadence.draw()
    heart.draw()
    stick.draw()
    for i in range(skel_num):
        skeleton[i].draw()
    for i in range(bat_num):
        bat[i].draw()
    for i in range(dragon_num):
        dragon[i].draw()
    update_canvas()
