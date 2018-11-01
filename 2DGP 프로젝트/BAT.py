from pico2d import*
import main_state
import game_framework

TIME_PER_ACTION = 1.0
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 8


class Bat:
    def __init__(self):
        self.x,self.y=104+24*8,500-24
        self.frame=0
        self.image=load_image('bat.png')
        self.move=0
        self.life=1

    def update(self):
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 4
        self.move += 400 *115/60* game_framework.frame_time
        if(self.move>=800):
            if(abs(self.x-main_state.cadence.x)-abs(self.y-main_state.cadence.y)>=0):
                if(self.x-main_state.cadence.x>0):
                    if(self.x-24==main_state.cadence.x and self.y==main_state.cadence.y): # 캐릭터와 충돌
                        pass
                    elif(self.x - 24 == main_state.skeleton.x and self.y == main_state.skeleton.y): # skeletion과 충돌
                        pass
                    else:
                        self.x-=24

                elif(self.x-main_state.cadence.x<0):
                    if (self.x + 24 == main_state.cadence.x and self.y == main_state.cadence.y):
                        pass
                    elif(self.x + 24 == main_state.skeleton.x and self.y == main_state.skeleton.y):
                        pass
                    else:
                        self.x+=24


            elif(abs(self.x-main_state.cadence.x)-abs(self.y-main_state.cadence.y)<0):
                if(self.y-main_state.cadence.y>0):
                    if (self.x == main_state.cadence.x and self.y-24 == main_state.cadence.y):
                        pass
                    elif(self.x == main_state.skeleton.x and self.y-24 == main_state.skeleton.y):
                        pass
                    else:
                        self.y-=24

                elif(self.y-main_state.cadence.y<0):
                    if (self.x == main_state.cadence.x and self.y + 24 == main_state.cadence.y):
                        pass
                    elif(self.x== main_state.cadence.x and self.y+24 == main_state.skeleton.y):
                        pass
                    else:
                        self.y+=24
            self.move=0

    def draw(self):
        if(self.life!=0):
            self.image.clip_draw(int(self.frame) * 24, 24, 24, 28, self.x, self.y)
