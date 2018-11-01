from pico2d import*
import game_framework
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
        if event==RIGHT_ON:
            cadence.vertical+=1
        elif event==LEFT_ON:
            cadence.vertical-=1
        elif event==UP_ON:
            cadence.horizon+=1
        elif event==DOWN_ON:
            cadence.horizon-=1
        elif event==RIGHT_OFF:
            cadence.vertical-=1
        elif event==LEFT_OFF:
            cadence.vertical+=1
        elif event == UP_OFF:
            cadence.horizon -= 1
        elif event == DOWN_OFF:
            cadence.horizon += 1

    @staticmethod
    def exit(cadence,event):
        pass



    @staticmethod
    def do(cadence):
        cadence.frame = (cadence.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 4
        cadence.rhythm+=400*115/60*game_framework.frame_time
        if cadence.rhythm>=400:
            cadence.act=False
            cadence.rhythm=0

    @staticmethod
    def draw(cadence):
        cadence.image.clip_draw(int(cadence.frame) * 24, 24, 24, 24, cadence.x, cadence.y)

class RunState:
    @staticmethod
    def enter(cadence,event):
        if event==RIGHT_ON:
            cadence.vertical+=1
        elif event==LEFT_ON:
            cadence.vertical-=1
        elif event==UP_ON:
            cadence.horizon+=1
        elif event==DOWN_ON:
            cadence.horizon-=1
        elif event==RIGHT_OFF:
            cadence.vertical-=1
        elif event==LEFT_OFF:
            cadence.vertical+=1
        elif event == UP_OFF:
            cadence.horizon -= 1
        elif event == DOWN_OFF:
            cadence.horizon += 1

    @staticmethod
    def exit(cadence,event):
        pass

    @staticmethod
    def do(cadence):
        cadence.frame = (cadence.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 4
        if cadence.act==False:
            cadence.x += cadence.vertical * 24
            cadence.y += cadence.horizon * 24
            cadence.act=True
        cadence.rhythm += 400 * 115 / 60 * game_framework.frame_time
        if cadence.rhythm >= 400:
            cadence.act = False
            cadence.rhythm = 0




    @staticmethod
    def draw(cadence):
        cadence.image.clip_draw(int(cadence.frame) * 24, 24, 24, 24, cadence.x, cadence.y)


next_state_table={
    IdleState:{RIGHT_ON:RunState,LEFT_ON:RunState,UP_ON:RunState,DOWN_ON:RunState,
               RIGHT_OFF:IdleState, LEFT_OFF:IdleState, UP_OFF:IdleState,DOWN_OFF:IdleState},
    RunState:{RIGHT_ON:RunState,LEFT_ON:RunState,UP_ON:RunState,DOWN_ON:RunState,
               RIGHT_OFF:IdleState, LEFT_OFF:IdleState, UP_OFF:IdleState,DOWN_OFF:IdleState}
}


class Cadence:
    def __init__(self):
        self.x, self.y = 104+24, 500-24
        self.frame = 0
        self.vertical=0
        self.horizon=0
        self.image = load_image('clone.png')
        self.attack_sound=load_wav('attack.wav')
        self.rhythm=0
        self.act=True
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

    def tmp(self):
        print("HELLO")

    def draw(self):
        self.cur_state.draw(self)

    def handle_event(self, event):
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.add_event(key_event)


