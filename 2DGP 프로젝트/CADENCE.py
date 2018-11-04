from pico2d import*
import game_framework
import math

import main_state
# 프레임
TIME_PER_ACTION = 1.0
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 8

#cadence event

RIGHT_ON, LEFT_ON, UP_ON, DOWN_ON,RIGHT_OFF,LEFT_OFF,UP_OFF,DOWN_OFF = range(8)

key_event_table = {
    (SDL_KEYDOWN, SDLK_RIGHT): RIGHT_ON,
    (SDL_KEYDOWN, SDLK_LEFT): LEFT_ON,
    (SDL_KEYDOWN, SDLK_UP): UP_ON,
    (SDL_KEYDOWN, SDLK_DOWN): DOWN_ON,
    (SDL_KEYUP, SDLK_RIGHT): RIGHT_OFF,
    (SDL_KEYUP, SDLK_LEFT): LEFT_OFF,
    (SDL_KEYUP, SDLK_UP): UP_OFF,
    (SDL_KEYUP, SDLK_DOWN): DOWN_OFF
}

class IdleState:
    @staticmethod
    def enter(cadence,event):
        if event==RIGHT_ON and cadence.rhythm>=300:
            cadence.dir=1
        elif event==LEFT_ON and cadence.rhythm>=300:
            cadence.dir=-1
        elif event==UP_ON:
            pass
        elif event==DOWN_ON:
            pass
        elif event==RIGHT_OFF:
            pass
        elif event==LEFT_OFF:
            pass
        elif event == UP_OFF:
            pass
        elif event == DOWN_OFF:
            pass

    @staticmethod
    def exit(cadence,event):
        if event==RIGHT_ON and cadence.act==False and cadence.rhythm>=300:
            if (cadence.x + 24 == main_state.bat.x and cadence.y == main_state.bat.y):
                main_state.bat.life -= 1
                main_state.bat.x = None
                main_state.bat.y = None
                cadence.attack_dir=0
                cadence.attack()
            elif(cadence.x + 24 == main_state.skeleton.x and cadence.y == main_state.skeleton.y):
                main_state.skeleton.life -= 1
                main_state.skeleton.x = None
                main_state.skeleton.y = None
                cadence.attack_dir = 0
                cadence.attack()
            else:
                cadence.x+=24
            cadence.act = True
        elif event==LEFT_ON and cadence.act==False and cadence.rhythm>=300:
            if (cadence.x - 24 == main_state.bat.x and cadence.y == main_state.bat.y):
                main_state.bat.life -= 1
                main_state.bat.x=None
                main_state.bat.y=None
                cadence.attack_dir = 1
                cadence.attack()
            elif (cadence.x - 24 == main_state.skeleton.x and cadence.y == main_state.skeleton.y):
                main_state.skeleton.life -= 1
                main_state.skeleton.x = None
                main_state.skeleton.y = None
                cadence.attack_dir = 1
                cadence.attack()
            else:
                cadence.x -= 24
            cadence.act = True
        elif event==DOWN_ON and cadence.act==False and cadence.rhythm>=300:
            if (cadence.y - 24 == main_state.bat.y and cadence.x == main_state.bat.x):
                main_state.bat.life -= 1
                main_state.bat.x = None
                main_state.bat.y = None
                cadence.attack_dir = 2
                cadence.attack()
            elif (cadence.y - 24 == main_state.skeleton.y and cadence.x == main_state.skeleton.x):
                main_state.skeleton.life -= 1
                main_state.skeleton.x = None
                main_state.skeleton.y = None
                cadence.attack_dir = 2
                cadence.attack()
            else:
                cadence.y -= 24
            cadence.act = True
        elif event==UP_ON and cadence.act==False and cadence.rhythm>=300:
            if (cadence.y + 24 == main_state.bat.y and cadence.x == main_state.bat.x):
                main_state.bat.life -= 1
                main_state.bat.x = None
                main_state.bat.y = None
                cadence.attack_dir = 3
                cadence.attack()
            elif (cadence.y + 24 == main_state.skeleton.y and cadence.x == main_state.skeleton.x):
                main_state.skeleton.life -= 1
                main_state.skeleton.x = None
                main_state.skeleton.y = None
                cadence.attack_dir = 3
                cadence.attack()
            else:
                cadence.y += 24
            cadence.act = True




    @staticmethod
    def do(cadence):
        cadence.frame = (cadence.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 4
        if cadence.attack_check==True:
            cadence.attack_frame=(cadence.attack_frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 4
        if(cadence.attack_frame>3):
            cadence.attack_frame=0
            cadence.attack_check=False

        cadence.rhythm+=400*115/60*game_framework.frame_time
        if cadence.rhythm>=400:
            cadence.act=False
            cadence.rhythm=0

    @staticmethod
    def draw(cadence):
        if cadence.dir==1:
            cadence.image.clip_composite_draw(int(cadence.frame) * 24, 24, 24, 24,0,' ' ,cadence.x, cadence.y,24,24)

        else:
            cadence.image.clip_composite_draw(int(cadence.frame) * 24, 24, 24, 24, 0, 'h', cadence.x, cadence.y, 24, 24)

        if (cadence.attack_check == True and cadence.attack_dir == 0):
            cadence.attack_effect.clip_composite_draw(int(cadence.attack_frame) * 24, 0, 24, 24, 0, ' ', cadence.x + 12,cadence.y, 24, 24)
        elif (cadence.attack_check == True and cadence.attack_dir==1):
            cadence.attack_effect.clip_composite_draw(int(cadence.attack_frame) * 24, 0, 24, 24, 0, 'h', cadence.x - 12,cadence.y, 24, 24)
        elif (cadence.attack_check == True and cadence.attack_dir == 2):
            cadence.attack_effect.clip_composite_draw(int(cadence.attack_frame) * 24, 0, 24, 24, math.radians(-90), '', cadence.x,cadence.y-12, 24, 24)
        elif (cadence.attack_check == True and cadence.attack_dir == 3):
            cadence.attack_effect.clip_composite_draw(int(cadence.attack_frame) * 24, 0, 24, 24, math.radians(90), '', cadence.x,cadence.y+12, 24, 24)

next_state_table={
    IdleState:{RIGHT_ON:IdleState,LEFT_ON:IdleState,UP_ON:IdleState,DOWN_ON:IdleState,
               RIGHT_OFF:IdleState, LEFT_OFF:IdleState, UP_OFF:IdleState,DOWN_OFF:IdleState}

}


class Cadence:
    def __init__(self):
        self.x, self.y = 104+24, 500-24
        self.moving_x,self.moving_y=104+24,500-24
        self.frame = 0
        self.attack_frame=0
        self.attack_check=False
        self.image = load_image('clone.png')
        self.attack_sound=load_wav('attack.wav')
        self.attack_effect=load_image('attack_effect.png')
        self.rhythm=0
        self.act=True
        self.dir=1
        self.attack_dir=0
        self.event_que=[]
        self.cur_state=IdleState
        self.cur_state.enter(self,None)

    def add_event(self, event):
        self.event_que.insert(0, event)

    def update(self):
        self.cur_state.do(self)
        if len(self.event_que) > 0:
            event = self.event_que.pop()
            self.cur_state.exit(self, event)
            self.cur_state = next_state_table[self.cur_state][event]
            self.cur_state.enter(self, event)

    def attack(self):
        self.attack_sound.set_volume(500)
        self.attack_sound.play()
        self.attack_check=True


    def draw(self):
        self.cur_state.draw(self)

    def handle_event(self, event):
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.add_event(key_event)

