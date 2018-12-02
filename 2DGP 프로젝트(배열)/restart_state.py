import game_framework
import title_state
from pico2d import *
import main_state
import weapon_state

from SKELETON import Skeleton
from BAT import Bat
from DRAGON import Dragon


name = "TitleState"
death=None
restart=None


def enter():
    global death,restart
    death=load_wav('cadence_death.wav')
    death.play()
    restart=load_image('restart.png')

def exit():
    global death
    del(death)



def handle_events():
    events=get_events()
    for event in events:
        if event.type==SDL_QUIT:
            game_framework.quit()
        else:
            if(event.type,event.key)==(SDL_KEYDOWN,SDLK_ESCAPE):
                del (main_state.cadence)
                del (main_state.heart)
                del (main_state.stick)
                del (main_state.skeleton)
                del (main_state.bat)
                del (main_state.dragon)
                del (main_state.map)
                del (main_state.choose_sound)
                game_framework.quit()
            elif(event.type,event.key)==(SDL_KEYDOWN,SDLK_SPACE):

                main_state.skeleton = []
                main_state.skel_num = 2
                main_state.bat = []
                main_state.bat_num = 2
                main_state.dragon = []
                main_state.dragon_num = 1

                for i in range(main_state.skel_num):
                    main_state.skeleton.append(Skeleton())
                for i in range(main_state.bat_num):
                    main_state.bat.append(Bat())
                for i in range(main_state.dragon_num):
                    main_state.dragon.append(Dragon())

                game_framework.change_state(weapon_state)


def draw():
    clear_canvas()
    restart.draw(400,300)
    update_canvas()







def update():
    pass


def pause():
    pass


def resume():
    pass