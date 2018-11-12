from pico2d import*
import random
import game_framework
import main_state

TIME_PER_ACTION = 1.0
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 8


class Skeleton:
    def __init__(self):
        self.x,self.y=104+24*random.randint(1,23),500-24*random.randint(1,15)
        self.frame=0
        self.attack_frame=0
        self.move_check=False
        self.attack_check=False
        self.image=load_image('skeleton.png')
        self.enemy_attack=load_image('enemy_attack.png')
        self.move=0
        self.life=2

    def update(self):
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 4
        if self.attack_check==True:
            self.attack_frame= (self.attack_frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 6
            if self.attack_frame>4:
                self.attack_frame=0
                self.attack_check=False
        self.move+=400*115/60*game_framework.frame_time

        if(self.move>=800):
            if(abs(self.x-main_state.cadence.x)-abs(self.y-main_state.cadence.y)>=0):
                if(self.x-main_state.cadence.x>0):
                    if(self.x-24==main_state.cadence.x and self.y==main_state.cadence.y):
                        self.move_check=True
                        self.attack_check=True
                    for i in range(main_state.bat_num):
                        if(self.x-24==main_state.bat[i].x and self.y==main_state.bat[i].y):
                            self.move_check=True
                    for i in range(main_state.skel_num):
                        if(self.x-24==main_state.skeleton[i].x and self.y==main_state.skeleton[i].y):
                            self.move_check=True
                    if self.move_check==False:
                        self.x-=24

                elif(self.x-main_state.cadence.x<0):
                    if (self.x + 24 == main_state.cadence.x and self.y == main_state.cadence.y):
                        self.move_check = True
                        self.attack_check=True
                    for i in range(main_state.bat_num):
                        if (self.x + 24 == main_state.bat[i].x and self.y == main_state.bat[i].y):
                            self.move_check = True
                    for i in range(main_state.skel_num):
                        if (self.x + 24 == main_state.skeleton[i].x and self.y == main_state.skeleton[i].y):
                            self.move_check = True
                    if self.move_check == False:
                        self.x += 24

            elif(abs(self.x-main_state.cadence.x)-abs(self.y-main_state.cadence.y)<0):
                if(self.y-main_state.cadence.y>0):
                    if (self.x == main_state.cadence.x and self.y-24 == main_state.cadence.y):
                        self.move_check=True
                        self.attack_check=True
                    for i in range(main_state.bat_num):
                        if(self.x==main_state.bat[i].x and self.y-24==main_state.bat[i].y):
                            self.move_check=True
                    for i in range(main_state.skel_num):
                        if(self.x==main_state.skeleton[i].x and self.y-24==main_state.skeleton[i].y):
                            self.move_check=True
                    if self.move_check==False:
                        self.y-=24

                elif(self.y-main_state.cadence.y<0):
                    if (self.x == main_state.cadence.x and self.y+24 == main_state.cadence.y):
                        self.move_check=True
                        self.attack_check=True
                    for i in range(main_state.bat_num):
                        if(self.x==main_state.bat[i].x and self.y+24==main_state.bat[i].y):
                            self.move_check=True
                    for i in range(main_state.skel_num):
                        if(self.x==main_state.skeleton[i].x and self.y+24==main_state.skeleton[i].y):
                            self.move_check=True
                    if self.move_check==False:
                        self.y+=24
            self.move=0
            self.move_check=False

    def draw(self):
        if(self.life>0):
            if(main_state.cadence.x<self.x):
                self.image.clip_draw(int(self.frame) * 24, 24, 24, 28, self.x, self.y)
            elif(main_state.cadence.x>=self.x):
                self.image.clip_composite_draw(int(self.frame)*24,24,24,28,0,'h',self.x,self.y,24,28)

            if(main_state.cadence.x<self.x and main_state.cadence.y==self.y):
                if self.attack_check==True:
                    self.enemy_attack.clip_composite_draw(int(self.attack_frame)*27,0,27,24,0,' ',self.x-24,self.y,12,12)
            elif (main_state.cadence.x > self.x and main_state.cadence.y==self.y):
                if self.attack_check == True:
                    self.enemy_attack.clip_composite_draw(int(self.attack_frame) * 27, 0, 27, 24, 0, ' ', self.x + 24,self.y, 12, 12)
            elif (main_state.cadence.y > self.y and main_state.cadence.x==self.x):
                if self.attack_check == True:
                    self.enemy_attack.clip_composite_draw(int(self.attack_frame) * 27, 0, 27, 24, 0, ' ', self.x,self.y+24, 12, 12)
            elif (main_state.cadence.y < self.y and main_state.cadence.x==self.x):
                if self.attack_check == True:
                    self.enemy_attack.clip_composite_draw(int(self.attack_frame) * 27, 0, 27, 24, 0, ' ', self.x,self.y-24, 12, 12)
