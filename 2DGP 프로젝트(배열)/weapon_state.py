from pico2d import *

import game_framework
import main_state

name = "MainState"


knife=None
sword=None
rapier=None
sound=None



def enter():
    global knife,sword,rapier,sound
    knife = load_image('knife.png')
    sword = load_image('sword.png')
    rapier = load_image('rapier.png')
    sound=load_music('lobby.mp3')
    sound.set_volume(100)
    sound.repeat_play()


def exit():
    global knife, sword, rapier,sound
    del(sword)
    del(rapier)
    del(knife)
    del(sound)




def pause():
    pass


def resume():
    pass


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        elif event.type==SDL_KEYDOWN and event.key==SDLK_1:
            main_state.cadence_weapon = 0
            game_framework.change_state(main_state)


        elif event.type==SDL_KEYDOWN and event.key==SDLK_2:
            main_state.cadence_weapon = 1
            game_framework.change_state(main_state)


        elif event.type==SDL_KEYDOWN and event.key==SDLK_3:
            main_state.cadence_weapon = 2
            game_framework.change_state(main_state)


def update():
   pass


def draw():
    clear_canvas()

    knife.clip_composite_draw(0, 20, 19, 20, 0, ' ', 200 ,300, 48, 48)
    sword.clip_composite_draw(0, 24, 24, 24, 0, ' ', 400, 300, 48, 48)
    rapier.clip_composite_draw(0, 27, 26, 27, 0, ' ', 600, 300, 48, 48)

    update_canvas()
