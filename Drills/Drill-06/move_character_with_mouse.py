from pico2d import *

KPU_WIDTH, KPU_HEIGHT = 1280, 1024


def handle_events():
    global running
    global x,y
    global chx,chy
    global cntstart
    global tmpx, tmpy
    global count
    events=get_events()
    for event in events:
        if event.type==SDL_QUIT:
            running=False
        elif event.type==SDL_MOUSEMOTION:
            x,y=event.x, KPU_HEIGHT-1-event.y
        elif event.type==SDL_KEYDOWN and event.key==SDLK_ESCAPE:
            running=False
        elif event.type==SDL_MOUSEBUTTONDOWN:
            cntstart=1
            tmpx,tmpy=event.x-15, KPU_HEIGHT-1-event.y+20


open_canvas(KPU_WIDTH,KPU_HEIGHT)
kpu_ground = load_image('KPU_GROUND.png')
character = load_image('animation_sheet.png')
arrow=load_image('hand_arrow.png')
running = True
x, y = KPU_WIDTH // 2, KPU_HEIGHT // 2
frame = 0
hide_cursor()
chx,chy=1280//2,1024//2
cntstart=0
count=0
while running:
    clear_canvas()
    kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
    arrow.draw(x,y)
    character.clip_draw(frame * 100, 100 * 1, 100, 100, chx, chy)
    update_canvas()
    frame = (frame + 1) % 8
    if(cntstart==1):
        chx=chx+(tmpx-chx)//20
        chy=chy+(tmpy-chy)//20
        count+=1
        if(count==20):
            cntstart=0
    delay(0.02)
    handle_events()

close_canvas()




