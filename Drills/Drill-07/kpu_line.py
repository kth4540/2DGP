from pico2d import *
import turtle
import random
width,height=1280,1024
open_canvas(width,height)
map=load_image('KPU_GROUND.png')
chararter=load_image('animation_sheet.png')
size=5
points=[(random.randint(200,1000),random.randint(200,800))for i in range(size)]
n=1
x=0
y=0
frame=0
def move(p1,p2):
    global x
    global y
    global frame
    for i in range(0,100,2):
        t=i/100
        x = (1 - t) * p1[0] + t * p2[0]
        y = (1 - t) * p1[1] + t * p2[1]
        clear_canvas()
        map.draw(width/2,height/2)
        if(p1[0]>p2[0]):
            chararter.clip_draw(frame*100,0,100,100,x,y)
        elif(p1[0]<p2[0]):
            chararter.clip_draw(frame * 100, 100, 100, 100, x, y)
        frame=(frame+1)%8
        update_canvas()
        delay(0.05)
        get_events()




while(True):
    move(points[n-1],points[n])
    n=(n+1)%size
close_canvas()
