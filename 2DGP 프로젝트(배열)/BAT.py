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
        self.move_check=False
        self.image=load_image('bat.png')
        self.move=0
        self.life=1

    def update(self):
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 4
        self.move += 400 *115/60* game_framework.frame_time
        if(self.move>=800):
            if (abs(self.x - main_state.cadence.x) - abs(self.y - main_state.cadence.y) >= 0):
                if (self.x - main_state.cadence.x > 0):
                    if (self.x - 24 == main_state.cadence.x and self.y == main_state.cadence.y):
                        self.move_check = True
                    for i in range(2):
                        if (self.x - 24 == main_state.bat[i].x and self.y == main_state.bat[i].y):
                            self.move_check = True
                    for i in range(2):
                        if (self.x - 24 == main_state.skeleton[i].x and self.y == main_state.skeleton[i].y):
                            self.move_check = True
                    if self.move_check == False:
                        self.x -= 24

                elif (self.x - main_state.cadence.x < 0):
                    if (self.x + 24 == main_state.cadence.x and self.y == main_state.cadence.y):
                        self.move_check = True
                    for i in range(2):
                        if (self.x + 24 == main_state.bat[i].x and self.y == main_state.bat[i].y):
                            self.move_check = True
                    for i in range(2):
                        if (self.x + 24 == main_state.skeleton[i].x and self.y == main_state.skeleton[i].y):
                            self.move_check = True
                    if self.move_check == False:
                        self.x += 24

            elif (abs(self.x - main_state.cadence.x) - abs(self.y - main_state.cadence.y) < 0):
                if (self.y - main_state.cadence.y > 0):
                    if (self.x == main_state.cadence.x and self.y - 24 == main_state.cadence.y):
                        self.move_check = True
                    for i in range(2):
                        if (self.x == main_state.bat[i].x and self.y - 24 == main_state.bat[i].y):
                            self.move_check = True
                    for i in range(2):
                        if (self.x == main_state.skeleton[i].x and self.y - 24 == main_state.skeleton[i].y):
                            self.move_check = True
                    if self.move_check == False:
                        self.y -= 24

                elif (self.y - main_state.cadence.y < 0):
                    if (self.x == main_state.cadence.x and self.y + 24 == main_state.cadence.y):
                        self.move_check = True
                    for i in range(2):
                        if (self.x == main_state.bat[i].x and self.y + 24 == main_state.bat[i].y):
                            self.move_check = True
                    for i in range(2):
                        if (self.x == main_state.skeleton[i].x and self.y + 24 == main_state.skeleton[i].y):
                            self.move_check = True
                    if self.move_check == False:
                        self.y += 24
            self.move = 0
            self.move_check = False

    def draw(self):
        if(self.life>0):
            if(main_state.cadence.x>=self.x):
                self.image.clip_draw(int(self.frame) * 24, 24, 24, 28, self.x, self.y)
            elif(main_state.cadence.x<self.x):
                self.image.clip_composite_draw(int(self.frame)*24,24,24,28,0,'h',self.x,self.y,24,28)
