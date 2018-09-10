from pico2d import *
import math
import os
os.chdir('C:\\GitHub\\2DGP\\Drills\\Drill-03')
open_canvas()
grass = load_image('grass.png')
character = load_image('character.png')
x=400
y=30
rnd=0
drt=1
while (True):
    clear_canvas_now()
    grass.draw_now(400, 30)
    if(drt==1):
        character.draw_now(x,y)
        x=x+5
        if(x==760):
            drt=2
    elif(drt==2):
        character.draw_now(x,y)
        y=y+5
        if(y==560):
            drt=3
    elif(drt==3):
        character.draw_now(x,y)
        x=x-5
        if(x==0):
            drt=4
    elif(drt==4):
        character.draw_now(x,y)
        y=y-5
        if(y==30):
            drt=5
    elif(drt==5):
        character.draw_now(x,y)
        x=x+5
        if(x==400):
            drt=6
    elif(drt==6):
        character.draw_now(x,y)
        x=400+200*math.cos(3/2*math.pi+math.pi*rnd/18)
        y=230+200*math.sin(3/2*math.pi+math.pi*rnd/18)
        rnd=rnd+1
        if(rnd==36):
            drt=1
            x=400
            y=30
            rnd=0
    delay(0.02)
close_canvas()
