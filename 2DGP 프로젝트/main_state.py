import random
import json
import os
import threading

from pico2d import *

import game_framework
import title_state



name = "MainState"

cadence = None
heart=None
stick=None
skeleton=None
map=None
bat=None
font = None

class Map:
    def __init__(self):
        self.image1=load_image('wall.png')
        self.image2=load_image('floor.png')

    def draw(self):
        for i in range(1,25+1):
            self.image1.draw(80+24*i,500)
            self.image1.draw(80+24*i,114)
        for i in range(1,15+1):
            self.image1.clip_draw(0,22,24,24,680,510-24*i)
            self.image1.clip_draw(0,22,24,24,104,510-24*i)

        for i in range(1,23+1):
            for j in range(1,15+1):
                self.image2.clip_draw(0,26,24,24,104+24*i,500-24*j) # 좌측 상단 바닥 좌표 = (104+24,500-24)


class Heart:
    def __init__(self):
        self.x,self.y=400,50
        self.frame=0
        self.image=load_image('heart.png')
        self.tmp=0


    def update(self):
        self.tmp=(self.tmp+1)%280
        if(self.tmp==250 or self.tmp==0):
            self.frame=(self.frame+1)%2

    def draw(self):
        self.image.clip_draw(self.frame * 41, 0, 41, 52, self.x, self.y)

class Stick():
    def __init__(self):
        self.x,self.y=0,50
        self.image=load_image('stick.png')

    def update(self):
        self.x+=2
        if(self.x>400):
            self.x=0

    def draw(self):
        self.image.draw(self.x,self.y)
        self.image.draw(800-self.x,self.y)


class Cadence:
    def __init__(self):
        self.x, self.y = 104+24, 500-24
        self.frame = 0
        self.image = load_image('clone.png')
        self.tmp=0

    def update(self):
        self.tmp=(self.tmp+1)%30
        if(self.tmp==0):
            self.frame = (self.frame + 1) % 4

    def draw(self):
        self.image.clip_draw(self.frame * 24, 24, 24, 24, self.x, self.y)

class Skeleton:
    def __init__(self):
        self.x,self.y=104+24*6,500-24
        self.frame=0
        self.image=load_image('skeleton.png')
        self.tmp=0
        self.move=0

    def update(self):
        global cadence
        self.tmp=(self.tmp+1)%30
        self.move=(self.move+1)%200
        if(self.tmp==0):
            self.frame=(self.frame+1)%4
        if(self.move==0):
            if(abs(self.x-cadence.x)-abs(self.y-cadence.y)>=0):
                if(self.x-cadence.x>0):
                    if(self.x-24==cadence.x and self.y==cadence.y):
                        self.x=self.x
                    else:
                        self.x-=24

                elif(self.x-cadence.x<0):
                    if (self.x + 24 == cadence.x and self.y == cadence.y):
                        self.x=self.x
                    else:
                        self.x+=24


            elif(abs(self.x-cadence.x)-abs(self.y-cadence.y)<0):
                if(self.y-cadence.y>0):
                    if (self.x == cadence.x and self.y-24 == cadence.y):
                        self.y=self.y
                    else:
                        self.y-=24

                elif(self.y-cadence.y<0):
                    if (self.x == cadence.x and self.y + 24 == cadence.y):
                        self.y=self.y
                    else:
                        self.y+=24



    def draw(self):
        self.image.clip_draw(self.frame*24,28,24,28,self.x,self.y)


class Bat:
    def __init__(self):
        self.x,self.y=104+24*8,500-24
        self.frame=0
        self.image=load_image('bat.png')
        self.tmp=0
        self.move=0

    def update(self):
        global cadence
        self.tmp=(self.tmp+1)%30
        self.move=(self.move+1)%200
        if(self.tmp==0):
            self.frame=(self.frame+1)%4
        if(self.move==0):
            if(abs(self.x-cadence.x)-abs(self.y-cadence.y)>=0):
                if(self.x-cadence.x>0):
                    if(self.x-24==cadence.x and self.y==cadence.y):
                        self.x=self.x
                    else:
                        self.x-=24

                elif(self.x-cadence.x<0):
                    if (self.x + 24 == cadence.x and self.y == cadence.y):
                        self.x=self.x
                    else:
                        self.x+=24


            elif(abs(self.x-cadence.x)-abs(self.y-cadence.y)<0):
                if(self.y-cadence.y>0):
                    if (self.x == cadence.x and self.y-24 == cadence.y):
                        self.y=self.y
                    else:
                        self.y-=24

                elif(self.y-cadence.y<0):
                    if (self.x == cadence.x and self.y + 24 == cadence.y):
                        self.y=self.y
                    else:
                        self.y+=24



    def draw(self):
        self.image.clip_draw(self.frame*24,28,24,28,self.x,self.y)


    def draw(self):
        self.image.clip_draw(self.frame*24,24,24,24,self.x,self.y)



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
    events=get_events()
    for event in events:
        if event.type==SDL_QUIT:
            game_framework.quit()
        elif event.type==SDL_KEYDOWN and event.key==SDLK_ESCAPE:
            game_framework.change_state(title_state)

        elif event.type==SDL_KEYDOWN and event.key==SDLK_LEFT:
            if(stick.x>300):
                cadence.x-=24

        elif event.type == SDL_KEYDOWN and event.key == SDLK_RIGHT:
            if (stick.x > 300):
                cadence.x += 24

        elif event.type == SDL_KEYDOWN and event.key == SDLK_UP:
            if (stick.x > 300):
                cadence.y += 24

        elif event.type == SDL_KEYDOWN and event.key == SDLK_DOWN:
            if (stick.x > 300):
                cadence.y -= 24


def update():
    heart.update()
    stick.update()
    cadence.update()
    skeleton.update()
    bat.update()

def draw():
    clear_canvas()
    map.draw()
    cadence.draw()
    heart.draw()
    stick.draw()
    skeleton.draw()
    bat.draw()
    update_canvas()