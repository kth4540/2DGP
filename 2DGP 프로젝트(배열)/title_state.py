import game_framework
import main_state
from pico2d import *


name = "TitleState"
image = None
lobby_sound=None


def enter():
    global image
    global lobby_sound
    image=load_image('mainmenu.png')
    lobby_sound=load_music('lobby.mp3')
    lobby_sound.set_volume(50)
    lobby_sound.play()

def exit():
    global image
    global lobby_sound
    del(image)
    del(lobby_sound)


def handle_events():
    events=get_events()
    for event in events:
        if event.type==SDL_QUIT:
            game_framework.quit()
        else:
            if(event.type,event.key)==(SDL_KEYDOWN,SDLK_ESCAPE):
                game_framework.quit()
            elif(event.type,event.key)==(SDL_KEYDOWN,SDLK_SPACE):
                game_framework.change_state(main_state)




def draw():
    clear_canvas()
    image.clip_composite_draw(0,0,480,270,0,' ',400,300,800,600)
    update_canvas()







def update():
    pass


def pause():
    pass


def resume():
    pass






