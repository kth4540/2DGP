from pico2d import*

open_canvas()
grass=load_image('grass.png')
character=load_image('animation_sheet.png')

def run_left():
    x,y=0+25,90
    frame=0
    while(x<800-25):
        clear_canvas()
        grass.draw(400,30)
        character.clip_draw(frame*100,100,100,100,x,y)
        update_canvas()
        frame=(frame+1)%8
        x+=5
        delay(0.05)
        get_events()

def run_right():
    x, y = 800 - 25, 90
    frame = 0
    while (x > 0+25):
        clear_canvas()
        grass.draw(400, 30)
        character.clip_draw(frame * 100, 0, 100, 100, x, y)
        update_canvas()
        frame = (frame + 1) % 8
        x -= 5
        delay(0.05)
        get_events()

while(True):
    run_left()
    run_right()

close_canvas()