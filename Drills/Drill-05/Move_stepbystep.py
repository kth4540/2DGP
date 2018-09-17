from pico2d import *
open_canvas()
grass = load_image('grass.png')
character = load_image('animation_sheet.png')


def Move_203_535_to_132_243():
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
def Move_132_243_to_535_470():
    x,y=132,243
    frame=0
    count=0
    while(count<20):
        clear_canvas()
        character.clip_draw(frame * 100, 100, 100, 100, x, y)
        update_canvas()
        frame=(frame+1)%8
        x=x-(132-535)//20
        y=y-(243-470)//20
        count=count+1
        delay(0.05)
def Move_535_470_to_477_203():
    pass
def Move_477_203_to_715_136():
    pass
def Move_715_136_to_316_225():
    pass
def Move_316_225_to_510_92():
    pass
def Move_510_92_to_692_518():
    pass
def Move_692_518_to_682_336():
    pass
def Move_682_336_to_712_349():
    pass

def Go_Back():
    pass



while(True):
    #Move_203_535_to_132_243()
    Move_132_243_to_535_470()
    Move_535_470_to_477_203()
    Move_477_203_to_715_136()
    Move_715_136_to_316_225()
    Move_316_225_to_510_92()
    Move_510_92_to_692_518()
    Move_692_518_to_682_336()
    Move_682_336_to_712_349()
    Go_Back()
close_canvas()

