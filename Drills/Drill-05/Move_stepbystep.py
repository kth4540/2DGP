from pico2d import *
open_canvas()
grass = load_image('grass.png')
character = load_image('animation_sheet.png')

chx,chy=203,535
frame=0
def Move(x,y):
    if(x-chx>0):
        Move_left()
    elif(x-chx<0):
        Move_right()

def Move_left():
    pass
def Move_right():
    pass

while(True):
    Move(chx,chy)
close_canvas()

