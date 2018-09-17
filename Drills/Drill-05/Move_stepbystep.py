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
    x, y = 535, 470
    frame = 0
    count = 0
    while (count < 20):
        clear_canvas()
        character.clip_draw(frame * 100, 0, 100, 100, x, y)
        update_canvas()
        frame = (frame + 1) % 8
        x = x - (535 - 477) // 20
        y = y - (470 - 203) // 20
        count = count + 1
        delay(0.05)
def Move_477_203_to_715_136():
    x, y = 477, 203
    frame = 0
    count = 0
    while (count < 20):
        clear_canvas()
        character.clip_draw(frame * 100, 100, 100, 100, x, y)
        update_canvas()
        frame = (frame + 1) % 8
        x = x - (477 - 715) // 20
        y = y - (203 - 136) // 20
        count = count + 1
        delay(0.05)
def Move_715_136_to_316_225():
    x, y = 715, 136
    frame = 0
    count = 0
    while (count < 20):
        clear_canvas()
        character.clip_draw(frame * 100, 0, 100, 100, x, y)
        update_canvas()
        frame = (frame + 1) % 8
        x = x - (715 - 316) // 20
        y = y - (136 - 225) // 20
        count = count + 1
        delay(0.05)
def Move_316_225_to_510_92():
    x, y = 316, 225
    frame = 0
    count = 0
    while (count < 20):
        clear_canvas()
        character.clip_draw(frame * 100, 100, 100, 100, x, y)
        update_canvas()
        frame = (frame + 1) % 8
        x = x - (316 - 510) // 20
        y = y - (225 - 92) // 20
        count = count + 1
        delay(0.05)
def Move_510_92_to_692_518():
    x, y = 510, 92
    frame = 0
    count = 0
    while (count < 20):
        clear_canvas()
        character.clip_draw(frame * 100, 100, 100, 100, x, y)
        update_canvas()
        frame = (frame + 1) % 8
        x = x - (510 - 692) // 20
        y = y - (92 - 518) // 20
        count = count + 1
        delay(0.05)
def Move_692_518_to_682_336():
    x, y = 692, 518
    frame = 0
    count = 0
    while (count < 20):
        clear_canvas()
        character.clip_draw(frame * 100, 0, 100, 100, x, y)
        update_canvas()
        frame = (frame + 1) % 8
        x = x - (692 - 682) // 20
        y = y - (518 - 336) // 20
        count = count + 1
        delay(0.05)
def Move_682_336_to_712_349():
    x, y = 682, 336
    frame = 0
    count = 0
    while (count < 20):
        clear_canvas()
        character.clip_draw(frame * 100, 100, 100, 100, x, y)
        update_canvas()
        frame = (frame + 1) % 8
        x = x - (682 - 712) // 20
        y = y - (336 - 349) // 20
        count = count + 1
        delay(0.05)

def Go_Back():
    x, y = 712, 349
    frame = 0
    count = 0
    while (count < 20):
        clear_canvas()
        character.clip_draw(frame * 100, 0, 100, 100, x, y)
        update_canvas()
        frame = (frame + 1) % 8
        x = x - (712 - 203) // 20
        y = y - (349 - 535) // 20
        count = count + 1
        delay(0.05)



while(True):
    #Move_203_535_to_132_243()
    #Move_132_243_to_535_470()
    #Move_535_470_to_477_203()
    #Move_477_203_to_715_136()
    #Move_715_136_to_316_225()
    #Move_316_225_to_510_92()
    #Move_510_92_to_692_518()
    #Move_692_518_to_682_336()
    #Move_682_336_to_712_349()
    #Go_Back()
close_canvas()

