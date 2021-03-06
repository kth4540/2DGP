from pico2d import*
import random
import main_state
import game_framework

TIME_PER_ACTION = 1.0
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 8


class Dragon:
    def __init__(self):
        self.x, self.y = 104 + 24 * random.randint(1, 23), 500 - 24 * random.randint(1, 15)
        self.frame=0
        self.attack_frame=0
        self.fire_frame=0
        self.attack_check=False
        self.fire_check=False
        self.move_check=False
        self.fire_attack_frame=0
        self.image=load_image('dragon_blue.png')
        self.enemy_attack=load_image('enemy_attack.png')
        self.fire=load_image('ice_blast.png')
        self.move=0
        self.life=5

    def update(self):
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 4
        if self.attack_check==True:
            self.attack_frame= (self.attack_frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 6
            if self.attack_frame>5:
                self.attack_frame=0
                self.attack_check=False

        if self.fire_check==True:
            self.fire_frame= (self.fire_frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 5
            self.fire_attack_frame = (self.fire_attack_frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 4
            if self.fire_frame>4:
                self.fire_frame=0
                self.fire_check=False
                self.fire_attack_frame=0

        self.move += 400 *130/60* game_framework.frame_time
        if(self.move>=800 and self.life>0):
            if (abs(self.x - main_state.cadence.x) - abs(self.y - main_state.cadence.y) >= 0):
                if (self.x - main_state.cadence.x > 0):
                    if (self.x-main_state.cadence.x<=48 and self.y == main_state.cadence.y):
                        self.move_check = True
                        self.fire_check=True
                        main_state.cadence.life -= 3
                    for i in range(main_state.bat_num):
                        if (self.x - 24 == main_state.bat[i].x and self.y == main_state.bat[i].y):
                            self.move_check = True
                    for i in range(main_state.skel_num):
                        if (self.x - 24 == main_state.skeleton[i].x and self.y == main_state.skeleton[i].y):
                            self.move_check = True
                    if self.move_check == False:
                        self.x -= 24

                elif (self.x - main_state.cadence.x < 0):
                    if (main_state.cadence.x-self.x<=48 and self.y == main_state.cadence.y):
                        self.move_check = True
                        self.fire_check=True
                        main_state.cadence.life -= 3
                    for i in range(main_state.bat_num):
                        if (self.x + 24 == main_state.bat[i].x and self.y == main_state.bat[i].y):
                            self.move_check = True
                    for i in range(main_state.skel_num):
                        if (self.x + 24 == main_state.skeleton[i].x and self.y == main_state.skeleton[i].y):
                            self.move_check = True
                    if self.move_check == False:
                        self.x += 24

            elif (abs(self.x - main_state.cadence.x) - abs(self.y - main_state.cadence.y) < 0):
                if (self.y - main_state.cadence.y > 0):
                    if (self.x == main_state.cadence.x and self.y - 24 == main_state.cadence.y):
                        self.move_check = True
                        self.attack_check = True
                        main_state.cadence.life -= 2

                    for i in range(main_state.bat_num):
                        if (self.x == main_state.bat[i].x and self.y - 24 == main_state.bat[i].y):
                            self.move_check = True
                    for i in range(main_state.skel_num):
                        if (self.x == main_state.skeleton[i].x and self.y - 24 == main_state.skeleton[i].y):
                            self.move_check = True
                    if self.move_check == False:
                        self.y -= 24

                elif (self.y - main_state.cadence.y < 0):
                    if (self.x == main_state.cadence.x and self.y + 24 == main_state.cadence.y):
                        self.move_check = True
                        self.attack_check=True
                        main_state.cadence.life -= 2

                    for i in range(main_state.bat_num):
                        if (self.x == main_state.bat[i].x and self.y + 24 == main_state.bat[i].y):
                            self.move_check = True
                    for i in range(main_state.skel_num):
                        if (self.x == main_state.skeleton[i].x and self.y + 24 == main_state.skeleton[i].y):
                            self.move_check = True
                    if self.move_check == False:
                        self.y += 24
            self.move = 0
            self.move_check = False

    def draw(self):
        if (self.life > 0):
            if (main_state.cadence.x < self.x):
                if(self.fire_check==False):
                    self.image.clip_composite_draw(int(self.frame) * 61, 51, 61, 51, 0, ' ', self.x, self.y, 51, 41)
                elif(self.fire_check==True):
                    self.image.clip_composite_draw(int(self.fire_attack_frame+4) * 61, 51, 61, 51, 0, ' ', self.x, self.y, 51, 41)

            elif (main_state.cadence.x >= self.x):
                if (self.fire_check == False):
                    self.image.clip_composite_draw(int(self.frame) * 61, 51, 61, 51, 0, 'h', self.x, self.y, 51, 41)
                elif (self.fire_check == True):
                    self.image.clip_composite_draw(int(self.fire_attack_frame + 4) * 61, 51, 61, 51, 0, 'h', self.x, self.y, 51, 41)

            if (main_state.cadence.x < self.x):
                if self.attack_check == True:
                    self.enemy_attack.clip_composite_draw(int(self.attack_frame) * 27, 0, 27, 24, 0, ' ', self.x - 24,
                                                          self.y, 12, 12)
            elif (main_state.cadence.x > self.x):
                if self.attack_check == True:
                    self.enemy_attack.clip_composite_draw(int(self.attack_frame) * 27, 0, 27, 24, 0, ' ', self.x + 24,
                                                          self.y, 12, 12)
            elif (main_state.cadence.y > self.y):
                if self.attack_check == True:
                    self.enemy_attack.clip_composite_draw(int(self.attack_frame) * 27, 0, 27, 24, 0, ' ', self.x,
                                                          self.y + 24, 12, 12)
            elif (main_state.cadence.y < self.y):
                if self.attack_check == True:
                    self.enemy_attack.clip_composite_draw(int(self.attack_frame) * 27, 0, 27, 24, 0, ' ', self.x,
                                                          self.y - 24, 12, 12)

            if(main_state.cadence.x>self.x):
                if self.fire_check==True:
                    self.fire.clip_composite_draw(int(self.fire_frame+2)*88,0,88,109,0,'',self.x+48,self.y+12,48,72)
            elif (main_state.cadence.x <= self.x):
                if self.fire_check == True:
                    self.fire.clip_composite_draw(int(self.fire_frame+2) * 88, 0, 88, 109, 0, 'h', self.x - 48,
                                                  self.y + 12, 48, 72)

