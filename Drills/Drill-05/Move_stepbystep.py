from pico2d import *
open_canvas()
grass = load_image('grass.png')
character = load_image('animation_sheet.png')


def Move_1():
    x,y=203,535
    frame=0
    count=0
    while(count<20):
        clear_canvas()
        character.clip_draw(frame*100,0,100,100,x,y)
        update_canvas()
        frame=(frame+1)%8
        x=x-(203-132)//20
        y=y-(535-243)//20
        count=count+1
        delay(0.05)
def Move_2():
    pass
def Move_3():
    pass
def Move_4():
    pass
def Move_5():
    pass
def Move_6():
    pass
def Move_7():
    pass
def Move_8():
    pass
def Move_9():
    pass
def Move_10():
    pass
def Go_Back():
    pass



while(True):
    #Move_1()
    Move_2()
    Move_3()
    Move_4()
    Move_5()
    Move_6()
    Move_7()
    Move_8()
    Move_9()
    Move_10()
    Go_Back()
close_canvas()

