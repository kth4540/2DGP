from pico2d import *
import turtle
import random
width,height=1280,1024
open_canvas(width,height)
map=load_image('KPU_GROUND.png')
chararter=load_image('animation_sheet.png')
size=10
points=[(random.randint(200,1000),random.randint(200,800))for i in range(size)]
n=1
x=0
y=0
frame=0

def draw_curve_10_points(p1, p2, p3, p4, p5,p6,p7,p8,p9,p10):
    global x
    global y
    global frame
    # draw p1-p2
    for i in range(0, 100, 2):
        clear_canvas()
        map.draw(width/2,height/2)
        t = i / 100
        x = ((-t ** 3 + 2 * t ** 2 - t) * p10[0] + (3 * t ** 3 - 5 * t ** 2 + 2) * p1[0] + (
                -3 * t ** 3 + 4 * t ** 2 + t) * p2[0] + (t ** 3 - t ** 2) * p3[0]) / 2
        y = ((-t ** 3 + 2 * t ** 2 - t) * p10[1] + (3 * t ** 3 - 5 * t ** 2 + 2) * p1[1] + (
                -3 * t ** 3 + 4 * t ** 2 + t) * p2[1] + (t ** 3 - t ** 2) * p3[1]) / 2
        if(x>p1[0]):
            chararter.clip_draw(100*frame,100,100,100,x,y)
        elif(x<p1[0]):
            chararter.clip_draw(100 * frame, 0, 100, 100, x, y)
        frame=(frame+1)%8
        update_canvas()
        get_events()
        delay(0.05)


# draw p2-p3
    for i in range(0, 100, 2):
        clear_canvas()
        map.draw(width/2,height/2)
        t = i / 100
        x = ((-t ** 3 + 2 * t ** 2 - t) * p1[0] + (3 * t ** 3 - 5 * t ** 2 + 2) * p2[0] + (
                -3 * t ** 3 + 4 * t ** 2 + t) * p3[0] + (t ** 3 - t ** 2) * p4[0]) / 2
        y = ((-t ** 3 + 2 * t ** 2 - t) * p1[1] + (3 * t ** 3 - 5 * t ** 2 + 2) * p2[1] + (
                -3 * t ** 3 + 4 * t ** 2 + t) * p3[1] + (t ** 3 - t ** 2) * p4[1]) / 2
        if (x > p2[0]):
            chararter.clip_draw(100 * frame, 100, 100, 100, x, y)
        elif (x < p2[0]):
            chararter.clip_draw(100 * frame, 0, 100, 100, x, y)
        frame=(frame+1)%8
        update_canvas()
        get_events()
        delay(0.05)
# draw p3-p4
    for i in range(0, 100, 2):
        clear_canvas()
        map.draw(width/2,height/2)
        t = i / 100
        x = ((-t ** 3 + 2 * t ** 2 - t) * p2[0] + (3 * t ** 3 - 5 * t ** 2 + 2) * p3[0] + (
                -3 * t ** 3 + 4 * t ** 2 + t) * p4[0] + (t ** 3 - t ** 2) * p5[0]) / 2
        y = ((-t ** 3 + 2 * t ** 2 - t) * p2[1] + (3 * t ** 3 - 5 * t ** 2 + 2) * p3[1] + (
                -3 * t ** 3 + 4 * t ** 2 + t) * p4[1] + (t ** 3 - t ** 2) * p5[1]) / 2
        if (x > p3[0]):
            chararter.clip_draw(100 * frame, 100, 100, 100, x, y)
        elif (x < p3[0]):
            chararter.clip_draw(100 * frame, 0, 100, 100, x, y)
        frame=(frame+1)%8
        update_canvas()
        get_events()
        delay(0.05)
# draw p4-p5
    for i in range(0, 100, 2):
        clear_canvas()
        map.draw(width/2,height/2)
        t = i / 100
        x = ((-t ** 3 + 2 * t ** 2 - t) * p3[0] + (3 * t ** 3 - 5 * t ** 2 + 2) * p4[0] + (
                -3 * t ** 3 + 4 * t ** 2 + t) * p5[0] + (t ** 3 - t ** 2) * p6[0]) / 2
        y = ((-t ** 3 + 2 * t ** 2 - t) * p3[1] + (3 * t ** 3 - 5 * t ** 2 + 2) * p4[1] + (
                -3 * t ** 3 + 4 * t ** 2 + t) * p5[1] + (t ** 3 - t ** 2) * p6[1]) / 2
        if (x > p4[0]):
            chararter.clip_draw(100 * frame, 100, 100, 100, x, y)
        elif (x < p4[0]):
            chararter.clip_draw(100 * frame, 0, 100, 100, x, y)
        frame=(frame+1)%8
        update_canvas()
        get_events()
        delay(0.05)
# draw p5-p6
    for i in range(0, 100, 2):
        clear_canvas()
        map.draw(width/2,height/2)
        t = i / 100
        x = ((-t ** 3 + 2 * t ** 2 - t) * p4[0] + (3 * t ** 3 - 5 * t ** 2 + 2) * p5[0] + (
                -3 * t ** 3 + 4 * t ** 2 + t) * p6[0] + (t ** 3 - t ** 2) * p7[0]) / 2
        y = ((-t ** 3 + 2 * t ** 2 - t) * p4[1] + (3 * t ** 3 - 5 * t ** 2 + 2) * p5[1] + (
                -3 * t ** 3 + 4 * t ** 2 + t) * p6[1] + (t ** 3 - t ** 2) * p7[1]) / 2
        if (x > p5[0]):
            chararter.clip_draw(100 * frame, 100, 100, 100, x, y)
        elif (x < p5[0]):
            chararter.clip_draw(100 * frame, 0, 100, 100, x, y)
        frame=(frame+1)%8
        update_canvas()
        get_events()
        delay(0.05)
# draw p6-p7
    for i in range(0, 100, 2):
        clear_canvas()
        map.draw(width/2,height/2)
        t = i / 100
        x = ((-t ** 3 + 2 * t ** 2 - t) * p5[0] + (3 * t ** 3 - 5 * t ** 2 + 2) * p6[0] + (
                -3 * t ** 3 + 4 * t ** 2 + t) * p7[0] + (t ** 3 - t ** 2) * p8[0]) / 2
        y = ((-t ** 3 + 2 * t ** 2 - t) * p5[1] + (3 * t ** 3 - 5 * t ** 2 + 2) * p6[1] + (
                -3 * t ** 3 + 4 * t ** 2 + t) * p7[1] + (t ** 3 - t ** 2) * p8[1]) / 2
        if (x > p6[0]):
            chararter.clip_draw(100 * frame, 100, 100, 100, x, y)
        elif (x < p6[0]):
            chararter.clip_draw(100 * frame, 0, 100, 100, x, y)
        frame=(frame+1)%8
        update_canvas()
        get_events()
        delay(0.05)
# draw p7-p8
    for i in range(0, 100, 2):
        clear_canvas()
        map.draw(width/2,height/2)
        t = i / 100
        x = ((-t ** 3 + 2 * t ** 2 - t) * p6[0] + (3 * t ** 3 - 5 * t ** 2 + 2) * p7[0] + (
                -3 * t ** 3 + 4 * t ** 2 + t) * p8[0] + (t ** 3 - t ** 2) * p9[0]) / 2
        y = ((-t ** 3 + 2 * t ** 2 - t) * p6[1] + (3 * t ** 3 - 5 * t ** 2 + 2) * p7[1] + (
                -3 * t ** 3 + 4 * t ** 2 + t) * p8[1] + (t ** 3 - t ** 2) * p9[1]) / 2
        if (x > p7[0]):
            chararter.clip_draw(100 * frame, 100, 100, 100, x, y)
        elif (x < p7[0]):
            chararter.clip_draw(100 * frame, 0, 100, 100, x, y)
        frame=(frame+1)%8
        update_canvas()
        get_events()
        delay(0.05)








while(True):
    draw_curve_10_points(points[0],points[1],points[2],points[3],points[4],points[5],points[6],points[7],points[8],points[9])
close_canvas()
